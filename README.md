### WSU-NG
Novelty Generator for the evaluation of novelty-aware AI agents

---
### Installation
* Requirements:
  * [docker](https://docs.docker.com/engine/install/ubuntu/)
  * [docker-compose](https://docs.docker.com/compose/install/)

---
### Quick Start
To build the sample agent:
```
docker-compose -f evaluator.yml build
```

To run the sample agent:
```
docker-compose -f evaluator.yml up
```

To stop the run midway press CTRL + C.

Confirm processes are terminated:
```
docker-compose -f evaluator.yml down
```

---
### Setting parameters

* To switch to the vizdoom agent, replace the command in sample-agent in evaluator.yml to:

`python -u SOTA-vizdoom.py --config=config/demo-vizdoom.config --printout --logfile=logs/log.txt`

* To set desired experimental parameters, modify the [sail-on] parameters in
[TA1.config](src%2Fdomains%2FWSU-Portable-Generator%2Fconfigs%2Fpartial%2FTA1.config).
  
---
### Adding a custom agent

#### Dockerized Agents
Custom agents can be easily added through the use of docker. 
If your agent is already packaged then all you need to do is modify `evaluator.yml`.

In `evaluation.yml` under `sample-agent:`:
* Set `build:`
  * `context: <dir>` where `<dir>` is your dockerfile location.
  * `dockerfile: <filename>` where `<filename>` is your dockerfile's name.
* Set ``command: <cmd>`` where `<cmd>` is your docker entry point command.

For more information on agent information see the agent [README.md](src%2Fagents%2FREADME.md).

---
### Notes
* Both the Cartpole3D and ViZDoom novelty generators startup when calling the evaluation compose file.
* By default, the base parameters are set to:
  * novelty levels = [200, 101, 102, 103, 104, 105, 106, 107, 108]
  * difficulty = [easy, medium, hard]
  * novelty_visibility = [0, 1]
  * hint_level = [-1, 0, 1, 2, 3]
* For quicker experiments, reduce the number of the base parameters.

---
### Acknowledgements
This work was supported by the DARPA SAIL-ON program under cooperative agreement number W911NF-20-2-0004.
