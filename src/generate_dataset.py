import numpy as np
from .utils import generate_room_dim, load_config


def generate_dataset():
    dataset = {}
    config = load_config("config.yaml")
    widths, heights = generate_room_dim(config)
    N = config["num_data_points"]
    rt60s = np.random.uniform(low=0.25, high=0.7, size=N)
    dataset["Widths"] = widths
    dataset["Heights"] = heights
    dataset["RT60s"] = rt60s
    return dataset
