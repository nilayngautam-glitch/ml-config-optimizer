from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime

class ExperimentsBase (SQLModel):
    project_name : str
    problem_type : str
    dataset_size  : int 
    dataset_name : str
    seed : int | None = Field(default=None)
    backbone : str  | None = Field(default=None)
    activation : str 
    optimizer : str | None = Field(default=None)
    batch_normalization : bool | None = Field(default=None)
    regularization : str | None = Field(default=None)
    dropout : str | None = Field(default=None)
    batch_size : int | None = Field(default=None)
    learning_rate : float | None = Field(default=None)
    pretrained_weights : str | None = Field(default=None)
    augmentation : str | None = Field(default=None)
    freeze_strategy : str | None = Field(default=None)
    loss_function : str | None = Field(default=None)
    val_accuracy : float
    val_loss : float
    epochs : int
    iou : float | None = Field(default=None)
    f1_score : float | None = Field(default=None)
    mean_avg_precision : float | None = Field(default=None)
    auc_roc : float | None = Field(default=None)
    primary_metric : str = Field(default="val_accuracy")
    time_stamp : datetime = Field(default_factory=datetime.now)

class Experiment (ExperimentsBase, table=True):
    id : int | None = Field(default=None, primary_key=True)

class Experiment_insert(ExperimentsBase):
    pass

class Experiment_update(ExperimentsBase):
    pass


