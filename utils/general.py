import numpy as np


def generate_white_noise(mu=0, std=1, nsamples=1000):
    """
    Function to generate white gaussian noise of given
    mean, standard deviation, and number of samples
    """
    x = np.random.normal(mu, std, size=nsamples)
    return x
