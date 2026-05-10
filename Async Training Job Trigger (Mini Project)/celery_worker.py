from celery import Celery
import time


app = Celery("celery_worker",broker="redis://localhost:6379/0")

@app.task
def run_train_job(config_dict:dict):
    time.sleep(10) # Training simulation
    return {
            "val_accuracy": config_dict["val_accuracy"],
            "val_loss": config_dict["val_loss"],
            "epochs": config_dict["epochs"],
            "status": "completed"
           }