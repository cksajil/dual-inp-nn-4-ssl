import numpy as np
from scipy.signal import stft


def generate_white_noise(mu=0, std=1, nsamples=1000):
    """
    Function to generate white gaussian noise of given
    mean, standard deviation, and number of samples
    """
    x = np.random.normal(mu, std, size=nsamples)
    return x


def compute_stft(x, Fs, N=1000):
    f, t, Zxx = stft(x, Fs, nperseg=N)
    return f, t, Zxx
