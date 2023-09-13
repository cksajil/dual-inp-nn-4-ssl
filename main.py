from utils import generate_white_noise
from utils import compute_stft

x = generate_white_noise()
freq, time, spectrum = compute_stft(x, Fs=8000)
print(spectrum)
