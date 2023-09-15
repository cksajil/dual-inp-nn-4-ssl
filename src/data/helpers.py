import numpy as np


def generate_room_dim(config):
    """
    Generate room dimensions (width & height) randomly
    in the close interval [3, 6]
    """
    offset = config["source_offset"]
    width, height = np.random.uniform(low=3, high=6, size=2)
    return width - offset, height - offset
