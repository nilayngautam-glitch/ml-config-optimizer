from pydantic import BaseModel

class Config(BaseModel):
    backbone : str
    activation : str
    mixup : bool

class Result(BaseModel):
    val_accuracy : float
    val_loss : float
    epochs : int

class Experiment_input(BaseModel):

    config : Config
    result : Result