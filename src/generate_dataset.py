from utils.general import generate_room_dim
from utils.helpers import load_config


def generate_dataset():
    config = load_config("config.yaml")
    width, height = generate_room_dim(config)
    print(width, height)


if __name__ == "__main__":
    generate_dataset()
