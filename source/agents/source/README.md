<a id="SOTA-vizdoom"></a>

# SOTA-vizdoom

<a id="SOTA-vizdoom.TA2Agent"></a>

## TA2Agent Objects

```python
class TA2Agent(TA2Logic)
```

<a id="SOTA-vizdoom.TA2Agent.experiment_start"></a>

#### experiment\_start

```python
def experiment_start()
```

This function is called when this TA2 has connected to a TA1 and is ready to begin
the experiment.

<a id="SOTA-vizdoom.TA2Agent.training_start"></a>

#### training\_start

```python
def training_start()
```

This function is called when we are about to begin training on episodes of data in
your chosen domain.

<a id="SOTA-vizdoom.TA2Agent.training_episode_start"></a>

#### training\_episode\_start

```python
def training_episode_start(episode_number: int)
```

This function is called at the start of each training episode, with the current episode
number (0-based) that you are about to begin.

Parameters
----------
episode_number : int
    This identifies the 0-based episode number you are about to begin training on.

<a id="SOTA-vizdoom.TA2Agent.training_instance"></a>

#### training\_instance

```python
def training_instance(feature_vector: dict, feature_label: dict) -> dict
```

Process a training

Parameters
----------
feature_vector : dict
    The dictionary of the feature vector.  Domain specific feature vector formats are
    defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
