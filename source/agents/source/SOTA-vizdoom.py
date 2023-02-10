# !/usr/bin/env python3
# ************************************************************************************************ #
# **                                                                                            ** #
# **    AIQ-SAIL-ON SOTA Agent Example                                                          ** #
# **                                                                                            ** #
# **        Brian L Thomas, 2020                                                                ** #
# **        Vincent Lombardi 2021                                                               ** #
# **                                                                                            ** #
# **  Tools by the AI Lab - Artificial Intelligence Quotient (AIQ) in the School of Electrical  ** #
# **  Engineering and Computer Science at Washington State University.                          ** #
# **                                                                                            ** #
# **  Copyright Washington State University, 2020                                               ** #
# **  Copyright Brian L. Thomas, 2020                                                           ** #
# **                                                                                            ** #
# **  All rights reserved                                                                       ** #
# **  Modification, distribution, and sale of this work is prohibited without permission from   ** #
# **  Washington State University.                                                              ** #
# **                                                                                            ** #
# **  Contact: Brian L. Thomas (bthomas1@wsu.edu)                                               ** #
# **  Contact: Larry Holder (holder@wsu.edu)                                                    ** #
# **  Contact: Diane J. Cook (djcook@wsu.edu)                                                   ** #
# **  Contact: Vincent Lombardi (vincent.lombardi@wsu.edu)                                      ** #
# ************************************************************************************************ #

import copy
import optparse
import random
import time

from objects.SOTA_logic import SotaLogic
from objects import objects

import torch
from sota_util.phase_3.doomnet.doom_net import Net as net
from sota_util.phase_3.doomnet.myutil import v_wrap, tracker, target_sighted, get_angle, get_dist, target_in_room, navigate, gunner
import numpy as np


