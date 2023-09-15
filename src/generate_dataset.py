from .utils import generate_room_dim, load_config


def generate_dataset():
    config = load_config("config.yaml")
    width, height = generate_room_dim(config)
    print(width, height)
