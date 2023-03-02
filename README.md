## WSU-NG
Novelty Generator for the evaluation of novelty-aware AI agents

---
## Installation
* Requirements:
  * [docker](https://docs.docker.com/engine/install/ubuntu/)
  * [docker-compose](https://docs.docker.com/compose/install/)

---
## Quick Start
To build the sample agent:
```
docker-compose -f evaluator-[cartpole, vizdoom].yml build
```

To run the sample agent:
```
docker-compose -f evaluator-[cartpole, vizdoom].yml up
```

To stop the run midway press CTRL + C.

Confirm processes are terminated:
```
docker-compose -f evaluator-[cartpole, vizdoom].yml down
```

---
## Setting parameters

* To set desired experimental parameters, modify the [sail-on] parameters in
[TA1.config](src%2Fdomains%2FWSU-Portable-Generator%2Fconfigs%2Fpartial%2FTA1.config).

* Additional parameter variations will be made available shortly.

---
## Adding a custom agent

### Dockerized Agents
Custom agents can be easily added through the use of docker. 
If your agent is already packaged then all you need to do is modify `evaluator-[cartpole, vizdoom].yml`.

In `evaluator-[cartpole, vizdoom].yml` under `sample-agent:`:
* Set `build:`
  * `context: <dir>` where `<dir>` is your dockerfile location.
  * `dockerfile: <filename>` where `<filename>` is your dockerfile's name.
* Set ``command: <cmd>`` where `<cmd>` is your docker entry point command.

For more information on agent integration see the agent [README.md](src%2Fagents%2FREADME.md).

### Python agents

Python based agents can be easily added in. A base random action agent 
[random_action.py](src%2Fagents%2Fsample%2Fsource%2Frandom_action.py) is provided as an example starting point. 
Additional functionality can be used by directly integrating with the instance handler 
[sample-cartpole.py](src%2Fagents%2Fsample%2Fsource%2Fsample-cartpole.py)
 or 
[sample-vizdoom.py](src%2Fagents%2Fsample%2Fsource%2Fsample-vizdoom.py).


---
## Notes
* Both the Cartpole3D and ViZDoom novelty generators startup when calling the evaluation compose file.
* By default, the base parameters are set to:
  * novelty levels = [200, 101, 102, 103, 104, 105, 106, 107, 108]
  * difficulty = [easy, medium, hard]
  * novelty_visibility = [0, 1]
  * hint_level = [-1, 0, 1, 2, 3]
* For quicker experiments, reduce the number of the base parameters.
* When running the system you will see several lines of `run() Connection was closed, reconnecting...`. 
  This is normal as the subcomponents finish building out of order.


---
## Acknowledgements
This work was supported by the DARPA SAIL-ON program under cooperative agreement number W911NF-20-2-0004.
