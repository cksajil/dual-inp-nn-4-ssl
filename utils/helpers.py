import yaml
import requests
from os.path import join


def load_config(config_name):
    """
    A function to load and return config file in YAML format
    """
    CONFIG_PATH = "./config/"
    with open(join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config


config = load_config("config.yaml")


def retrieve_file_list():
    doi = config["project_doi"]
    response = requests.get(f"https://zenodo.org/api/records/{doi}")
    data = response.json()
    files = data["files"]
    if len(files) == 0:
        print("No model files found.")
    else:
        formats = ".csv"
        model_files = [file for file in files if file["key"].endswith(formats)]
        essentials = {}
        for item in model_files:
            file_url = item["links"]["self"]
            model_filename = item["key"]
            essentials[model_filename] = file_url
    return essentials
