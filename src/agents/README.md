## Agent implementation information

Below is a list of key functions that can be used to modify and or create an agent that can interact with the 
novelty generator. 

---

## Key functions

### training_instance()

* Provides both a feature_vector and feature_label (if available).
* Expects an action label.

### train_model()

* Called when all training data has been sent.

### testing_instance()

* Provides a feature_vector and novelty_indicator.
* Expects an action label.

### save_model()

* Provides a constant filename for the experiment to be used as a save filename.
  * Runs that don't pause do not need to implement this.

### reset_model()

* Used to load from an experimental constant filename.

---

## Additional Information

More information and additional functionality can be found directly within the generator handler code. 
See [sample-cartpole.py](sample%2Fsource%2Fsample-cartpole.py).