class SotaAgent(SotaLogic):
    def __init__(self):
        super().__init__()
        torch.manual_seed(123)

        self.possible_answers = list()
        self.possible_answers.append(dict({'action': 'nothing'}))
        self.possible_answers.append(dict({'action': 'left'}))
        self.possible_answers.append(dict({'action': 'right'}))
        self.possible_answers.append(dict({'action': 'forward'}))
        self.possible_answers.append(dict({'action': 'backward'}))
        self.possible_answers.append(dict({'action': 'shoot'}))
        self.possible_answers.append(dict({'action': 'turn_left'}))
        self.possible_answers.append(dict({'action': 'turn_right'}))

        self.gnav = None


        self.pl_x = 0  # previous move x coord
        self.pl_y = 0  # previous move y coord
        self.navigation = False
        self.resupply = False  # find health or ammo
        self.r_load = False
        self.traveling = False
        self.medic = False
        self.manual = False  # safeguard for if the navigation agent gets stuck
        self.fired = False
        self.pact = 0  # previous action
        self.e_count = 0
        self.e_list = {}

        self.actions = [1, 2, 4, 3, 6, 7]

        self.c_list = [{"x_position": 0.0, "y_position": 0.0}, {"x_position": 0.0, "y_position": 488.0},
                       {"x_position": 0.0, "y_position": -488.0}, {"x_position": 488.0, "y_position": 0.0},
                       {"x_position": -488.0, "y_position": 0.0}]

        # This variable can be set to true and the system will attempt to end training at the
        # completion of the current episode, or sooner if possible.
        self.end_training_early = True

        # This variable is checked only during the evaluation phase.  If set to True the system
        # will attempt to cleanly end the experiment at the conclusion of the current episode,
        # or sooner if possible.
        self.end_experiment_early = False

        return

    def reset_vars(self):
        self.pl_x = 0
        self.pl_y = 0

        self.pact = 0
        self.traveling = False
        self.navigation = False
        self.resupply = False  # find health or ammo
        self.r_load = False
        self.medic = False
        self.manual = False
        self.fired = False
        self.e_list = {}
        self.e_count = 0

    # named after the main character of doom
    def slayer_agent(self, feature_vector: dict) -> dict:
        """Process an episode data instance.
        Parameters
        ----------
        feature_vector : dict
            The dictionary of the feature vector.  Domain specific feature vector formats are
            defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
        Returns
        -------
        dict
            A dictionary of your label prediction of the format {'action': label}.  This is
                strictly enforced and the incorrect format will result in an exception being thrown.
        """

        found_error = False
        # Check for some error conditions and provide helpful feedback.
        if 'enemies' not in feature_vector:
            self.log.error('This does not appear to be a vizdoom feature vector! Did you forget '
                           'to set the correct domain in the agent config file?')
            found_error = True

        player = feature_vector['player']

        pl_x2 = player['x_position']
        pl_y2 = player['y_position']

        hit = False

        health = int(player['health'])
        items = feature_vector['items']
        ammo = int(player['ammo'])
        p_coord = tracker(player)
        if ammo < 1 and len(items['ammo']) <= 0:  # end the round quickly
            return self.possible_answers[0]

        state_vec, nav_vec, e_temp, elist, barrage, turn_l, turn_r = self.breaker(feature_vector)
        if self.e_count == 0 and e_temp > 0:
            self.e_list = elist
            self.e_count = e_temp

        if ammo >= 3 and self.r_load:
            self.r_load = False
            self.resupply = False

        if health > 30 and self.medic:
            self.resupply = False
            self.medic = False

        if int(self.pl_x) == int(pl_x2) and int(self.pl_y) == int(pl_y2):
            if self.pact == 0 or self.pact == 1 or self.pact == 2 or self.pact == 3:
                if self.navigation and ammo > 0:
                    if self.resupply:
                        self.manual = True
                        self.medic = False
                        self.r_load = False

        for key in elist.keys():
            if key in self.e_list.keys():
                if elist[key] < self.e_list[key]:
                    if self.fired:
                        hit = True

        if self.fired and not hit:  # prevents out of control spam firing
            self.manual = False
        self.e_list = elist

        self.pl_x = pl_x2
        self.pl_y = pl_y2

        if e_temp < self.e_count:
            self.e_count -= 1

        label_prediction = self.possible_answers[5]
        act = np.dtype('int64').type(4)  # shooting is default
        self.fired = False

        self.navigation = False
        if ammo < 1:
            self.manual = False

        tir = target_in_room(feature_vector['enemies'], p_coord)
        if barrage and ammo > 0:  # essentially a smart gun that forces the agent to fire or turn towards easy targets
            self.fired = True
            self.navigation = True

        elif turn_l and ammo > 0:
            act = np.dtype('int64').type(5)
            label_prediction = self.possible_answers[6]
            self.navigation = True

        elif turn_r and ammo > 0:
            act = np.dtype('int64').type(6)
            label_prediction = self.possible_answers[7]
            self.navigation = True

        else:
            if tir and (ammo > 0 or len(items['ammo']) <= 0):  # and not resupply:
                t_dist = get_dist(player, self.c_list[0])

                if tir and p_coord == 1 and t_dist > 300 and not self.traveling:
                    self.navigation = True
                    self.traveling = True
                    nav_vec[5] = self.c_list[0]['x_position']
                    nav_vec[6] = self.c_list[0]['y_position']
                    nav_vec[7] = t_dist
                    act = self.gnav.choose_action(v_wrap(nav_vec[None, :]))
                    label_prediction = self.possible_answers[self.actions[act]]


                elif tir and p_coord == 1 and t_dist > 275 and self.traveling:
                    self.navigation = True
                    nav_vec[5] = self.c_list[0]['x_position']
                    nav_vec[6] = self.c_list[0]['y_position']
                    nav_vec[7] = t_dist
                    act = self.gnav.choose_action(v_wrap(nav_vec[None, :]))
                    label_prediction = self.possible_answers[self.actions[act]]

                else:
                    self.traveling = False
                    nav_vec[5] = self.c_list[p_coord - 1]['x_position']
                    nav_vec[6] = self.c_list[p_coord - 1]['y_position']
                    nav_vec[7] = get_dist(player, self.c_list[p_coord - 1])
                    act = self.gnav.choose_action(v_wrap(nav_vec[None, :]))
                    label_prediction = self.possible_answers[self.actions[act]]
            else:  # navigation net

                if health <= 30 and len(items['health']) > 0 and not self.manual and not tir:
                    med = self.break_health(items, player, p_coord, feature_vector['enemies'])

                    m_coord = tracker(med)
                    if m_coord == p_coord:
                        nav_vec[5] = float(med['x_position'])
                        nav_vec[6] = float(med['y_position'])
                        nav_vec[7] = get_dist(player, med)
                        self.resupply = True
                        self.medic = True


                    elif p_coord == 1:
                        targ_coord = m_coord
                        nav_vec[5] = self.c_list[m_coord - 1]['x_position']
                        nav_vec[6] = self.c_list[m_coord - 1]['y_position']
                        nav_vec[7] = get_dist(player, self.c_list[targ_coord - 1])
                    else:
                        nav_vec[5] = self.c_list[0]['x_position']
                        nav_vec[6] = self.c_list[0]['y_position']
                        nav_vec[7] = get_dist(player, self.c_list[0])

                elif ((ammo > 2 and not tir) or (ammo < 1 and tir)) and len(items['ammo']) > 0 and not self.manual:
                    clip = self.break_ammo(items, player, p_coord, feature_vector['enemies'])
                    a_coord = tracker(clip)

                    if a_coord == p_coord:
                        nav_vec[5] = float(clip['x_position'])
                        nav_vec[6] = float(clip['y_position'])
                        nav_vec[7] = get_dist(player, clip)
                        self.r_load = True
                        self.resupply = True

                    elif p_coord == 1:
                        targ_coord = a_coord
                        nav_vec[5] = self.c_list[a_coord - 1]['x_position']
                        nav_vec[6] = self.c_list[a_coord - 1]['y_position']
                        nav_vec[7] = get_dist(player, self.c_list[targ_coord - 1])

                    else:
                        nav_vec[5] = self.c_list[0]['x_position']
                        nav_vec[6] = self.c_list[0]['y_position']
                        nav_vec[7] = get_dist(player, self.c_list[0])  # [targ_coord - 1])

                else:  # p_coord == targ_coord and not resupply and ammo > 1:
                    targ_coord = navigate(feature_vector['enemies'], p_coord, player)

                    nav_vec[5] = self.c_list[targ_coord - 1]['x_position']
                    nav_vec[6] = self.c_list[targ_coord - 1]['y_position']
                    nav_vec[7] = get_dist(player, self.c_list[targ_coord - 1])
                self.traveling = False
                self.navigation = True
                act = self.gnav.choose_action(v_wrap(nav_vec[None, :]))
                label_prediction = self.possible_answers[self.actions[act]]

        self.pact = act

        return label_prediction

    def reset_slayer(self):
        self.gnav = None
        self.gnav = net(20, 6, 64, 32)
        self.gnav.load_state_dict(torch.load("sota_util/phase_3/doomnet/navigation2.txt"))


    def initialize_sota_agent(self):
        """The SOTA agent does not exit after completing an experiment, so this function is
        called explicitly when we start a new experiment to set up anything for the agent.
        """
        # This variable can be set to true and the system will attempt to end training at the
        # completion of the current episode, or sooner if possible.
        self.end_training_early = True
        # This variable is checked only during the evaluation phase.  If set to True the system
        # will attempt to cleanly end the experiment at the conclusion of the current episode,
        # or sooner if possible.
        self.end_experiment_early = False

        # Reset agent every trial :D
        # self.agent = None
        # self.agent = Simple()
        self.reset_slayer()

        return

    def experiment_start(self):
        """This function is called when this TA2 has connected to a TA1 and is ready to begin
        the experiment.
        """
        self.log.info('Experiment Start')
        return

    def training_start(self):
        """This function is called when we are about to begin training on episodes of data in
        your chosen domain.
        """
        self.log.info('Training Start')
        return

    def training_episode_start(self, episode_number: int):
        """This function is called at the start of each training episode, with the current episode
        number (0-based) that you are about to begin.
        Parameters
        ----------
        episode_number : int
            This identifies the 0-based episode number you are about to begin training on.
        """
        self.reset_vars()

        self.log.info('Training Episode Start: #{}'.format(episode_number))
        return

    def training_instance(self, feature_vector: dict, feature_label: dict) -> dict:
        """Process a training instance.
        Parameters
        ----------
        feature_vector : dict
            The dictionary of the feature vector.  Domain specific feature vectors are defined
            on the github (https://github.com/holderlb/WSU-SAILON-NG).
        feature_label : dict
            The dictionary of the label for this feature vector.  Domain specific feature labels
            are defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
        Returns
        -------
        dict
            A dictionary of your label prediction of the format {'action': label}.  This is
                strictly enforced and the incorrect format will result in an exception being thrown.
        """
        self.log.debug('Training Instance: feature_vector={}  feature_label={}'.format(
            feature_vector, feature_label))

        # Here is where the agent makes a prediction
        label_prediction = self.slayer_agent(feature_vector=feature_vector)  # self.agent.predict(feature_vector)

        return label_prediction

    def training_performance(self, performance: float, feedback: dict = None):
        """Provides the current performance on training after each instance.
        Parameters
        ----------
        performance : float
            The normalized performance score.
        feedback : dict, optional
            A dictionary that may provide additional feedback on your prediction based on the
            budget set in the TA1. If there is no feedback, the object will be None.
        """
        self.log.debug('Training Performance: {}'.format(performance))
        return

    def training_episode_end(self, performance: float, feedback: dict = None) -> \
            (float, float, int, dict):
        """Provides the final performance on the training episode.
        Parameters
        ----------
        performance : float
            The final normalized performance score of the episode.
        feedback : dict, optional
            A dictionary that may provide additional feedback on your prediction based on the
            budget set in the TA1. If there is no feedback, the object will be None.
        Returns
        -------
        float, float, int, dict
            A float of the probability of there being novelty.
            A float of the probability threshold for this to evaluate as novelty detected.
            Integer representing the predicted novelty level.
            A JSON-valid dict characterizing the novelty.
        """
        self.log.info('Training Episode End: performance={}'.format(performance))

        novelty_probability = random.random()
        novelty_threshold = self.novelty_threshold
        novelty = 0
        novelty_characterization = dict()

        return novelty_probability, novelty_threshold, novelty, novelty_characterization

    def training_end(self):
        """This function is called when we have completed the training episodes.
        """
        self.log.info('Training End')
        return

    def train_model(self):
        """Train your model here if needed.  If you don't need to train, just leave the function
        empty.  After this completes, the logic calls save_model() and reset_model() as needed
        throughout the rest of the experiment.
        """
        self.log.info('Train the model here if needed.')

        return

    def save_model(self, filename: str):
        """Save the current trained model to disk so agent can reset to it at the start of
        each trial.
        Parameters
        ----------
        filename : str
            The filename to save the model to.
        """
        self.log.info('Save model to disk.')
        return

    def reset_model(self, filename: str):
        """Reset model to state just after training.
        Parameters
        ----------
        filename : str
            The filename where the model was stored.
        """
        self.log.info('Load model from disk.')
        # self.agent = None
        # self.agent = Simple()

        self.reset_slayer()

        return

    def trial_start(self, trial_number: int, novelty_description: dict):
        """This is called at the start of a trial with the current 0-based number.
        Parameters
        ----------
        trial_number : int
            This is the 0-based trial number in the novelty group.
        novelty_description : dict
            A dictionary that will have a description of the trial's novelty.
        """
        self.log.info('Trial Start: #{}  novelty_desc: {}'.format(trial_number,
                                                                  str(novelty_description)))
        return

    def testing_start(self):
        """This is called after a trial has started but before we begin going through the
        episodes.
        """
        self.log.info('Testing Start')
        return

    def testing_episode_start(self, episode_number: int):
        """This is called at the start of each testing episode in a trial, you are provided the
        0-based episode number.
        Parameters
        ----------
        episode_number : int
            This is the 0-based episode number in the current trial.
        """
        self.log.info('Testing Episode Start: #{}'.format(episode_number))

        return

    def testing_instance(self, feature_vector: dict, novelty_indicator: bool = None) -> dict:
        """Evaluate a testing instance.  Returns the predicted label or action, if you believe
        this episode is novel, and what novelty level you beleive it to be.
        Parameters
        ----------
        feature_vector : dict
            The dictionary containing the feature vector.  Domain specific feature vectors are
            defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
        novelty_indicator : bool, optional
            An indicator about the "big red button".
                - True == novelty has been introduced.
                - False == novelty has not been introduced.
                - None == no information about novelty is being provided.
        Returns
        -------
        dict
            A dictionary of your label prediction of the format {'action': label}.  This is
                strictly enforced and the incorrect format will result in an exception being thrown.
        """
        self.log.debug('Testing Instance: feature_vector={}, novelty_indicator={}'.format(
            feature_vector, novelty_indicator))

        # This is where the agent makes a prediction
        # label_prediction = self.agent.predict(feature_vector)
        label_prediction = self.slayer_agent(feature_vector=feature_vector)
        return label_prediction

    def testing_performance(self, performance: float, feedback: dict = None):
        """Provides the current performance on training after each instance.
        Parameters
        ----------
        performance : float
            The normalized performance score.
        feedback : dict, optional
            A dictionary that may provide additional feedback on your prediction based on the
            budget set in the TA1. If there is no feedback, the object will be None.
        """
        return

    def testing_episode_end(self, performance: float, feedback: dict = None) -> \
            (float, float, int, dict):
        """Provides the final performance on the testing episode.
        Parameters
        ----------
        performance : float
            The final normalized performance score of the episode.
        feedback : dict, optional
            A dictionary that may provide additional feedback on your prediction based on the
            budget set in the TA1. If there is no feedback, the object will be None.
        Returns
        -------
        float, float, int, dict
            A float of the probability of there being novelty.
            A float of the probability threshold for this to evaluate as novelty detected.
            Integer representing the predicted novelty level.
            A JSON-valid dict characterizing the novelty.
        """
        self.log.info('Testing Episode End: performance={}'.format(performance))

        novelty_probability = self.novelty_guess
        novelty_threshold = self.novelty_threshold
        novelty = random.choice(objects.VALID_NOVELTY)
        novelty_characterization = dict()

        return novelty_probability, novelty_threshold, novelty, novelty_characterization

    def testing_end(self):
        """This is called after the last episode of a trial has completed, before trial_end().
        """
        self.log.info('Testing End')
        return

    def trial_end(self):
        """This is called at the end of each trial.
        """
        self.log.info('Trial End')
        return

    def experiment_end(self):
        """This is called when the experiment is done.
        """
        self.log.info('Experiment End')
        return

    def break_health(self, items, player, p_coord, enemies):
        if len(items['health']) <= 0:
            return None
        min_dist = 10000

        m_health = None
        med_list = items['health']
        for h in med_list:
            dist = get_dist(player, h)
            if min_dist > dist:
                min_dist = dist
                m_health = h

        m_coord = tracker(m_health)
        if m_coord != p_coord:
            for h in med_list:
                h_c = tracker(h)
                if h_c == p_coord:
                    m_health = h
                    m_coord = h_c
                    break

        if m_coord != 1 and p_coord == m_coord:
            hazard = False
            for e in enemies:
                if tracker(e) == m_coord:
                    hazard = True
                    break
            if hazard:
                for h in med_list:
                    if tracker(h) == 1:
                        m_health = h
                        break

        return m_health

    def break_ammo(self, items, player, p_coord, enemies):
        clip_list = items['ammo']
        if len(clip_list) <= 0:
            return None
        min_dist = 10000

        m_ammo = None

        for a in clip_list:
            dist = get_dist(player, a)
            if min_dist > dist:
                min_dist = dist
                m_ammo = a

        if player['ammo'] < 3 and len(enemies) > 0:
            a_coord = tracker(m_ammo)
            if a_coord != p_coord:
                for a in clip_list:
                    a_c = tracker(a)
                    if a_c == p_coord:
                        m_ammo = a
                        a_coord = a_c
                        break

            if a_coord != 1 and p_coord == a_coord:
                hazard = False
                for e in enemies:
                    if tracker(e) == a_coord:
                        hazard = True
                        break
                if hazard:
                    for a in clip_list:
                        if tracker(a) == 1:
                            m_ammo = a
                            break

        return m_ammo

    def break_traps(self, items, player):
        temp = []
        temp2 = []
        if len(items['trap']) <= 0:
            return [0.0, 0.0], [0.0, 0.0, 0.0]

        min_dist = 10000
        m_trap = items['trap'][0]
        for t in items['trap']:
            dist = get_dist(player, t)
            if min_dist > dist:
                min_dist = dist
                m_trap = t

        temp.append(min_dist)
        temp.append(get_angle(m_trap, player, 0.0))
        temp2.append(float(m_trap['x_position']))
        temp2.append(float(m_trap['y_position']))
        temp2.append(min_dist)

        return temp, temp2

    def break_obstacles(self, items, player):
        temp = []
        temp2 = []
        o_list = []

        i = len(items['obstacle'])
        min_dist = 10000
        m_obst = None

        for o in items['obstacle']:
            dist = get_dist(player, o)
            #temp.append(dist)
            #temp.append(get_angle(o, player, 0.0))
            if target_sighted(o, player):
                if gunner(o, player, 0.0, 30.0):
                    o_list.append(dist)

            if min_dist > dist:
                min_dist = dist
                m_obst = o
        """
        while i < 4:
            temp.append(0.0)
            temp.append(0.0)
            i += 1
        """
        if len(items['obstacle']) <= 0:
            temp2 = [0.0, 0.0, 0.0]
        else:
            temp2.append(float(m_obst['x_position']))
            temp2.append(float(m_obst['y_position']))
            temp2.append(min_dist)

        return temp, temp2, o_list

    def break_enemy(self, enemies, player):
        temp = []
        temp2 = {}
        temp3 = []
        min_dist = 10000
        m_enemy = None
        i = len(enemies)
        for e in enemies:
            e_health = int(e['health'])
            temp2[int(e['id'])] = e_health
            dist = get_dist(player, e)

            if min_dist > dist and target_sighted(e, player):
                min_dist = dist
                m_enemy = e
            """
            angle = get_angle(e, player, 0.0)
            temp.append(e['x_position'])
            temp.append(e['y_position'])
            temp.append(angle)
            temp.append(dist)
            temp.append(e_health)
            """
        """
        while i < 4:
            temp.append(0)
            temp.append(0)
            temp.append(0)
            temp.append(0)
            temp.append(0)
            i += 1
        """
        if not m_enemy:
            temp3 = [0.0, 0.0, 10000.0]
        else:
            temp3.append(float(m_enemy['x_position']))
            temp3.append(float(m_enemy['y_position']))
            temp3.append(min_dist)

        return temp, temp2, temp3


    def breaker(self, state):
        """ master function for breaking apart feature vector takes in state
        returns
        state_vec (for combat)
        nav_vec (for navigation)
        e_count or number of enemies
        elist list of enemy ids and health
        barrage whether agent needs to shoot
        turn_l should agent turn left
        turn_r should agent turn right
        """

        enemies = state['enemies']
        items = state['items']
        player = state['player']

        barrage = False
        turn_l = False
        turn_r = False
        #targets, elist, e_temp2 = self.break_enemy(enemies, player)
        _, elist, e_temp2 = self.break_enemy(enemies, player)

        #obstacles, ob_temp2, o_list = self.break_obstacles(items, player)
        _, ob_temp2, o_list = self.break_obstacles(items, player)

        if player['ammo'] > 0:
            for e in enemies:
                if target_sighted(e, player):
                    dist = get_dist(player, e)

                    if gunner(e, player, 0.0, 20):
                        barr = True
                        for d in o_list:  # is there a pillar in the way
                            if d < dist:
                                barr = False
                        if barr:
                            barrage = True
                            break

                    if not turn_l and not turn_r:

                        if gunner(e, player, 45.0):
                            turn_l = True

                        if gunner(e, player, -45.0):
                            turn_r = True

                        if gunner(e, player, 90.0):
                            turn_l = True

                        if gunner(e, player, -90.0):
                            turn_r = True

                        if gunner(e, player, 135.0):
                            turn_l = True

                        if gunner(e, player, -135.0):
                            turn_r = True

                        if gunner(e, player, 180.0):
                            turn_l = True

        e_count = len(enemies)

        #t_temp, t_temp2 = self.break_traps(items, player)
        _, t_temp2 = self.break_traps(items, player)
        """
        avatar = [float(player['x_position']), float(player['y_position']),
                  float(player['angle'])]  # int(player['ammo'])]
        """
        #sensor_vec = avatar + [e_count] + targets + [0.0, 0.0] + obstacles + t_temp
        sensor_vec = [0,0,0] # currently not in use
        
        #print(len(sensor_vec))
        #exit()
        if e_temp2[2] < 80 and (player['health'] <= 40 or player['ammo'] <= 2):
            if e_temp2[2] < 90.0 and e_temp2[2] < ob_temp2[2]:
                ob_temp2 = e_temp2

        avatar2 = [float(player['x_position']), float(player['y_position']), float(player['angle']), 100, 20]
        sensor_vec2 = avatar2 + [0.0, 0.0, 0.0] + ob_temp2 + [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] + t_temp2

        return np.asarray(sensor_vec), np.asarray(
            sensor_vec2), e_count, elist, barrage, turn_l, turn_r


if __name__ == "__main__":
    agent = SotaAgent()
    agent.run()