feature_label : dict
    The dictionary of the label for this feature vector.  Domain specific feature labels
    are defined on the github (https://github.com/holderlb/WSU-SAILON-NG). This will always
    be in the format of {'action': label}.  Some domains that do not need an 'oracle' label
    on training data will receive a valid action chosen at random.

Returns
-------
dict
    A dictionary of your label prediction of the format {'action': label}.  This is
        strictly enforced and the incorrect format will result in an exception being thrown.

<a id="SOTA-vizdoom.TA2Agent.training_performance"></a>

#### training\_performance

```python
def training_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="SOTA-vizdoom.TA2Agent.training_episode_end"></a>

#### training\_episode\_end

```python
def training_episode_end(performance: float,
                         feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the training episode and indicates that the training
episode has ended.

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

<a id="SOTA-vizdoom.TA2Agent.training_end"></a>

#### training\_end

```python
def training_end()
```

This function is called when we have completed the training episodes.

<a id="SOTA-vizdoom.TA2Agent.train_model"></a>

#### train\_model

```python
def train_model()
```

Train your model here if needed.  If you don't need to train, just leave the function
empty.  After this completes, the logic calls save_model() and reset_model() as needed
throughout the rest of the experiment.

<a id="SOTA-vizdoom.TA2Agent.save_model"></a>

#### save\_model

```python
def save_model(filename: str)
```

Saves the current model in memory to disk so it may be loaded back to memory again.

Parameters
----------
filename : str
    The filename to save the model to.

<a id="SOTA-vizdoom.TA2Agent.reset_model"></a>

#### reset\_model

```python
def reset_model(filename: str)
```

Loads the model from disk to memory.

Parameters
----------
filename : str
    The filename where the model was stored.

<a id="SOTA-vizdoom.TA2Agent.trial_start"></a>

#### trial\_start

```python
def trial_start(trial_number: int, novelty_description: dict)
```

This is called at the start of a trial with the current 0-based number.

Parameters
----------
trial_number : int
    This is the 0-based trial number in the novelty group.
novelty_description : dict
    A dictionary that will have a description of the trial's novelty.

<a id="SOTA-vizdoom.TA2Agent.testing_start"></a>

#### testing\_start

```python
def testing_start()
```

This is called after a trial has started but before we begin going through the
episodes.

<a id="SOTA-vizdoom.TA2Agent.testing_episode_start"></a>

#### testing\_episode\_start

```python
def testing_episode_start(episode_number: int)
```

This is called at the start of each testing episode in a trial, you are provided the
0-based episode number.

Parameters
----------
episode_number : int
    This is the 0-based episode number in the current trial.

<a id="SOTA-vizdoom.TA2Agent.testing_instance"></a>

#### testing\_instance

```python
def testing_instance(feature_vector: dict,
                     novelty_indicator: bool = None) -> dict
```

Evaluate a testing instance.  Returns the predicted label or action, if you believe
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

<a id="SOTA-vizdoom.TA2Agent.testing_performance"></a>

#### testing\_performance

```python
def testing_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="SOTA-vizdoom.TA2Agent.testing_episode_end"></a>

#### testing\_episode\_end

```python
def testing_episode_end(performance: float,
                        feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the testing episode.

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

<a id="SOTA-vizdoom.TA2Agent.testing_end"></a>

#### testing\_end

```python
def testing_end()
```

This is called after the last episode of a trial has completed, before trial_end().

<a id="SOTA-vizdoom.TA2Agent.trial_end"></a>

#### trial\_end

```python
def trial_end()
```

This is called at the end of each trial.

<a id="SOTA-vizdoom.TA2Agent.experiment_end"></a>

#### experiment\_end

```python
def experiment_end()
```

This is called when the experiment is done.

<a id="SOTA-cartpole"></a>

# SOTA-cartpole

<a id="SOTA-cartpole.TA2Agent"></a>

## TA2Agent Objects

```python
class TA2Agent(TA2Logic)
```

<a id="SOTA-cartpole.TA2Agent.experiment_start"></a>

#### experiment\_start

```python
def experiment_start()
```

This function is called when this TA2 has connected to a TA1 and is ready to begin
the experiment.

<a id="SOTA-cartpole.TA2Agent.training_start"></a>

#### training\_start

```python
def training_start()
```

This function is called when we are about to begin training on episodes of data in
your chosen domain.

<a id="SOTA-cartpole.TA2Agent.training_episode_start"></a>

#### training\_episode\_start

```python
def training_episode_start(episode_number: int)
```

This function is called at the start of each training episode, with the current episode
number (0-based) that you are about to begin.

Parameters
----------
episode_number : int
    This identifies the 0-based episode number you are about to begin training on.

<a id="SOTA-cartpole.TA2Agent.training_instance"></a>

#### training\_instance

```python
def training_instance(feature_vector: dict, feature_label: dict) -> dict
```

Process a training

Parameters
----------
feature_vector : dict
    The dictionary of the feature vector.  Domain specific feature vector formats are
    defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
feature_label : dict
    The dictionary of the label for this feature vector.  Domain specific feature labels
    are defined on the github (https://github.com/holderlb/WSU-SAILON-NG). This will always
    be in the format of {'action': label}.  Some domains that do not need an 'oracle' label
    on training data will receive a valid action chosen at random.

Returns
-------
dict
    A dictionary of your label prediction of the format {'action': label}.  This is
        strictly enforced and the incorrect format will result in an exception being thrown.

<a id="SOTA-cartpole.TA2Agent.training_performance"></a>

#### training\_performance

```python
def training_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="SOTA-cartpole.TA2Agent.training_episode_end"></a>

#### training\_episode\_end

```python
def training_episode_end(performance: float,
                         feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the training episode and indicates that the training
episode has ended.

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

<a id="SOTA-cartpole.TA2Agent.training_end"></a>

#### training\_end

```python
def training_end()
```

This function is called when we have completed the training episodes.

<a id="SOTA-cartpole.TA2Agent.train_model"></a>

#### train\_model

```python
def train_model()
```

Train your model here if needed.  If you don't need to train, just leave the function
empty.  After this completes, the logic calls save_model() and reset_model() as needed
throughout the rest of the experiment.

<a id="SOTA-cartpole.TA2Agent.save_model"></a>

#### save\_model

```python
def save_model(filename: str)
```

Saves the current model in memory to disk so it may be loaded back to memory again.

Parameters
----------
filename : str
    The filename to save the model to.

<a id="SOTA-cartpole.TA2Agent.reset_model"></a>

#### reset\_model

```python
def reset_model(filename: str)
```

Loads the model from disk to memory.

Parameters
----------
filename : str
    The filename where the model was stored.

<a id="SOTA-cartpole.TA2Agent.trial_start"></a>

#### trial\_start

```python
def trial_start(trial_number: int, novelty_description: dict)
```

This is called at the start of a trial with the current 0-based number.

Parameters
----------
trial_number : int
    This is the 0-based trial number in the novelty group.
novelty_description : dict
    A dictionary that will have a description of the trial's novelty.

<a id="SOTA-cartpole.TA2Agent.testing_start"></a>

#### testing\_start

```python
def testing_start()
```

This is called after a trial has started but before we begin going through the
episodes.

<a id="SOTA-cartpole.TA2Agent.testing_episode_start"></a>

#### testing\_episode\_start

```python
def testing_episode_start(episode_number: int)
```

This is called at the start of each testing episode in a trial, you are provided the
0-based episode number.

Parameters
----------
episode_number : int
    This is the 0-based episode number in the current trial.

<a id="SOTA-cartpole.TA2Agent.testing_instance"></a>

#### testing\_instance

```python
def testing_instance(feature_vector: dict,
                     novelty_indicator: bool = None) -> dict
```

Evaluate a testing instance.  Returns the predicted label or action, if you believe
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

<a id="SOTA-cartpole.TA2Agent.testing_performance"></a>

#### testing\_performance

```python
def testing_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="SOTA-cartpole.TA2Agent.testing_episode_end"></a>

#### testing\_episode\_end

```python
def testing_episode_end(performance: float,
                        feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the testing episode.

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

<a id="SOTA-cartpole.TA2Agent.testing_end"></a>

#### testing\_end

```python
def testing_end()
```

This is called after the last episode of a trial has completed, before trial_end().

<a id="SOTA-cartpole.TA2Agent.trial_end"></a>

#### trial\_end

```python
def trial_end()
```

This is called at the end of each trial.

<a id="SOTA-cartpole.TA2Agent.experiment_end"></a>

#### experiment\_end

```python
def experiment_end()
```

This is called when the experiment is done.

<a id="objects"></a>

# objects

<a id="objects.objects"></a>

# objects.objects

<a id="objects.objects.CasasDatetimeException"></a>

## CasasDatetimeException Objects

```python
class CasasDatetimeException(Exception)
```

A custom exception to help enforce the use of timezones in datetime objects across CASAS.

Attributes
----------
value : str
    The description of the error situation.

<a id="objects.objects.CasasDatetimeException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value)
```

Initialize a CasasDatetimeException object.

Parameters
----------
value : str
    The description of the error situation.

<a id="objects.objects.CasasDatetimeException.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Get a string of the exception.

Returns
-------
str
    A description of the error situation.

<a id="objects.objects.CasasRabbitMQException"></a>

## CasasRabbitMQException Objects

```python
class CasasRabbitMQException(Exception)
```

A custom exception to help enforce the use of the consuming state versus some of the RPC
methods in the casas.rabbitmq.Connection class.

Attributes
----------
value : str
    The description of the error situation.

<a id="objects.objects.CasasRabbitMQException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value)
```

Initialize a CasasRabbitMQException object.

Parameters
----------
value : str
    The description of the error situation.

<a id="objects.objects.CasasRabbitMQException.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Get a string of the exception.

Returns
-------
str
    A description of the error situation.

<a id="objects.objects.AiqDataException"></a>

## AiqDataException Objects

```python
class AiqDataException(Exception)
```

A custom exception to help enforce the standardization of our data types.

Attributes
----------
value : str
    The description of the error situation.

<a id="objects.objects.AiqDataException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value)
```

Initialize a AiqDataException object.

Parameters
----------
value : str
    The description of the error situation.

<a id="objects.objects.AiqDataException.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Get a string of the exception.

Returns
-------
str
    A description of the error situation.

<a id="objects.objects.AiqExperimentException"></a>

## AiqExperimentException Objects

```python
class AiqExperimentException(Exception)
```

A custom exception to help signal that there was an error in the experiment.

Attributes
----------
value : str
    The description of the error situation.

<a id="objects.objects.AiqExperimentException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value)
```

Initialize a AiqExperimentException object.

Parameters
----------
value : str
    The description of the error situation.

<a id="objects.objects.AiqExperimentException.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Get a string of the exception.

Returns
-------
str
    A description of the error situation.

<a id="objects.objects.CasasObject"></a>

## CasasObject Objects

```python
class CasasObject(object)
```

The base class for all of the CASAS objects.

Attributes
----------
action : str
    The defined action value for json.
target : str
    The target for this object.
serial : str
    The serial for this object.
sensor_1 : str
    The translated primary sensor name.
sensor_2 : str
    The translated secondary sensor name.
sensor_type : str
    The sensor type for this object.
package_type : str
    The package type for this object.
site : str
    The site this object is associated with.
epoch : float
    A float representation of the Unix epoch for this object.
stamp : datetime.datetime
    The UTC datetime.datetime object for the value in epoch.
stamp_local : datetime.datetime
    The site local datetime.datetime object for the value in epoch.
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

<a id="objects.objects.CasasObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initialize a new CasasObject object.

<a id="objects.objects.CasasObject.localize_stamp"></a>

#### localize\_stamp

```python
def localize_stamp(timezone=pytz.timezone('America/Los_Angeles'))
```

Converts the UTC stamp into local stamp.

Parameters
----------
timezone : pytz.timezone
    The timezone to localize stamp into (default = America/Los_Angeles).

<a id="objects.objects.CasasObject.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing this object.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str

<a id="objects.objects.CasasObject.get_detailed_json"></a>

#### get\_detailed\_json

```python
def get_detailed_json(secret=None, key=None)
```

Returns a JSON string representing this object with additional fields.

If classes that inherit from this class do not implement this function, the inherited
behavior is that this function will return the result of self.get_json(secret, key).

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str

<a id="objects.objects.CasasError"></a>

## CasasError Objects

```python
class CasasError(CasasObject)
```

This class represents an instance of a `CasasError`, which is part of a `CasasResponse`.

Attributes
----------
action : str
    The defined action for the json, this object is 'casas_error'.
error_type : str
    The type of the error.
message : str
    A brief description fo the error.
error_dict : dict
    An optional dict of additional information about the error.

<a id="objects.objects.CasasError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(error_type, message, error_dict=None)
```

Initialize a new CasasError object.

Parameters
----------
error_type : str
    The type of the error.
message : str
    A brief description of the error.
error_dict : dict, optional
    An optional dict of additional information about the error.

<a id="objects.objects.CasasError.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CasasError.

Parameters
----------
secret : str, optional
    The secret in the key:secret, not used here.
key : str, optional
    The key in the key:secret, not used here.

Returns
-------
str
    A JSON string representing the CasasError.

<a id="objects.objects.CasasResponse"></a>

## CasasResponse Objects

```python
class CasasResponse(CasasObject)
```

This class represents an instance of a `CasasResponse`, which is used with RPC calls.

Attributes
----------
action : str
    The defined action for the json, this object is 'casas_response'.
status : str
    The status of the response.
response_type : str
    The type of the response message.
error_message : str
    An optional general error message for the response.
error_list : list
    Optional list of `CasasError` objects.

<a id="objects.objects.CasasResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(status='success',
             response_type='data',
             error_message='No Errors',
             error_list=None)
```

Initialize a new CasasResponse object.

Parameters
----------
status : str, optional
    Define the status of the response.
response_type : str, optional
    Define the type of the response message.
error_message : str, optional
    Optional general error message for the response.
error_list : list, optional
    Optional list of errors.

<a id="objects.objects.CasasResponse.add_error"></a>

#### add\_error

```python
def add_error(casas_error, error_type=None)
```

Add a CasasError object to the CasasResponse.

Parameters
----------
casas_error : CasasError
    An error to add to the CasasResponse.
error_type : str, optional
    An optional error type to set the response_type for this object.

<a id="objects.objects.CasasResponse.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CasasResponse.

Parameters
----------
secret : str, optional
    The secret in the key:secret, not used here.
key : str, optional
    The key in the key:secret, not used here.

Returns
-------
str
    A JSON string representing the CasasResponse.

<a id="objects.objects.CasasObjectList"></a>

## CasasObjectList Objects

```python
class CasasObjectList(CasasObject)
```

This class represents a list of one or more CasasObjects.

<a id="objects.objects.CasasObjectList.__init__"></a>

#### \_\_init\_\_

```python
def __init__(object_list=None)
```

Initialize a new CasasObjectList object.

Parameters
----------
object_list : list, optional
    A list of CasasObject that you wish to handle together.

<a id="objects.objects.CasasObjectList.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a newline delimited string of the objects in the self.object_list.

Returns
-------
str
    A newline delimited string of the objects in the self.object_list.

<a id="objects.objects.CasasObjectList.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CasasObjectList.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the CasasObjectList.

<a id="objects.objects.CasasObjectList.get_detailed_json"></a>

#### get\_detailed\_json

```python
def get_detailed_json(secret=None, key=None)
```

Returns a JSON string representing the CasasObjectList with additional fields.

This function primarily calls the detailed JSON functions of it's contained objects.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret requi9red for uploading data.

Returns
-------
str
    A JSON string representing the CasasObjectList

<a id="objects.objects.CasasGetObject"></a>

## CasasGetObject Objects

```python
class CasasGetObject(CasasObject)
```

This class represents an authenticated wrapper around a request for an object.

Attributes
----------
action : str
    The defined action for the json, this object is 'casas_get_object'.
casas_object : CasasObject
    The CasasObject that we want to request.
key : str
    The key value that is paired with secret for authorizing access to the requested object.
secret : str
    The secret value that is paired with key for authorizing access to the requested object.
site : str
    The testbed that is associated with the key and secret.

<a id="objects.objects.CasasGetObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__(casas_object, key, secret, site)
```

Initialize a new CasasGetObject object.

Parameters
----------
casas_object : CasasObject
    The CasasObject that we want to request.
key : str
    The key value that is paired with secret for authorizing access to the requested object.
secret : str
    The secret value that is paired with key for authorizing access to the requested object.
site : str
    The testbed that is associated with the key and secret.

<a id="objects.objects.CasasGetObject.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CasasGetObject.

Parameters
----------
secret : str, optional
    This value is not used, we use the class object instead.
key : str, optional
    This value is not used, we use the class object instead.

Returns
-------
str
    A JSON string representing the CasasGetObject.

<a id="objects.objects.CasasSetObject"></a>

## CasasSetObject Objects

```python
class CasasSetObject(CasasObject)
```

This class represents an authenticated wrapper around a request to set or update an object.

Attributes
----------
action : str
    The defined action for the json, this object is 'casas_set_object'.
casas_object : CasasObject
    The CasasObject that we want to request be set or updated.
key : str
    The key value that is paired with secret for authorizing access to set or update the
    requested changes to the provided object.
secret : str
    The secret value that is paired with key for authorizing access to set or update the
    requested changes to the provided object.
site : str
    The testbed that is associated with the key and secret.

<a id="objects.objects.CasasSetObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__(casas_object, key, secret, site)
```

Initialize a new CasasSetObject object.

Parameters
----------
casas_object : CasasObject
    The CasasObject that we want to set or update.
key : str
    The key value that is paired with secret for authorizing access to set or update the
    requested changes to the provided object.
secret : str
    The secret value that is paired with key for authorizing access to set or update the
    requested changes to the provided object.
site : str
    The testbed that is associated with the key and secret.

<a id="objects.objects.CasasSetObject.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CasasSetObject.

Parameters
----------
secret : str, optional
    This value is not used, we use the class object instead.
key : str, optional
    This value is not used, we use the class object instead.

Returns
-------
str
    A JSON string representing the CasasSetObject.

<a id="objects.objects.Testbed"></a>

## Testbed Objects

```python
class Testbed(CasasObject)
```

This class represents an instance of a Testbed.

Attributes
----------
action : str
    The defined action for the json, this object is 'testbed'.
site : str
    The name of the Testbed.
description : str
    An optional description of the testbed.
active : boolean
    A flag to identify if this site is active.
created_on : datetime.datetime
    A UTC timestamp of when this site was created.
created_on_epoch : float
    The UNIX epoch of the `created_on` datetime.datetime.
has_internet : boolean
    A flag to identify if this site has an internet connection.
timezone : str
    The full time zone name for this site.
last_seen : datetime.datetime
    The UTC timestamp of when this site was last seen.
last_seen_epoch : float
    The UNIX epoch of the `last_seen` datetime.datetime.
first_event : datetime.datetime
    The UTC timestamp of the first event recorded for this site.
first_event_epoch : float
    The UNIX epoch of the `first_event` datetime.datetime.
latest_event : datetime.datetime
    The UTC timestamp of the most recent event recorded for this site.
latest_event_epoch : float
    The UNIX epoch of the `latest_event` datetime.datetime.

<a id="objects.objects.Testbed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site,
             description=None,
             active=False,
             created_on=None,
             has_internet=False,
             timezone='America/Los_Angeles',
             last_seen=None,
             first_event=None,
             latest_event=None)
```

Initialize a new Testbed object.

Parameters
----------
site : str
    The name of the Testbed.
description : str, optional
    An optional description of the testbed.
active : boolean, optional
    A flag to identify if this site is active.
created_on : datetime.datetime, optional
    A UTC timestamp of when this site was created.
has_internet : boolean, optional
    A flag to identify if this site has an internet connection.
timezone : str, optional
    The full time zone name for this site.
last_seen : datetime.datetime, optional
    The UTC timestamp of when this site was last seen.
first_event : datetime.datetime, optional
    The UTC timestamp of the first event recorded for this site.
latest_event : datetime.datetime, optional
    The UTC timestamp of the most recent event recorded for this site.

Raises
------
CasasDatetimeException
    If `created_on`, `last_seen`, `first_event`, or `latest_event` is a naive
    datetime.datetime object, where the tzinfo is not set.

<a id="objects.objects.Testbed.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Algorithm fields.

Returns
-------
str
    A tab delimited string of the Algorithm fields.

<a id="objects.objects.Testbed.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Testbed.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the Testbed.

Raises
------
CasasDatetimeException
    If `created_on`, `last_seen`, `first_event`, or `latest_event` is a naive
    datetime.datetime object, where the tzinfo is not set.

<a id="objects.objects.Event"></a>

## Event Objects

```python
class Event(CasasObject)
```

Represents an Event object that gets passed around.

This is a standard Event JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "event",
     "data": {"uuid": "",
              "epoch": "",
              "serial": "",
              "target": "",
              "message": "",
              "by": "",
              "category": "",
              "sensor_type": "",
              "package_type": ""
              }
    }

This is a detailed Event JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "event",
     "data": {"uuid": "",
              "epoch": "",
              "stamp": "",
              "stamp_local": "",
              "sensor_1": "",
              "sensor_2": "",
              "serial": "",
              "target": "",
              "message": "",
              "by": "",
              "category": "",
              "sensor_type": "",
              "package_type": ""
              }
    }



Attributes
----------
action : str
    The defined action for the json, this object is 'event'.
by : str
    The name of the agent that created this event.
category : str
    Identifies the category of the event.
channel : str
    The channel that this event was published to.
epoch : float
    A float representing the UTC epoch for when the event occurred.
event_id : str
    An optional value representing this event's event_id in the database.
message : str
    The core message of the event.
package_type : str
    Defines the package type of the event.
sensor_1 : str
    An optional translation value for this sensor target.
sensor_2 : str
    An optional translation value for this sensor target.
sensor_type : str
    Defines the sensor type of the event.
serial : str
    The serial identification of the target.
site : str
    The name of the testbed where this event was created.
stamp : datetime.datetime
    The UTC datetime.datetime object for when the event occurred.
stamp_local : datetime.datetime
    The local datetime.datetime object when the event occurred.
target : str
    The target generating the event.
uuid : str
    A UUID string identifying this event.

<a id="objects.objects.Event.__init__"></a>

#### \_\_init\_\_

```python
def __init__(category,
             package_type,
             sensor_type,
             message,
             target,
             serial,
             by,
             channel,
             site,
             epoch=None,
             uuid=None,
             sensor_1=None,
             sensor_2=None,
             event_id=None,
             stamp=None,
             stamp_local=None,
             request_id=None,
             request_size=None)
```

Initialize a new Event object.

Parameters
----------
category : str
    Identifies the category of the event.
package_type : str
    Defines the package type of the event.
sensor_type : str
    Defines the sensor type of the event.
message : str
    The core message of the event.
target : str
    The target generating the event.
serial : str
    The serial identification of the target.
by : str
    The name of the agent that created this event.
channel : str
    The channel that this event was published to.
site : str
    The name of the testbed where this event was created.
epoch : float
    A float representing the UTC epoch for when the event occurred.
uuid : str, optional
    A UUID string identifying this event.
sensor_1 : str, optional
    An optional translation value for this sensor target.
sensor_2 : str, optional
    An optional translation value for this sensor target.
event_id : str, optional
    An optional value representing this event's event_id in the database.
stamp : datetime.datetime, optional
    The UTC datetime.datetime object for when the event occurred.
stamp_local : datetime.datetime, optional
    The local datetime.datetime object when the event occurred.

Raises
------
CasasDatetimeException
    If `stamp` or `stamp_local` is a naive datetime.datetime object, where the tzinfo is
    not set.

<a id="objects.objects.Event.validate_event"></a>

#### validate\_event

```python
def validate_event()
```

Validates the event object, and converts the epoch into a UTC stamp.

<a id="objects.objects.Event.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Event fields.

Returns
-------
str
    A tab delimited string of the Event fields.

<a id="objects.objects.Event.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Event.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Event.

<a id="objects.objects.Event.get_detailed_json"></a>

#### get\_detailed\_json

```python
def get_detailed_json(secret=None, key=None)
```

Returns a JSON string representing the Event with additional fields.

This function adds additional optional fields into the JSON object that it returns.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Event.

<a id="objects.objects.Event.tag"></a>

#### tag

```python
def tag(created_by=None,
        label=None,
        value=None,
        dataset=None,
        experiment=None)
```

Returns a Tag object built from this Event and the provided parameters.

Parameters
----------
created_by : str
    A string depicting who/what created the tag being put on this event.
label : str
    The label being tagged on this event.
value : str
    An optional value for the tagged event.
dataset : str
    The name of the dataset this tag is part of.
experiment : str
    The name of the experiment this tag is part of.

Returns
-------
Tag
    A new Tag object representing the tagged event.

Raises
------
ValueError
    Tag.dataset must have an actual value!
ValueError
    Tag.experiment must have an actual value!

<a id="objects.objects.Tag"></a>

## Tag Objects

```python
class Tag(Event)
```

Represents a Tag object that gets passed around.

This is a standard Tag JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "tag",
     "data": {"tag": {"created_by": "",
                      "label": {"name": "",
                                "value": ""
                               },
                      "dataset": "",
                      "experiment": ""
                      },
              "uuid": "",
              "epoch": "",
              "serial": "",
              "target": "",
              "message": "",
              "by": "",
              "category": "",
              "sensor_type": "",
              "package_type": ""
              }
    }

This is a detailed Tag JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "tag",
     "data": {"tag": {"created_by": "",
                      "label": {"name": "",
                                "value":""
                                },
                      "dataset": "",
                      "experiment": ""
                      },
              "uuid": "",
              "epoch": "",
              "stamp": "",
              "stamp_local": "",
              "sensor_1": "",
              "sensor_2": "",
              "serial": "",
              "target": "",
              "message": "",
              "by": "",
              "category": "",
              "sensor_type": "",
              "package_type": ""
              }
    }

Attributes
----------
action : str
    The defined action for the json, this object is 'tag'.
by : str
    The name of the agent that created this event.
category : str
    Identifies the category of the event.
channel : str
    The channel that this event was published to.
created_by : str
    A string depicting who/what created the tag being put on this event.
dataset : str
    The name of the dataset this tag is part of.
epoch : float
    A float representing the UTC epoch for when the event occurred.
event_id : str
    An optional value representing this event's event_id in the database.
experiment : str
    The name of the experiment this tag is part of.
label : str
    The label being tagged on this event.
message : str
    The core message of the event.
package_type : str
    Defines the package type of the event.
sensor_1 : str
    An optional translation value for this sensor target.
sensor_2 : str
    An optional translation value for this sensor target.
sensor_type : str
    Defines the sensor type of the event.
serial : str
    The serial identification of the target.
site : str
    The name of the testbed where this event was created.
stamp : datetime.datetime
    The UTC datetime.datetime object for when the event occurred.
stamp_local : datetime.datetime
    The local datetime.datetime object when the event occurred.
target : str
    The target generating the event.
uuid : str
    A UUID string identifying this event.
value : str
    An optional value for the tagged event.

<a id="objects.objects.Tag.__init__"></a>

#### \_\_init\_\_

```python
def __init__(category,
             package_type,
             sensor_type,
             message,
             target,
             serial,
             by,
             channel,
             site,
             epoch,
             uuid,
             created_by,
             label,
             value,
             dataset,
             experiment,
             sensor_1=None,
             sensor_2=None,
             event_id=None,
             stamp=None,
             stamp_local=None,
             request_id=None,
             request_size=None)
```

Initialize a new Tag object.

Parameters
----------
category : str
    Identifies the category of the event.
package_type : str
    Defines the package type of the event.
sensor_type : str
    Defines the sensor type of the event.
message : str
    The core message of the event.
target : str
    The target generating the event.
serial : str
    The serial identification of the target.
by : str
    The name of the agent that created this event.
channel : str
    The channel that this event was published to.
site : str
    The name of the testbed where this event was created.
epoch : float
    A float representing the UTC epoch for when the event occurred.
uuid : str
    A UUID string identifying this event.
created_by : str
    A string depicting who/what created the tag being put on this event.
label : str
    The label being tagged on this event.
value : str
    An optional value for the tagged event.
dataset : str
    The name of the dataset this tag is part of.
experiment : str
    The name of the experiment this tag is part of.
sensor_1 : str
    An optional translation value for this sensor target.
sensor_2 : str
    An optional translation value for this sensor target.
event_id : str
    An optional value representing this event's event_id in the database.
stamp : datetime.datetime, optional
    The UTC datetime.datetime object for when the event occurred.
stamp_local : datetime.datetime, optional
    The local datetime.datetime object when the event occurred.

Raises
------
CasasDatetimeException
    If `stamp` or `stamp_local` is a naive datetime.datetime object, where the tzinfo is
    not set.

<a id="objects.objects.Tag.validate_tag"></a>

#### validate\_tag

```python
def validate_tag()
```

Validates the Tag attributes.

Raises
------
ValueError
    If Tag.dataset is not defined or is an empty string.
ValueError
    If Tag.experiment is not defined or is an empty string.

<a id="objects.objects.Tag.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Tag fields.

Returns
-------
str
    A tab delimited string of the Tag fields.

<a id="objects.objects.Tag.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Tag.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Tag.

<a id="objects.objects.Tag.get_detailed_json"></a>

#### get\_detailed\_json

```python
def get_detailed_json(secret=None, key=None)
```

Returns a JSON string representing the Tag with additional fields.

This function adds additional optional fields into the JSON object that it returns.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Tag.

<a id="objects.objects.Control"></a>

## Control Objects

```python
class Control(CasasObject)
```

Represents a Control object that gets passed around.

This is a standard Control JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "control",
     "data": {"uuid": "",
              "epoch": "",
              "serial": "",
              "target": "",
              "command": "",
              "value": "",
              "replyto": "",
              "cid": "",
              "by": "",
              "category": ""
              }
    }

This is a Control JSON message converted to Event.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "event",
     "data": {"uuid": "",
              "epoch": "",
              "serial": "",
              "target": "",
              "message": "{'command':'','value':'','cid':'','replyto':'','response':''}",
              "by": "",
              "category": "control",
              "sensor_type": "control",
              "package_type": "control"
              }
    }

This is a detailed Control JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "control",
     "data": {"uuid": "",
              "epoch": "",
              "stamp": "",
              "stamp_local": "",
              "sensor_1": "",
              "sensor_2": "",
              "serial": "",
              "target": "",
              "command": "",
              "value": "",
              "replyto": "",
              "cid": "",
              "by": "",
              "category": "",
              "sensor_type": "",
              "package_type": ""
              }
    }

Attributes
----------
action : str
    The defined action for the json, this object is 'control'.
by : str
    The name of the agent that created this command.
category : str
    Identifies the category of the control command.
channel : str
    The channel that this command was published to.
cid : str, optional
    An optional value for keeping track of a control command.
command : str
    The command message being sent.
epoch : float
    A float representing the UTC epoch for when the command occurred.
event_id : str
    An optional value representing this command's event_id in the database.
message : str
    The core message of the command.
package_type : str
    Defines the package type of the command.
replyto : str, optional
    An optional value of an agent ID to reply to after completing the command.
response: str, optional
    The response (if any) from executing the control command.
sensor_1 : str
    An optional translation value for this sensor target.
sensor_2 : str
    An optional translation value for this sensor target.
sensor_type : str
    Defines the sensor type of the command.
serial : str
    The serial identification of the target.
site : str
    The name of the testbed where this command was created.
stamp : datetime.datetime
    The UTC datetime.datetime object for when the command occurred.
stamp_local : datetime.datetime
    The local datetime.datetime object when the command occurred.
target : str
    The target to execute the command.
uuid : str
    A UUID string identifying this event/command.
value : str
    An optional value field being sent with the control command.

<a id="objects.objects.Control.__init__"></a>

#### \_\_init\_\_

```python
def __init__(category,
             target,
             serial,
             by,
             channel,
             site,
             command,
             value,
             replyto,
             cid,
             response=None,
             package_type="control",
             sensor_type="control",
             message=None,
             epoch=None,
             uuid=None,
             sensor_1=None,
             sensor_2=None,
             event_id=None,
             stamp=None,
             stamp_local=None)
```

Initialize a new Control object.

Parameters
----------
category : str
    Identifies the category of the control command.
target : str
    The target to execute the command.
serial : str
    The serial identification of the target.
by : str
    The name of the agent that created this command.
channel : str
    The channel that this command was published to.
site : str
    The name of the testbed where this command was created.
command : str
    The command message being sent.
value : str
    An optional value field being sent with the control command.
replyto : str, optional
    An optional value of an agent ID to reply to after completing the command.
cid : str, optional
    An optional value for keeping track of a control command.
response: str, optional
    The response (if any) from executing the control command.
package_type : str
    Defines the package type of the command.
sensor_type : str
    Defines the sensor type of the command.
message : str
    The core message of the command.
epoch : float
    A float representing the UTC epoch for when the command occurred.
uuid : str
    A UUID string identifying this event/command.
sensor_1 : str
    An optional translation value for this sensor target.
sensor_2 : str
    An optional translation value for this sensor target.
event_id : str
    An optional value representing this command's event_id in the database.
stamp : datetime.datetime, optional
    The UTC datetime.datetime object for when the command occurred.
stamp_local : datetime.datetime, optional
    The local datetime.datetime object when the command occurred.

Raises
------
CasasDatetimeException
    If `stamp` or `stamp_local` is a naive datetime.datetime object, where the tzinfo is
    not set.

<a id="objects.objects.Control.validate_control"></a>

#### validate\_control

```python
def validate_control()
```

Validates the new Control object and converts the epoch.

<a id="objects.objects.Control.get_as_event_obj"></a>

#### get\_as\_event\_obj

```python
def get_as_event_obj()
```

Returns an Event object representation of the Control object.

Returns
-------
Event
    An Event object representation of this Control object.
    All Control objects are stored in the database as Event objects.

<a id="objects.objects.Control.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Control fields.

Returns
-------
str
    A tab delimited string of the Control fields.

<a id="objects.objects.Control.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Control.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Control.

<a id="objects.objects.Control.get_detailed_json"></a>

#### get\_detailed\_json

```python
def get_detailed_json(secret=None, key=None)
```

Returns a JSON string representing the Control with additional fields.

This function adds additional optional fields into the JSON object that it returns.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Control.

<a id="objects.objects.Control.tag"></a>

#### tag

```python
def tag(created_by=None,
        label=None,
        value=None,
        dataset=None,
        experiment=None)
```

Returns a Tag object built from this Control command and the provided parameters.

Parameters
----------
created_by : str
    A string depicting who/what created the tag being put on this Control command.
label : str, optional
    The label being tagged on this Control command.
value : str, optional
    An optional value for the tagged Control command.
dataset : str
    The name of the dataset this tag is part of.
experiment : str
    The name of the experiment this tag is part of.

Returns
-------
Tag
    A new Tag object representing the tagged Control command.

Raises
------
ValueError
    Tag.dataset must have an actual value!
ValueError
    Tag.experiment must have an actual value!

<a id="objects.objects.Heartbeat"></a>

## Heartbeat Objects

```python
class Heartbeat(CasasObject)
```

Represents a Heartbeat object that gets passed around.

This is a standard Heartbeat JSON message.

.. code-block:: JSON
    :emphasize-lines: 5

    {"channel": "",
     "site": "",
     "secret": "",
     "key": "",
     "action": "heartbeat",
     "data": {"epoch": ""
              }
    }

Attributes
----------
action : str
    The defined action for the json, this object is 'heartbeat'.
channel : str
    The channel that this heartbeat was published to.
site : str
    The name of the testbed where this heartbeat was created.
epoch : float
    A float representing the UTC epoch for when the heartbeat arrived.
stamp : datetime.datetime
    The UTC datetime.datetime object for when the heartbeat arrived.
stamp_local : datetime.datetime
    The local datetime.datetime object for when the heartbeat arrived.

<a id="objects.objects.Heartbeat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site, epoch=None, stamp=None, stamp_local=None)
```

Initialize a new Heartbeat object.

Parameters
----------
site : str
    The name of the testbed where this heartbeat was created.
epoch : float
    A float representing the UTC epoch for when the heartbeat arrived.
stamp : datetime.datetime
    The UTC datetime.datetime object for when the heartbeat arrived.
stamp_local : datetime.datetime
    The local datetime.datetime object for when the heartbeat arrived.

Raises
------
CasasDatetimeException
    If `stamp` or `stamp_local` is a naive datetime.datetime object, where the tzinfo is
    not set.

<a id="objects.objects.Heartbeat.validate_heartbeat"></a>

#### validate\_heartbeat

```python
def validate_heartbeat()
```

Validates the Heartbeat object, and converts the epoch into a UTC stamp.

<a id="objects.objects.Heartbeat.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Heartbeat fields.

Returns
-------
str
    A tab delimited string of the Heartbeat fields.

<a id="objects.objects.Heartbeat.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Heartbeat.

Parameters
----------
secret : str
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
key : str
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.

Returns
-------
str
    A JSON string representing the Heartbeat.

<a id="objects.objects.Translation"></a>

## Translation Objects

```python
class Translation(CasasObject)
```

This represents the translation of a target for a site, with an optional valid time range.

This is a standard Translation JSON message.

.. code-block:: JSON
    :emphasize-lines: 2

    {"site": "",
     "action": "translation",
     "data": {"target": "",
              "sensor_1": "",
              "sensor_2": "",
              "start_epoch": "",
              "end_epoch": ""
              }
    }

Attributes
----------
action : str
    The defined action for the json, this object is 'translation'.
target : str
    The sensor name for this translation.
site : str
    The testbed that this target translation is valid for.
sensor_1 : str
    The primary translation value for this target.
sensor_2 : str
    The secondary translation value for this target.
start_epoch : float
    The UTC epoch for the start of the valid range. If this is None, then the translation is
    valid from the entire start of events for this site until the end value.
start_stamp : datetime.datetime
    The UTC datetime.datetime object of the valid range.
end_epoch : float
    The UTC epoch for the end of the valid range. If this is None, then the translation is
    valid from the start value onwards (through current live data).
end_stamp : datetime.datetime
    The UTC datetime.datetime object of the valid range.

<a id="objects.objects.Translation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site,
             target,
             sensor_1,
             sensor_2,
             start_epoch=None,
             end_epoch=None)
```

Initialize a new Translation object.

Parameters
----------
site : str
    The testbed that this target translation is valid for.
target : str
    The sensor name for this translation.
sensor_1 : str
    The primary translation value for this target.
sensor_2 : str
    The secondary translation value for this target.
start_epoch : float, optional
    The UTC epoch for the start of the valid range. If this is None, then the translation is
    valid from the entire start of events for this site until the end value.
end_epoch : float, optional
    The UTC epoch for the end of the valid range. If this is None, then the translation is
    valid from the start value onwards (through current live data).

<a id="objects.objects.Translation.validate_translation"></a>

#### validate\_translation

```python
def validate_translation()
```

Validates the translation object and converts the epochs into UTC stamps.

<a id="objects.objects.Translation.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Translation fields.

Returns
-------
str
    A tab delimited string of the Translation fields.

<a id="objects.objects.Translation.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Translation.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the Translation.

<a id="objects.objects.TranslationGroup"></a>

## TranslationGroup Objects

```python
class TranslationGroup(CasasObject)
```

This class represents a translate file, which contains many Translation entries for a
single site.

Attributes
----------
action : str
    The defined action for the json, this object is 'translation_group'.
site : str
    The testbed that this TranslationGroup is valid for.
group_name : str
    The name or filename of this group.
translations : list(Translation)
    A list of the Translation objects that make up this TranslationGroup.
t_dict : dict({'target':list(Translation)}
    A dictionary where the keys are the targets, and the values are lists of Translation
    objects. This allows for quick lookups and validation when targets have different
    Translation objects across multiple times.

<a id="objects.objects.TranslationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site, group_name, translations=None)
```

Initialize a new TranslationGroup object.

Parameters
----------
site : str
    The testbed that this translation is valid for.
group_name : str
    The name (or filename) of this translation group.
translations : list, optional
    A list of translations that this group contains.

<a id="objects.objects.TranslationGroup.build_translation_structure"></a>

#### build\_translation\_structure

```python
def build_translation_structure()
```

Builds a dictionary->list structure for quick checking if a target has multiple
translations available.

<a id="objects.objects.TranslationGroup.validate_translation_group"></a>

#### validate\_translation\_group

```python
def validate_translation_group()
```

Validates the TranslationGroup Translation objects for the targets.

A valid translation for a single target must fall within a couple variations such that
there are no possible windows of time where the target does not have a translation value.

* Single translation

    * Both the start and stop values *MUST* be empty, as this single translation value
      has to cover *ALL* possible times (past/present/future) that the target could
      have/might be observed.

* Multiple translations

    * **The first translation**.  When sorted by temporal order, the start stamp of the
      first translation object *MUST* have a blank value, which means that there is no
      start limit to what this translation covers.

    * **All middle translations**.  For all translations objects where the start stamp is
      not empty, the start stamp of translation `i` must match the end stamp of
      translation `i-1`.

    * **All middle translations**.  For all translations objects where the end stamp is
      not empty, the end stamp of translation `i` must match the start stamp of
      translation `i+1`.

    * **The last translation**.  When sorted by temporal order, the end stamp of the
      last translation object *MUST* have a blank value, which means that there is no
      end limit to what this translation covers.


Raises
------
ValueError
    If the target has a single Translation where ether the start or stop times are not None.
ValueError
    If there are multiple translations for a target and the start stamp of the first
    translation is not None.
ValueError
    If there are multiple translations for a target and the end stamp does not match the
    start stamp of the next translation.
ValueError
    If there are multiple translations for a target and the end stamp of the last
    translation is not None.

<a id="objects.objects.TranslationGroup.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the TranslationGroup fields.

Returns
-------
str
    A tab delimited string of the TranslationGroup fields.

<a id="objects.objects.TranslationGroup.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the TranslationGroup.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the TranslationGroup.

<a id="objects.objects.Algorithm"></a>

## Algorithm Objects

```python
class Algorithm(CasasObject)
```

This class represents an instance of an Algorithm that is used to process data.

Attributes
----------
action : str
    The defined action for the json, this object is 'algorithm'.
name : str
    The name of the Algorithm.
version_major : str
    The MAJOR version of the Algorithm.  You only increment the major version of an Algorithm
    when there is an update such that a previously trained model is no longer compatible.
version_minor : str
    The MINOR version of the Algorithm.  This is incremented for minor changes that do not
    effect the features or usable model.

<a id="objects.objects.Algorithm.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name, version_major, version_minor)
```

Initialize a new Algorithm object.

Parameters
----------
name : str
    The name of the Algorithm.
version_major : str
    The MAJOR version of the algorithm.
version_minor : str
    The MINOR version of the algorithm.

<a id="objects.objects.Algorithm.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the Algorithm fields.

Returns
-------
str
    A tab delimited string of the Algorithm fields.

<a id="objects.objects.Algorithm.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the Algorithm.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the Algorithm.

<a id="objects.objects.AlgorithmModel"></a>

## AlgorithmModel Objects

```python
class AlgorithmModel(CasasObject)
```

This class represents a trained model that is stored on disk with a config file.

Attributes
----------
action : str
    The defined action for the json, this object is 'algorithm_model'.
name : str
    The human name of the AlgorithmModel.
filename : str
    The absolute path for the AlgorithmModel file.
configfile : str
    The path for the model config file.
algorithm : Algorithm
    The associated Algorithm object for this AlgorithmModel.

<a id="objects.objects.AlgorithmModel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name, filename, configfile, algorithm)
```

Initialize a new AlgorithmModel object.

Parameters
----------
name : str
    The human name of the AlgorithmModel.
filename : str
    The absolute path for the AlgorithmModel file.
configfile : str
    The path for the model config file.
algorithm : Algorithm
    The associated Algorithm object for this AlgorithmModel.

<a id="objects.objects.AlgorithmModel.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the AlgorithmModel fields.

Returns
-------
str
    A tab delimited string of the AlgorithmModel fields.

<a id="objects.objects.AlgorithmModel.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the AlgorithmModel.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the AlgorithmModel.

<a id="objects.objects.AlgorithmProcessor"></a>

## AlgorithmProcessor Objects

```python
class AlgorithmProcessor(CasasObject)
```

This class represents an instance of an AlgorithmProcessor that performs analysis of
streaming data for a given site using the defined algorithm, algorithm_model,
translation_group, and timestamp range. Labeled events are uploaded using the provided
key and secret.

Attributes
----------
action : str
    The defined action for the json, this object is 'algorithm_model'.
algorithm : Algorithm
    The associated Algorithm object for this AlgorithmProcessor.
algorithm_model : AlgorithmModel
    The associated AlgorithmModel object for this AlgorithmProcessor.
translation_group : TranslationGroup
    The associated TranslationGroup object for this AlgorithmProcessor.
site : str
    The testbed that this AlgorithmProcessor is valid for.
key : str
    The key in the key:secret pair used to upload the AlgorithmProcessor output.
secret : str
    The secret in the key:secret pair used to upload the AlgorithmProcessor output.
use_live_data : boolean
    A flag to identify if this AlgorithmProcessor will be listening to live data.
use_historic_data : boolean
    A flag to identify if this AlgorithmProcessor will request a stream of historic data.
start_stamp : datetime.datetime
    The UTC stamp for the start of the coverage by this AlgorithmProcessor. If this is
    None, then the start of this AlgorithmProcessor would be the first event for the site
    if use_historic_data is True, otherwise it would start with the first live event it
    receives.
start_epoch : float
    The UTC epoch value representing the UTC stamp in start_stamp. If start_stamp is None, then
    this variable is also None.
end_stamp : datetime.datetime
    The UTC stamp for the end of the coverage by this AlgorithmProcessor. If this is None,
    then this AlgorithmProcessor will continue processing data for this site forever.
end_epoch : float
    The UTC epoch value representing the UTC stamp in end_stamp. If end_stamp is None, then
    this variable is also None.
current_stamp : datetime.datetime
    The current UTC stamp for where the AlgorithmProcessor is currently working.
current_epoch : float
    The UTC epoch value representing the UTC stamp in current_stamp.
processing_historic_data: boolean
    A flag to identify if this AlgorithmProcessor is still processing historic data,
    this will be updated when it is ready to start processing live data.

<a id="objects.objects.AlgorithmProcessor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(algorithm,
             algorithm_model,
             translation_group,
             site,
             key,
             secret,
             use_live_data,
             use_historic_data,
             start_stamp=None,
             end_stamp=None,
             current_stamp=None,
             processing_historic_data=False,
             is_active=True)
```

Initialize a new AlgorithmProcessor object.

Parameters
----------
algorithm : Algorithm
    The associated Algorithm object for this AlgorithmProcessor.
algorithm_model : AlgorithmModel
    The associated AlgorithmModel object for this AlgorithmProcessor.
translation_group : TranslationGroup
    The associated TranslationGroup object for this AlgorithmProcessor.
site : str
    The testbed that this AlgorithmProcessor is valid for.
key : str
    The key in the key:secret pair used to upload the AlgorithmProcessor output.
secret : str
    The secret in the key:secret pair used to upload the AlgorithmProcessor output.
use_live_data : boolean
    A flag to identify if this AlgorithmProcessor will be listening to live data.
use_historic_data : boolean
    A flag to identify if this AlgorithmProcessor will request a stream of historic data.
start_stamp : datetime.datetime, optional
    The UTC stamp for the start of the coverage by this AlgorithmProcessor. If this is
    None, then the start of this AlgorithmProcessor would be the first event for the site
    if use_historic_data is True, otherwise it would start with the first live event it
    receives.
end_stamp : datetime.datetime, optional
    The UTC stamp for the end of the coverage by this AlgorithmProcessor. If this is None,
    then this AlgorithmProcessor will continue processing data for this site forever.
current_stamp : datetime.datetime, optional
    The current UTC stamp for where the AlgorithmProcessor is currently working.
processing_historic_data: boolean, optional
    A flag to identify if this AlgorithmProcessor is still processing historic data,
    this will be updated when it is ready to start processing live data.
is_active: boolean, optional
    A flag to denote if this AlgorithmProcessor should be actively running or if it should
    not be active.

Raises
------
CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.

<a id="objects.objects.AlgorithmProcessor.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the AlgorithmProcessor fields.

Returns
-------
str
    A tab delimited string of the AlgorithmProcessor fields.

<a id="objects.objects.AlgorithmProcessor.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the AlgorithmProcessor.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the AlgorithmProcessor.

<a id="objects.objects.AlgorithmProcessorRequest"></a>

## AlgorithmProcessorRequest Objects

```python
class AlgorithmProcessorRequest(CasasObject)
```

This class represents a query request to get a list of AlgorithmProcessor objects that
a program will be in charge of handling.

Attributes
----------
action : str
    The defined action for the json, this object is 'algorithm_processor_request'.
algorithm_name : str
    An Algorithm name to search for.
version_major : str
    An Algorithm major version value to search for.
version_minor : str
    An Algorithm minor version value to search for.
algorithm_model_name : str
    The AlgorithmModel name to use in our search.

<a id="objects.objects.AlgorithmProcessorRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(algorithm_name, version_major, version_minor,
             algorithm_model_name)
```

Initialize a new AlgorithmProcessorRequest object.

Parameters
----------
algorithm_name : str
    An Algorithm name to search for.
version_major : str
    An Algorithm major version value to search for.
version_minor : str
    An Algorithm minor version value to search for.
algorithm_model_name : str
    The AlgorithmModel name to use in our search.

<a id="objects.objects.AlgorithmProcessorRequest.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the AlgorithmProcessorRequest fields.

Returns
-------
str
    A tab delimited string of the AlgorithmProcessorRequest fields.

<a id="objects.objects.AlgorithmProcessorRequest.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the AlgorithmProcessorRequest.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the AlgorithmProcessorRequest.

<a id="objects.objects.AlgorithmProcessorUpdate"></a>

## AlgorithmProcessorUpdate Objects

```python
class AlgorithmProcessorUpdate(CasasObject)
```

<a id="objects.objects.AlgorithmProcessorUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(algorithm_processor,
             new_algorithm=None,
             new_algorithm_model=None,
             new_translation_group=None,
             new_upload_key=None,
             new_upload_secret=None,
             new_use_live_data=None,
             new_use_historic_data=None,
             new_start_stamp=None,
             new_end_stamp=None,
             new_current_stamp=None,
             new_processing_historic_data=None,
             new_is_active=None)
```

Initialize a new AlgorithmProcessor object.

Parameters
----------
algorithm_processor : AlgorithmProcessor
    The AlgorithmProcessor object to update in the database.
new_algorithm : Algorithm, optional
    The associated Algorithm object for this AlgorithmProcessor.
new_algorithm_model : AlgorithmModel, optional
    The associated AlgorithmModel object for this AlgorithmProcessor.
new_translation_group : TranslationGroup, optional
    The associated TranslationGroup object for this AlgorithmProcessor.
new_upload_key : str, optional
    The key in the key:secret pair used to upload the AlgorithmProcessor output.
new_upload_secret : str, optional
    The secret in the key:secret pair used to upload the AlgorithmProcessor output.
new_use_live_data : boolean, optional
    A flag to identify if this AlgorithmProcessor will be listening to live data.
new_use_historic_data : boolean, optional
    A flag to identify if this AlgorithmProcessor will request a stream of historic data.
new_start_stamp : datetime.datetime, optional
    The UTC stamp for the start of the coverage by this AlgorithmProcessor. If this is
    None, then the start of this AlgorithmProcessor would be the first event for the site
    if use_historic_data is True, otherwise it would start with the first live event it
    receives.
new_end_stamp : datetime.datetime, optional
    The UTC stamp for the end of the coverage by this AlgorithmProcessor. If this is None,
    then this AlgorithmProcessor will continue processing data for this site forever.
new_current_stamp : datetime.datetime, optional
    The current UTC stamp for where the AlgorithmProcessor is currently working.
new_processing_historic_data: boolean, optional
    A flag to identify if this AlgorithmProcessor is still processing historic data,
    this will be updated when it is ready to start processing live data.
new_is_active: boolean, optional
    A flag to denote if this AlgorithmProcessor should be actively running or if it should
    not be active.

Raises
------
CasasDatetimeException
    If `new_start_stamp`, `new_end_stamp`, or `new_current_stamp` is a naive
    datetime.datetime object, where the tzinfo is not set.

<a id="objects.objects.CilBaseline"></a>

## CilBaseline Objects

```python
class CilBaseline(CasasObject)
```

<a id="objects.objects.CilBaseline.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site, is_ready, start_stamp, end_stamp)
```

Initialize a new CilBaseline object.

Parameters
----------
site : str
    The testbed that this is baseline is valid for.
is_ready : boolean
    A flag to denote if this baseline is ready to use.
start_stamp : datetime.datetime
    The UTC stamp for the start of the window to use in calculating the baseline.
end_stamp : datetime.datetime
    The UTC stamp for the end of the window to use in calculating the baseline.

Raises
------
CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.

<a id="objects.objects.CilBaseline.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the CilBaseline fields.

Returns
-------
str
    A tab delimited string of the CilBaseline fields.

<a id="objects.objects.CilBaseline.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CilBaseline.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the CilBaseline.

<a id="objects.objects.CilMetric"></a>

## CilMetric Objects

```python
class CilMetric(CasasObject)
```

<a id="objects.objects.CilMetric.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name)
```

Initialize a new CilMetric object.

Parameters
----------
name : str
    The name of the CilMetric.

<a id="objects.objects.CilMetric.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the CilMetric fields.

Returns
-------
str
    A tab delimited string of the CilMetric fields.

<a id="objects.objects.CilMetric.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CilMetric.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the CilMetric.

<a id="objects.objects.CilBaselineMetric"></a>

## CilBaselineMetric Objects

```python
class CilBaselineMetric(CasasObject)
```

<a id="objects.objects.CilBaselineMetric.__init__"></a>

#### \_\_init\_\_

```python
def __init__(baseline, metric, value_zero_five_std, value_one_std,
             value_one_five_std)
```

Initialize a new CilBaselineMetric object.

Parameters
----------
baseline : CilBaseline
    The CilBaseline this CilBaselineMetric is part of.
metric : CilMetric
    The CilMetric this CilBaselineMetric is linked to.
value_zero_five_std : float
    The standard deviation of the baseline metric multiplied by 0.5.
value_one_std : float
    The standard deviation of the baseline metric.
value_one_five_std : float
    The standard deviation of the baseline metric multiplied by 1.5.

<a id="objects.objects.CilBaselineMetric.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the CilBaselineMetric fields.

Returns
-------
str
    A tab delimited string of the CilBaselineMetric fields.

<a id="objects.objects.CilBaselineMetric.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CilBaselineMetric.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the CilBaselineMetric.

<a id="objects.objects.CilData"></a>

## CilData Objects

```python
class CilData(CasasObject)
```

<a id="objects.objects.CilData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site, metric, value, stamp)
```

Initialize a new CilData object.

Parameters
----------
site : str
    The testbed that this CilData is valid for.
metric : CilMetric
    The CilMetric that this data is for.
value : float
    The calculated data value for this metric.
stamp : datetime.datetime
    The UTC stamp that this data is for.

Raises
------
CasasDatetimeException
    If `stamp` is a naive datetime.datetime object, where the tzinfo is not set.

<a id="objects.objects.CilData.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the CilData fields.

Returns
-------
str
    A tab delimited string of the CilData fields.

<a id="objects.objects.CilData.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the CilData.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the CilData.

<a id="objects.objects.RequestEvents"></a>

## RequestEvents Objects

```python
class RequestEvents(CasasObject)
```

<a id="objects.objects.RequestEvents.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site, start_stamp, end_stamp, sensor_types=None)
```

Initialize a new RequestEvents object.

Parameters
----------
site : str
    The testbed that this RequestEvents object is for.
start_stamp : datetime.datetime
    The UTC timestamp for the start of the requested window of data.
end_stamp : datetime.datetime
    The UTC timestamp for the end of the requested window of data.
sensor_types : list, optional
    An optional list of sensor types to limit our request to.

Raises
------
CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.

<a id="objects.objects.RequestEvents.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the RequestEvents fields.

Returns
-------
str
    A tab delimited string of the RequestEvents fields.

<a id="objects.objects.RequestEvents.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the RequestEvents.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the RequestEvents.

<a id="objects.objects.RequestDataset"></a>

## RequestDataset Objects

```python
class RequestDataset(CasasObject)
```

<a id="objects.objects.RequestDataset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(site,
             start_stamp,
             end_stamp,
             experiment,
             dataset,
             sensor_types=None)
```

Initialize a new RequestDataset object.

Parameters
----------
site : str
    The testbed that this RequestDataset object is for.
start_stamp : datetime.datetime
    The UTC timestamp for the start of the requested window of data.
end_stamp : datetime.datetime
    The UTC timestamp for the end of the requested window of data.
experiment : str
    The name of the experiment we wish to get data from.
dataset : str
    The name of the dataset we wish to get data from.
sensor_types : list, optional
    An optional list of sensor types to limit our request to.

Raises
------
CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.

<a id="objects.objects.RequestDataset.get_old_str"></a>

#### get\_old\_str

```python
def get_old_str()
```

Returns a tab delimited string of the RequestDataset fields.

Returns
-------
str
    A tab delimited string of the RequestDataset fields.

<a id="objects.objects.RequestDataset.get_json"></a>

#### get\_json

```python
def get_json(secret=None, key=None)
```

Returns a JSON string representing the RequestDataset.

Parameters
----------
secret : str, optional
    The secret in the key:secret required for uploading data.
key : str, optional
    The key in the key:secret required for uploading data.

Returns
-------
str
    A JSON string representing the RequestDataset.

<a id="objects.objects.make_epoch"></a>

#### make\_epoch

```python
def make_epoch(utc_datetime)
```

This function converts a datetime.datetime object into its float equivalent for the
unix epoch.

Parameters
----------
utc_datetime : datetime.datetime
    A UTC datetime.datetime object to convert into an epoch.

Returns
-------
float
    The UTC epoch value for the provided UTC datetime.datetime object.

Raises
------
CasasDatetimeException
    If `utc_datetime` is a naive datetime.datetime object, where the tzinfo is not set or
    is not the UTC timezone.

<a id="objects.objects.epoch_to_stamp"></a>

#### epoch\_to\_stamp

```python
def epoch_to_stamp(utc_epoch)
```

This function converts a float representing a UTC unix epoch into a datetime.datetime
object that is aware of the timezone.

Parameters
----------
utc_epoch : float
    A representation of a UTC unix epoch.

Returns
-------
datetime.datetime
    The datetime.datetime object created from the `utc_epoch`.

<a id="objects.objects.get_routing_key"></a>

#### get\_routing\_key

```python
def get_routing_key(casas_object)
```

This function takes in a CasasObject subclass and returns the RabbitMQ routing key for
the given object class.

Parameters
----------
casas_object : CasasObject
    The object that we want the routing key for.

Returns
-------
str
    The routing key for casas_object.

<a id="objects.objects.build_routing_key"></a>

#### build\_routing\_key

```python
def build_routing_key(action=EVENT,
                      sensor_type='*',
                      package_type='*',
                      site='*',
                      algorithm_name='*',
                      algorithm_version_major='*',
                      algorithm_version_minor='*',
                      metric='*')
```

This function builds a routing key from the provided parameters.

Parameters
----------
action : str
sensor_type : str, optional
    This is the desired sensor_type, default is '*' for all values.
package_type : str, optional
    This is the desired package_type, default is '*' for all values.
site : str, optional
    This is the desired site, default is '*' for all values.

Returns
-------
str
    The built routing key.

<a id="objects.objects.build_objects_from_json"></a>

#### build\_objects\_from\_json

```python
def build_objects_from_json(message, amqp_obj=None)
```

This function converts a string message into a list of casas.objects.

Parameters
----------
message : str
    A string of a JSON list containing dictionaries.
amqp_obj : object (optional)
    A rabbitmq.py Connection object to help keep things alive during large objects.

Returns
-------
list(casas.objects)
    A list containing Event, Tag, Control, Heartbeat, or Translation objects.
    This list can be mixed for different types so make sure to check the action variable.

<a id="objects.TA2_logic"></a>

# objects.TA2\_logic

<a id="objects.TA2_logic.TA2Logic"></a>

## TA2Logic Objects

```python
class TA2Logic(object)
```

<a id="objects.TA2_logic.TA2Logic.experiment_start"></a>

#### experiment\_start

```python
def experiment_start()
```

This function is called when this TA2 has connected to a TA1 and is ready to begin
the experiment.

<a id="objects.TA2_logic.TA2Logic.training_start"></a>

#### training\_start

```python
def training_start()
```

This function is called when we are about to begin training on episodes of data in
your chosen domain.

<a id="objects.TA2_logic.TA2Logic.training_episode_start"></a>

#### training\_episode\_start

```python
def training_episode_start(episode_number: int)
```

This function is called at the start of each training episode, with the current episode
number (0-based) that you are about to begin.

Parameters
----------
episode_number : int
    This identifies the 0-based episode number you are about to begin training on.

<a id="objects.TA2_logic.TA2Logic.training_instance"></a>

#### training\_instance

```python
def training_instance(feature_vector: dict, feature_label: dict) -> dict
```

Process a training

Parameters
----------
feature_vector : dict
    The dictionary of the feature vector.  Domain specific feature vector formats are
    defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
feature_label : dict
    The dictionary of the label for this feature vector.  Domain specific feature labels
    are defined on the github (https://github.com/holderlb/WSU-SAILON-NG). This will always
    be in the format of {'action': label}.  Some domains that do not need an 'oracle' label
    on training data will receive a valid action chosen at random.

Returns
-------
dict
    A dictionary of your label prediction of the format {'action': label}.  This is
        strictly enforced and the incorrect format will result in an exception being thrown.

<a id="objects.TA2_logic.TA2Logic.training_performance"></a>

#### training\_performance

```python
def training_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="objects.TA2_logic.TA2Logic.training_episode_end"></a>

#### training\_episode\_end

```python
def training_episode_end(performance: float,
                         feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the training episode and indicates that the training
episode has ended.

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

<a id="objects.TA2_logic.TA2Logic.training_end"></a>

#### training\_end

```python
def training_end()
```

This function is called when we have completed the training episodes.

<a id="objects.TA2_logic.TA2Logic.train_model"></a>

#### train\_model

```python
def train_model()
```

Train your model here if needed.  If you don't need to train, just leave the function
empty.  After this completes, the logic calls save_model() and reset_model() as needed
throughout the rest of the experiment.

<a id="objects.TA2_logic.TA2Logic.save_model"></a>

#### save\_model

```python
def save_model(filename: str)
```

Saves the current model in memory to disk so it may be loaded back to memory again.

Parameters
----------
filename : str
    The filename to save the model to.

<a id="objects.TA2_logic.TA2Logic.reset_model"></a>

#### reset\_model

```python
def reset_model(filename: str)
```

Loads the model from disk to memory.

Parameters
----------
filename : str
    The filename where the model was stored.

<a id="objects.TA2_logic.TA2Logic.trial_start"></a>

#### trial\_start

```python
def trial_start(trial_number: int, novelty_description: dict)
```

This is called at the start of a trial with the current 0-based number.

Parameters
----------
trial_number : int
    This is the 0-based trial number in the novelty group.
novelty_description : dict
    A dictionary that will have a description of the trial's novelty.

<a id="objects.TA2_logic.TA2Logic.testing_start"></a>

#### testing\_start

```python
def testing_start()
```

This is called after a trial has started but before we begin going through the
episodes.

<a id="objects.TA2_logic.TA2Logic.testing_episode_start"></a>

#### testing\_episode\_start

```python
def testing_episode_start(episode_number: int)
```

This is called at the start of each testing episode in a trial, you are provided the
0-based episode number.

Parameters
----------
episode_number : int
    This is the 0-based episode number in the current trial.

<a id="objects.TA2_logic.TA2Logic.testing_instance"></a>

#### testing\_instance

```python
def testing_instance(feature_vector: dict,
                     novelty_indicator: bool = None) -> dict
```

Evaluate a testing instance.  Returns the predicted label or action, if you believe
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

<a id="objects.TA2_logic.TA2Logic.testing_performance"></a>

#### testing\_performance

```python
def testing_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="objects.TA2_logic.TA2Logic.testing_episode_end"></a>

#### testing\_episode\_end

```python
def testing_episode_end(performance: float,
                        feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the testing episode.

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

<a id="objects.TA2_logic.TA2Logic.testing_end"></a>

#### testing\_end

```python
def testing_end()
```

This is called after the last episode of a trial has completed, before trial_end().

<a id="objects.TA2_logic.TA2Logic.trial_end"></a>

#### trial\_end

```python
def trial_end()
```

This is called at the end of each trial.

<a id="objects.TA2_logic.TA2Logic.experiment_end"></a>

#### experiment\_end

```python
def experiment_end()
```

This is called when the experiment is done.

<a id="objects.SOTA_logic"></a>

# objects.SOTA\_logic

<a id="objects.SOTA_logic.SotaLogic"></a>

## SotaLogic Objects

```python
class SotaLogic(TA2Logic)
```

<a id="objects.SOTA_logic.SotaLogic.training_instance"></a>

#### training\_instance

```python
def training_instance(feature_vector: dict, feature_label: dict) -> dict
```

Process a training

Parameters
----------
feature_vector : dict
    The dictionary of the feature vector.  Domain specific feature vector formats are
    defined on the github (https://github.com/holderlb/WSU-SAILON-NG).
feature_label : dict
    The dictionary of the label for this feature vector.  Domain specific feature labels
    are defined on the github (https://github.com/holderlb/WSU-SAILON-NG). This will always
    be in the format of {'action': label}.  Some domains that do not need an 'oracle' label
    on training data will receive a valid action chosen at random.

Returns
-------
dict
    A dictionary of your label prediction of the format {'action': label}.  This is
        strictly enforced and the incorrect format will result in an exception being thrown.

<a id="objects.SOTA_logic.SotaLogic.training_performance"></a>

#### training\_performance

```python
def training_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="objects.SOTA_logic.SotaLogic.training_episode_end"></a>

#### training\_episode\_end

```python
def training_episode_end(performance: float,
                         feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the training episode and indicates that the training
episode has ended.

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

<a id="objects.SOTA_logic.SotaLogic.training_end"></a>

#### training\_end

```python
def training_end()
```

This function is called when we have completed the training episodes.

<a id="objects.SOTA_logic.SotaLogic.train_model"></a>

#### train\_model

```python
def train_model()
```

Train your model here if needed.  If you don't need to train, just leave the function
empty.  After this completes, the logic calls save_model() and reset_model() as needed
throughout the rest of the experiment.

<a id="objects.SOTA_logic.SotaLogic.save_model"></a>

#### save\_model

```python
def save_model(filename: str)
```

Save the current trained model to disk so agent can reset to it at the start of
each trial.

Parameters
----------
filename : str
    The filename to save the model to.

<a id="objects.SOTA_logic.SotaLogic.reset_model"></a>

#### reset\_model

```python
def reset_model(filename: str)
```

Reset model to state just after training.

Parameters
----------
filename : str
    The filename where the model was stored.

<a id="objects.SOTA_logic.SotaLogic.trial_start"></a>

#### trial\_start

```python
def trial_start(trial_number: int, novelty_description: dict)
```

This is called at the start of a trial with the current 0-based number.

Parameters
----------
trial_number : int
    This is the 0-based trial number in the novelty group.
novelty_description : dict
    A dictionary that will have a description of the trial's novelty.

<a id="objects.SOTA_logic.SotaLogic.testing_start"></a>

#### testing\_start

```python
def testing_start()
```

This is called after a trial has started but before we begin going through the
episodes.

<a id="objects.SOTA_logic.SotaLogic.testing_episode_start"></a>

#### testing\_episode\_start

```python
def testing_episode_start(episode_number: int)
```

This is called at the start of each testing episode in a trial, you are provided the
0-based episode number.

Parameters
----------
episode_number : int
    This is the 0-based episode number in the current trial.

<a id="objects.SOTA_logic.SotaLogic.testing_instance"></a>

#### testing\_instance

```python
def testing_instance(feature_vector: dict,
                     novelty_indicator: bool = None) -> dict
```

Evaluate a testing instance.  Returns the predicted label or action, if you believe
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

<a id="objects.SOTA_logic.SotaLogic.testing_performance"></a>

#### testing\_performance

```python
def testing_performance(performance: float, feedback: dict = None)
```

Provides the current performance on training after each instance.

Parameters
----------
performance : float
    The normalized performance score.
feedback : dict, optional
    A dictionary that may provide additional feedback on your prediction based on the
    budget set in the TA1. If there is no feedback, the object will be None.

<a id="objects.SOTA_logic.SotaLogic.testing_episode_end"></a>

#### testing\_episode\_end

```python
def testing_episode_end(performance: float,
                        feedback: dict = None) -> (float, float, int, dict)
```

Provides the final performance on the testing episode.

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

<a id="objects.SOTA_logic.SotaLogic.testing_end"></a>

#### testing\_end

```python
def testing_end()
```

This is called after the last episode of a trial has completed, before trial_end().

<a id="objects.SOTA_logic.SotaLogic.trial_end"></a>

#### trial\_end

```python
def trial_end()
```

This is called at the end of each trial.

<a id="objects.SOTA_logic.SotaLogic.experiment_end"></a>

#### experiment\_end

```python
def experiment_end()
```

This is called when the experiment is done.

<a id="objects.rabbitmq"></a>

# objects.rabbitmq

<a id="objects.rabbitmq.ConsumeCallback"></a>

## ConsumeCallback Objects

```python
class ConsumeCallback(object)
```

This is a helper class for subscribing to RabbitMQ exchanges and queues then using
callback functions with the processed results.

<a id="objects.rabbitmq.ConsumeCallback.__init__"></a>

#### \_\_init\_\_

```python
def __init__(casas_events=True,
             callback_function=None,
             is_exchange=False,
             exchange_name=None,
             is_queue=False,
             queue_name=None,
             limit_to_sensor_types=None,
             auto_ack=False,
             callback_full_params=False,
             translations=None,
             timezone=None,
             manual_ack=False)
```

Initialize an instance of a ConsumeCallback object.

Parameters
----------
casas_events : bool
    Boolean defining if this exchange will be sending casas events.
callback_function : function
    The callback function to call when events from this queue binding arrive.
is_exchange : bool
    Boolean defining if we are subscribed to an exchange.
exchange_name : str
    Name of the RabbitMQ exchange.
is_queue : bool
    Boolean defining if we are subscribed to a queue.
queue_name : str
    Name of the RabbitMQ queue.
limit_to_sensor_types : list
    A list that will define what sensor types will be allowed through.
    All sensors are allowed through by default.
auto_ack : bool
    Boolean that if set to True, automatic acknowledgement mode will be used
callback_full_params : bool
    Boolean defining if the callback_function will be expecting the full callback
    parameters (channel, method, properties, body) or just body.
translations : dict
    A dictionary of TranslationGroup objects.
    translations[SITE] = TranslationGroup
timezone : dict
    A dictionary of sites as keys, with the value as the timezone string for that site.
    Assumes all sites are 'America/Los_Angeles' unless given in dict().
manual_ack : bool, optional
    Boolean that determines if the calling program will manually be sending the message
    ack.  This variable is overridden to False if auto_ack is True or if
    callback_full_params is False (as you need those to send the ack).  The default value
    is False.

<a id="objects.rabbitmq.ConsumeCallback.on_message"></a>

#### on\_message

```python
def on_message(channel, basic_deliver, properties, body)
```

Invoked by pika when a message is delivered from RabbitMQ. The
channel is passed for your convenience. The basic_deliver object that
is passed in carries the exchange, routing key, delivery tag and
a redelivered flag for the message. The properties passed in is an
instance of BasicProperties with the message properties and the body
is the message that was sent.

Parameters
----------
channel : pika.channel.Channel
    The channel object.
basic_deliver : pika.Spec.Basic.Deliver
    basic_deliver method.
properties : pika.Spec.BasicProperties
    properties object.
body : str|unicode
    The message body.

<a id="objects.rabbitmq.Connection"></a>

## Connection Objects

```python
class Connection()
```

This is a consumer that will handle unexpected interactions
with RabbitMQ such as channel and connection closures.

If RabbitMQ closes the connection, it will reopen it. You should
look at the output, as there are limited reasons why the connection may
be closed, which usually are tied to permission related issues or
socket timeouts.

If the channel is closed, it will indicate a problem with one of the
commands that were issued and that should surface in the output as well.

<a id="objects.rabbitmq.Connection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(agent_name,
             amqp_user,
             amqp_pass,
             amqp_host,
             amqp_port,
             amqp_vhost='/',
             amqp_ssl=True,
             translations=None,
             timezone=None,
             request_timeout=None)
```

Create a new instance of the CASAS RammitMQ Connection class.

Parameters
----------
agent_name : str
    The name of the agent using the RabbitMQ connection, used in logging and debugging.
amqp_user : str
    The RabbitMQ username.
amqp_pass : str
    The RabbitMQ password.
amqp_host : str
    The RabbitMQ hostname.
amqp_port : str
    The RabbitMQ port to use for connecting.
amqp_vhost : str,optional
    The RabbitMQ virtual host to connect to, with a default value of '/'.
amqp_ssl : bool,optional
    Defines if using SSL to make the connection to the RabbitMQ server.
translations : dict,optional
    A dictionary of dictionaries with format
    translations[SITE][TARGET] = (sensor_1,sensor_2)
timezone : dict,optional
    A dictionary of sites as keys, with the value as the timezone string for that site.
    Assumes all sites are 'America/Los_Angeles' unless given in dict().
request_timeout : int,optional
    An integer of the global timeout to use.

<a id="objects.rabbitmq.Connection.set_on_connect_callback"></a>

#### set\_on\_connect\_callback

```python
def set_on_connect_callback(callback)
```

Set a callback function to call when the agent has connected.

Parameters
----------
callback : function
    The callback function that will be called after a connection is established.
    The function can not require any parameters.

<a id="objects.rabbitmq.Connection.clear_on_connect_callback"></a>

#### clear\_on\_connect\_callback

```python
def clear_on_connect_callback()
```

Clear a callback function that may or may not have been set for on_connect.

<a id="objects.rabbitmq.Connection.set_on_disconnect_callback"></a>

#### set\_on\_disconnect\_callback

```python
def set_on_disconnect_callback(callback)
```

Set a callback function to call when the agent has been disconnected.

Parameters
----------
callback : function
    The callback function that will be called after the agent has been disconnected.
    The function can not require any parameters.

<a id="objects.rabbitmq.Connection.clear_on_disconnect_callback"></a>

#### clear\_on\_disconnect\_callback

```python
def clear_on_disconnect_callback()
```

Clear a callback function that may or may not have been set for on_disconnect.

<a id="objects.rabbitmq.Connection.set_on_connection_blocked_callback"></a>

#### set\_on\_connection\_blocked\_callback

```python
def set_on_connection_blocked_callback(callback)
```

Set a callback function to call when the agent has been blocked from publishing.

Parameters
----------
callback : function
    The callback function that will be called after the agent has been blocked from
    publishing.
    The function can not require any parameters.

<a id="objects.rabbitmq.Connection.clear_on_connection_blocked_callback"></a>

#### clear\_on\_connection\_blocked\_callback

```python
def clear_on_connection_blocked_callback()
```

Clear a callback function that may or may not have been set for on_connection_blocked.

<a id="objects.rabbitmq.Connection.set_on_connection_unblocked_callback"></a>

#### set\_on\_connection\_unblocked\_callback

```python
def set_on_connection_unblocked_callback(callback)
```

Set a callback function to call when the agent has been unblocked from publishing.

Parameters
----------
callback : function
    The callback function that will be called after the agent has been unblocked from
    publishing.
    The function can not require any parameters.

<a id="objects.rabbitmq.Connection.clear_on_connection_unblocked_callback"></a>

#### clear\_on\_connection\_unblocked\_callback

```python
def clear_on_connection_unblocked_callback()
```

Clear a callback function that may or may not have been set for on_connection_unblocked.

<a id="objects.rabbitmq.Connection.process_system_request_callback"></a>

#### process\_system\_request\_callback

```python
def process_system_request_callback(ch, method, props, body, response)
```

This is a callback function for processing the response to the getting or setting of a
system request type object.

Parameters
----------
ch : pika.channel.Channel
    The channel object.
method : pika.Spec.Basic.Deliver
    Basic deliver method.
props : pika.Spec.BasicProperties
    Properties of the message.
body : str|unicode
    The message body.
response : list
    A list of processed casas.objects that have been built from the JSON provided in
    the message body.

<a id="objects.rabbitmq.Connection.request_dataset"></a>

#### request\_dataset

```python
def request_dataset(site,
                    start_stamp,
                    end_stamp,
                    experiment,
                    dataset,
                    key,
                    secret,
                    sensor_types=None,
                    callback=None,
                    completed_callback=None,
                    callback_full_params=False,
                    manual_ack=False)
```

Request a dataset be sent to a provided function, event-by-event.

Parameters
----------
site : str
    The testbed that this request is for.
start_stamp : datetime.datetime
    The UTC timestamp for the start of the requested window of data.
end_stamp : datetime.datetime
    The UTC timestamp for the end of the request window of data.
experiment : str
    The name of the experiment we wish to get data from.
dataset : str
    The name of the dataset we wish to get data from.
key : str
    The key value that is paired with secret for accessing data.
secret : str
    The secret value that is paired with key for accessing data.
sensor_types : list, optional
    An optional list of sensor types to limit our request to.
callback : function, optional
    The callback function that will receive the requested events.
completed_callback : function, optional
    A function that will be called once the full dataset has been requested.
callback_full_params : bool, optional
    Boolean defining if the callback function will be expecting the full callback
    parameters (channel, method, properties, body) or just body.  The default value
    is False.
manual_ack : bool, optional
    Boolean that determines if the calling program will manually be sending the message
    ack.  This variable is overridden to False if callback_full_params is False (as you
    need those to send the ack).  The default value is False.

Raises
------
objects.CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.
objects.CasasRabbitMQException
    If the connection is currently in the consuming state and not able to be utilized for
    RPC type calls right now.

<a id="objects.rabbitmq.Connection.request_events_historic"></a>

#### request\_events\_historic

```python
def request_events_historic(site,
                            start_stamp,
                            end_stamp,
                            key,
                            secret,
                            sensor_types=None,
                            callback=None,
                            completed_callback=None,
                            callback_full_params=False,
                            manual_ack=False)
```

Request historic events in a given time range be sent to a provided function callback,
event-by-event.

Parameters
----------
site : str
    The testbed that this request is for.
start_stamp : datetime.datetime
    The UTC timestamp for the start of the requested window of data.
end_stamp : datetime.datetime
    The UTC timestamp for the end of the request window of data.
key : str
    The key value that is paired with secret for accessing data.
secret : str
    The secret value that is paired with key for accessing data.
sensor_types : list, optional
    An optional list of sensor types to limit our request to.
callback : function, optional
    The callback function that will receive the requested events.
completed_callback : function, optional
    A function that will be called once the full dataset has been requested.
callback_full_params : bool, optional
    Boolean defining if the callback function will be expecting the full callback
    parameters (channel, method, properties, body) or just body.  The default value
    is False.
manual_ack : bool, optional
    Boolean that determines if the calling program will manually be sending the message
    ack.  This variable is overridden to False if callback_full_params is False (as you
    need those to send the ack).  The default value is False.

Raises
------
objects.CasasDatetimeException
    If `start_stamp` or `end_stamp` is a naive datetime.datetime object, where the tzinfo
    is not set.
objects.CasasRabbitMQException
    If the connection is currently in the consuming state and not able to be utilized for
    RPC type calls right now.

<a id="objects.rabbitmq.Connection.process_request_events_callback"></a>

#### process\_request\_events\_callback

```python
def process_request_events_callback(ch, method, props, body, response)
```

This is a callback function for processing the responses to a request for historical
events, and possibly tags.

Parameters
----------
ch : pika.channel.Channel
    The channel object.
method : pika.Spec.Basic.Deliver
    Basic deliver method.
props : pika.Spec.BasicProperties
    Properties of the message.
body : str|unicode
    The message body.
response : list
    A list of processed casas.objects that have been built from the JSON provided in
    the message body.

<a id="objects.rabbitmq.Connection.setup_subscribe_to_exchange"></a>

#### setup\_subscribe\_to\_exchange

```python
def setup_subscribe_to_exchange(exchange_name,
                                exchange_type='topic',
                                routing_key='#',
                                exchange_durable=True,
                                exchange_auto_delete=False,
                                casas_events=True,
                                callback_function=None,
                                queue_name=None,
                                queue_durable=False,
                                queue_exclusive=True,
                                queue_auto_delete=True,
                                limit_to_sensor_types=None,
                                auto_ack=False,
                                callback_full_params=False,
                                manual_ack=False)
```

This function sets up a subscription to events from an exchange.

Parameters
----------
exchange_name : str
    Name of the RabbitMQ exchange.
exchange_type : str, optional
    The type of the exchange, usually 'topic'.
routing_key : str, optional
    The routing key to use when binding to the exchange,
    can be used for filtering by sensor_type.
exchange_durable : bool, optional
    Boolean defining exchange durability.
exchange_auto_delete : bool, optional
    Remove exchange when no more queues are bound to it.
casas_events : bool, optional
    Boolean defining if this exchange will be sending casas events.
callback_function : function
    The callback function to call when events from this queue binding arrive.
queue_name : str, optional
    Name of the RabbitMQ queue.
queue_durable : bool, optional
    Boolean defining queue durability.
queue_exclusive : bool, optional
    Boolean defining queue exclusivity.
queue_auto_delete : bool, optional
    Boolean defining if the queue should be automatically deleted on consumer disconnection.
limit_to_sensor_types : list
    A list that will define what sensor types will be allowed through.
    All sensors are allowed through by default.
auto_ack : bool, optional
    Boolean that if set to True, automatic acknowledgement mode will be used.
callback_full_params : bool, optional
    Boolean defining if the callback_function will be expecting the full callback
    parameters (channel, method, properties, body) or just body.
manual_ack : bool, optional
    Boolean that determines if the calling program will manually be sending the message
    ack.  This variable is overridden to False if auto_ack is True or if
    callback_full_params is False (as you need those to send the ack).  The default value
    is False.

<a id="objects.rabbitmq.Connection.remove_subscribe_to_exchange"></a>

#### remove\_subscribe\_to\_exchange

```python
def remove_subscribe_to_exchange(exchange_name, routing_key='#')
```

Removes a subscription to an exchange with the given routing_key.  If the exchange_name
and/or routing_key are not currently being used, then it simply returns with no errors.

Parameters
----------
exchange_name : str
    The name of the exchange that we would like to unsubscribe.
routing_key : str, optional
    The routing key used in the subscription of the exchange.

<a id="objects.rabbitmq.Connection.setup_publish_to_exchange"></a>

#### setup\_publish\_to\_exchange

```python
def setup_publish_to_exchange(exchange_name,
                              exchange_type='topic',
                              exchange_durable=True,
                              routing_key=None,
                              exchange_auto_delete=False)
```

Prepare the Connection to publish to the exchange.

Parameters
----------
exchange_name : str
    The name of the exchange you wish to publish to.
exchange_type : str, optional
    The type of the exchange you wish to publish to.
exchange_durable : bool, optional
    Boolean defining exchange durability.
routing_key : str, optional
    Ignore this parameter for now.
exchange_auto_delete : bool, optional
    Remove exchange when no more queues are bound to it.

<a id="objects.rabbitmq.Connection.remove_publish_to_exchange"></a>

#### remove\_publish\_to\_exchange

```python
def remove_publish_to_exchange(exchange_name)
```

Removes the entry holder in the config to publish to the provided exchange.  If the
exchange_name are not currently in the config, then it simply returns with no errors.

Parameters
----------
exchange_name : str
    The name of the exchange we wish to stop publishing to.

<a id="objects.rabbitmq.Connection.setup_subscribe_to_queue"></a>

#### setup\_subscribe\_to\_queue

```python
def setup_subscribe_to_queue(queue_name,
                             queue_durable=False,
                             queue_exclusive=False,
                             queue_auto_delete=False,
                             casas_events=True,
                             callback_function=None,
                             limit_to_sensor_types=None,
                             auto_ack=False,
                             callback_full_params=False,
                             manual_ack=False)
```

This function sets up a subscription to events from a queue.

Parameters
----------
queue_name : str
    Name of the RabbitMQ queue.
queue_durable : bool, optional
    Boolean defining queue durability.
queue_exclusive : bool, optional
    Boolean defining queue exclusivity.
queue_auto_delete : bool, optional
    Boolean defining if the queue should be automatically deleted on consumer disconnection.
casas_events : bool
    Boolean defining if this queue will be sending casas events.
callback_function : function
    The callback function to call when events from this queue arrive.
limit_to_sensor_types : list, optional
    A list of sensor types to limit sending to the callback function, an empty list results
    in no filtering of events.
auto_ack : bool, optional
    Boolean that if set to True, automatic acknowledgement mode will be used.
callback_full_params : bool, optional
    Boolean defining if the callback_function will be expecting the full callback
    parameters (channel, method, properties, body) or just body.
manual_ack : bool, optional
    Boolean that determines if the calling program will manually be sending the message
    ack.  This variable is overridden to False if auto_ack is True or if
    callback_full_params is False (as you need those to send the ack).  The default value
    is False.

<a id="objects.rabbitmq.Connection.remove_subscribe_to_queue"></a>

#### remove\_subscribe\_to\_queue

```python
def remove_subscribe_to_queue(queue_name, limit_to_sensor_types=None)
```

Removes a subscription to a queue.  If the queue_name and limit_to_sensor_types list
are not currently being used, then it simply returns with no errors.

Parameters
----------
queue_name : str
    The name of the queue that we would like to unsubscribe from.
limit_to_sensor_types : list, optional
    The list of sensor types to limit sending to the callback function.

<a id="objects.rabbitmq.Connection.setup_publish_to_queue"></a>

#### setup\_publish\_to\_queue

```python
def setup_publish_to_queue(queue_name,
                           queue_durable=False,
                           queue_exclusive=False,
                           queue_auto_delete=False,
                           delivery_mode=2)
```

Prepare the Connection to publish to a queue.

Parameters
----------
queue_name : str
    The name of the queue we wish to publish to.
queue_durable : bool, optional
    Boolean defining the durability of the queue.
queue_exclusive : bool, optional
    Boolean defining the exclusivity of the queue.
queue_auto_delete : bool, optional
    Boolean defining if the queue will automatically be deleted on disconnection.
delivery_mode : int
    Integer defining the delivery method for RabbitMQ.

<a id="objects.rabbitmq.Connection.remove_publish_to_queue"></a>

#### remove\_publish\_to\_queue

```python
def remove_publish_to_queue(queue_name)
```

Removes the entry holder in the config to publish to the provided queue.  If the
queue_name is not currently in the config, then it simply returns with no errors.

Parameters
----------
queue_name : str
    The name of the queue we wish to stop publishing to.

<a id="objects.rabbitmq.Connection.publish_to_exchange"></a>

#### publish\_to\_exchange

```python
def publish_to_exchange(exchange_name,
                        casas_object=None,
                        body_str=None,
                        routing_key=None,
                        correlation_id=None,
                        delivery_mode=2,
                        key=None,
                        secret=None,
                        reply_to=None)
```

Publish a message to the exchange.

Parameters
----------
exchange_name : str
    Name of the exchange we are publishing to.
casas_object : objects.CasasObject
    CASAS object to uploaded, this function handles the standard behaviors for us.
body_str : str, optional
    Use if you are publishing a non-CASAS object.  This value will be overwritten if you
    provide a value for casas_object.
routing_key : str, optional
    Use if you are using body_str to publish, this will be overwritten if using
    casas_object to upload.
correlation_id : str, optional
    This is an optional correlation ID to use when performing RPC style calls.
delivery_mode : int, optional
    Integer defining the delivery method for RabbitMQ.
key : str, optional
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.
secret : str, optional
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
reply_to : str, optional
    This is the name of the exclusive queue that the RPC style call on the other end
    should publish the response to.

Returns
-------

<a id="objects.rabbitmq.Connection.publish_to_queue"></a>

#### publish\_to\_queue

```python
def publish_to_queue(queue_name,
                     casas_object=None,
                     body_str=None,
                     correlation_id=None,
                     delivery_mode=2,
                     key=None,
                     secret=None,
                     reply_to=None)
```

Publish a message to the queue.

Parameters
----------
queue_name : str
    Name of the queue we are publishing to.
casas_object : objects.CasasObject
    CASAS object to be uploaded, this function handles the standard behaviors for us.
body_str : str, optional
    Use if you are publishing a non-CASAS object.  This value will be overwritten if you
    provide a value for casas_object.
correlation_id : str, optional
    This is an optional correlation ID to use when performing RPC style calls.
delivery_mode : int, optional
    Integer defining the delivery method for RabbitMQ.
key : str, optional
    The key value that is paired with secret for uploading events. If this is not provided
    it is removed from the JSON object before returning.
secret : str, optional
    The secret value that is paired with key for uploading events. If this is not provided
    it is removed from the JSON object before returning.
reply_to : str, optional
    This is the name of the exclusive queue that the RPC style call on the other end
    should publish the response to.

<a id="objects.rabbitmq.Connection.basic_get"></a>

#### basic\_get

```python
def basic_get(queue)
```

Parameters
----------
queue : str
    Name of the queue from which to get a message.

Returns
-------
(pika.spec.Basic.GetOk|None, pika.spec.BasicProperties|None, str|None)

<a id="objects.rabbitmq.Connection.basic_ack"></a>

#### basic\_ack

```python
def basic_ack(delivery_tag)
```

Acknowledge one message.

Parameters
----------
delivery_tag : int
    The server-assigned delivery tag.

<a id="objects.rabbitmq.Connection.start_consuming"></a>

#### start\_consuming

```python
def start_consuming()
```

Tells the connection to start consuming available messages.

Raises
------
objects.CasasRabbitMQException
    If the connection is currently waiting on a direct RPC request or RPC event/dataset
    callback processing we can not enable the connection to consume right now.

<a id="objects.rabbitmq.Connection.stop_consuming"></a>

#### stop\_consuming

```python
def stop_consuming()
```

Tell the connection to stop consuming available messages right now.

<a id="objects.rabbitmq.Connection.process_data_events"></a>

#### process\_data\_events

```python
def process_data_events(time_limit=0)
```

Will make sure that data events are processed.  Dispatches timer and channel callbacks
if not called from the scope of BlockingConnection or BlockingChannel callback.

Parameters
----------
time_limit : float
    Suggested upper bound on processing time in seconds.  The actual blocking time depends
    on the granularity of the underlying ioloop.  Zero means return as soon as possible.
    None means there is no limit on processing time and the function will block until I/O
    produces actionable events.

Returns
-------

<a id="objects.rabbitmq.Connection.run"></a>

#### run

```python
def run(prefetch_count=1, timeout=None)
```

Run the Connection object by connecting to RabbitMQ and then
starting the IOLoop to block and allow the SelectConnection to operate.

<a id="objects.rabbitmq.Connection.stop"></a>

#### stop

```python
def stop()
```

Cleanly shutdown the connection to RabbitMQ by stopping the Connection object
with RabbitMQ. When RabbitMQ confirms the cancellation, on_cancelok
will be invoked by pika, which will then closing the channel and
connection. The IOLoop is started again because this method is invoked
when CTRL-C is pressed raising a KeyboardInterrupt exception. This
exception stops the IOLoop which needs to be running for pika to
communicate with RabbitMQ. All of the commands issued prior to starting
the IOLoop will be buffered but not processed.

<a id="objects.rabbitmq.Connection.call_later"></a>

#### call\_later

```python
def call_later(seconds, function)
```

Adds a callback to the IO loop.

Parameters
----------
seconds : int
    Number of seconds to wait before calling function.
function : function
    The callback function to call when seconds have passed.

Returns
-------
str
    The timeout ID handle.

<a id="objects.rabbitmq.Connection.cancel_call_later"></a>

#### cancel\_call\_later

```python
def cancel_call_later(timeout_id)
```

Cancel the call_later for the provided timeout_id.

Parameters
----------
timeout_id : str
    The timeout ID handle.

<a id="objects.rabbitmq.Connection.call_later_threadsafe"></a>

#### call\_later\_threadsafe

```python
def call_later_threadsafe(function)
```

Requests a call to the given function as soon as possible in the context of this
connection's thread.

Parameters
----------
function : callable
    The callback method/function.

<a id="objects.rabbitmq.Connection.is_open"></a>

#### is\_open

```python
@property
def is_open()
```

Returns a boolean reporting the current connection state.

Returns
-------
bool
    The current connection state.

<a id="objects.rabbitmq.Connection.is_closed"></a>

#### is\_closed

```python
@property
def is_closed()
```

Returns a boolean reporting the current connection state.

Returns
-------
bool
    The current connection state.

<a id="objects.rabbitmq.Connection.is_closing"></a>

#### is\_closing

```python
@property
def is_closing()
```

Returns a boolean reporting the current connection state.

Returns
-------
bool
    The current connection state.

