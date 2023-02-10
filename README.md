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
## Adding a custom agent
Custom agents can be easily added 

---
## Notes
* Both the Cartpole3D and ViZDoom novelty generators startup when calling the evaluation compose file.
* 

---
### Acknowledgements
This work was supported by the DARPA SAIL-ON program under cooperative agreement number W911NF-20-2-0004.
