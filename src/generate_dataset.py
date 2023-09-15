from .utils import generate_room_dim, load_config


def generate_dataset():
    config = load_config("config.yaml")
    widths, heights = generate_room_dim(config)
    return widths, heights
