from helpers import generate_room_dim
from src.utils import load_config


config = load_config("config.yaml")

width, height = generate_room_dim(config)
print(width, height)
