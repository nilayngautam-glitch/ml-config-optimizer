# Think about what it needs to do in plain words — receive a config and results from the user, create an ExperimentLogger object, log the experiment, save it to JSON, and return a success message.

from fastapi import FastAPI, HTTPException
from Experiments_api_models import Experiment_input
from Experiment_logger import Experiment_logger

app = FastAPI()

@app.post("/experiments")
async def recieve(exp_input : Experiment_input):
   filepath = r"D:\ML DL Advisor project\Phase 2 (Web Backend — FastAPI, Databases & Async Jobs)/experiments.json"

   logger = Experiment_logger(filepath)

   logger.load_from_json() 

   logger.log_experiment(exp_input.config.model_dump(), exp_input.result.model_dump())
   logger.save_in_json()
   
   return {"message" : "Successfully loaded the experiment"}

@app.get("/experiments")
async def load():
      filepath = r"D:\ML DL Advisor project\Phase 2 (Web Backend — FastAPI, Databases & Async Jobs)/experiments.json"

      logger = Experiment_logger(filepath)

      exp = logger.load_from_json()

      return exp

@app.get("/experiments/best")
async def best():
     filepath = r"D:\ML DL Advisor project\Phase 2 (Web Backend — FastAPI, Databases & Async Jobs)/experiments.json"

     logger = Experiment_logger(filepath)

     best_exp = logger.load_from_json() 
     best_exp = logger.best_experiment()

     return best_exp