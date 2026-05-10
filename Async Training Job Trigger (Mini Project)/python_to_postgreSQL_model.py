from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime

class ExperimentsBase (SQLModel):
    project_name : str
    problem_type : str
    dataset_size  : int 
    backbone : str
    activation : str
    optimizer : str | None = Field(default=None)
    batch_size : int | None = Field(default=None)
    learning_rate : float | None = Field(default=None)
    pretrained_weights : str | None = Field(default=None)
    augmentation : str | None = Field(default=None)
    val_accuracy : float
    val_loss : float
    epochs : int
    time_stamp : datetime = Field(default_factory=datetime.now)

class Experiment (ExperimentsBase, table=True):
    id : int | None = Field(default=None, primary_key=True)

class Experiment_insert(ExperimentsBase):
    pass

class Experiment_update(ExperimentsBase):
    pass


