from datetime import datetime
import json

class Experiment_logger:
    def __init__(self,filepath):
        self.filepath = filepath
        self.experiments = []
    
    def log_experiment (self,config_dict,result_dict):
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

        final = {"config":config_dict, 
                 "results":result_dict, 
                 "current_timestamp":timestamp_str}
        
        self.experiments.append(final)

    def save_in_json (self):
        with open(self.filepath,'w') as f:
            json.dump(self.experiments,f)

    def load_from_json (self):
        try:
            with open(self.filepath,"r") as f:
                self.experiments= json.load(f)
        except FileNotFoundError:
            print(f"No file at {self.filepath}")
        
    def best_experiment(self):
        if (len(self.experiments)>0):  
            maximum = self.experiments[0]["results"]["val_accuracy"]
            for exp in self.experiments:
                if (exp["results"]["val_accuracy"]>=maximum):
                    maximum = exp["results"]["val_accuracy"]
                    best = exp

            return best
    
        else:
            print("Experiments list is empty")
            return None
        

filepath = r"D:\ML DL Advisor project\Phase 1 (Python Engineering & Software Fundamentals)\Experiment Logger (Mini Project)\experiments.json"

config1 = { "backbone" : "resnet50", "activation" : "relu", "mixup" : False }
result1 = { "val_accuracy"  : 0.82, "val_loss" : 0.45, "epochs" : 5}

config2 = { "backbone" : "efficientnet", "activation" : "gelu", "mixup" : True }
result2 = { "val_accuracy"  : 0.91, "val_loss" : 0.28, "epochs" : 5}

config3 = { "backbone" : "resnet50", "activation" : "swish", "mixup" : False }
result3 = { "val_accuracy"  : 0.87, "val_loss" : 0.35, "epochs" : 5}

logger = Experiment_logger(filepath)

logger.log_experiment(config1,result1)
logger.log_experiment(config2,result2)
logger.log_experiment(config3,result3)

logger.save_in_json()
logger.load_from_json()

print(logger.best_experiment())