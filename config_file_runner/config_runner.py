# pip install pyyaml 

import yaml

with open("config.yaml","r") as f:
    config = yaml.safe_load(f)

keys = {"top":["project_name","problem_type"],"model":["backbone", "pretrained", "activation"], "augmentation":["horizontal_flip", "mixup", "cutout"],"training": ["optimizer", "learning_rate", "epochs","batch_size"]}

for key in keys["top"] :
    if key not in config:
        raise ValueError(f"Missing required field : {key}")

def validation(title):
    for key in keys[title]:
        if key not in config[title]:
            raise ValueError(f"Missing required field : {key}")   

validation("model")
validation("augmentation")
validation("training")

def print_section(title):
    line = "=" * len(title)
    print(f"\n{line}\n{title}\n{line}\n")
    
print_section("Project Summary")

print(f"Project name : {config["project_name"]}")
print(f"Problem type : {config["problem_type"]}")
print("\n")

print_section("Model")

print(f"backbone : {config["model"]["backbone"]}")
print(f"pretrained : {config["model"]["pretrained"]}")
print(f"activation : {config["model"]["activation"]}")
print("\n")

print_section("Augmentation")

print(f"horizontal_flip : {config["augmentation"]["horizontal_flip"]}")
print(f"mixup : {config["augmentation"]["mixup"]}")
print(f"cutout : {config["augmentation"]["cutout"]}")
print("\n")

print_section("Training")

print(f"optimizer : {config["training"]["optimizer"]}")
print(f"learning_rate : {config["training"]["learning_rate"]}")
print(f"epochs : {config["training"]["epochs"]}")
print(f"batch_size : {config["training"]["batch_size"]}")
print("\n")

