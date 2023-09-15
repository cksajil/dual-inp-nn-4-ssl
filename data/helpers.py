import numpy as np


def generate_room_dim():
    """
    Generate room dimensions (width & height) randomly
    in the close interval [3, 6]
    """
    width, height = np.random.uniform(low=3, high=6, size=2)
    return width, height
