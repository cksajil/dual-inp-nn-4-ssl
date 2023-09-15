# from utils import generate_white_noise
# from utils import compute_stft
# from utils import load_config
# import pyroomacoustics as pra
# import numpy as np

# x = generate_white_noise()
# freq, time, spectrum = compute_stft(x, Fs=8000)


# rt60 = 0.5
# room_dim = [9, 7.5, 3.5]
# e_absorption, max_order = pra.inverse_sabine(rt60, room_dim)
# room = pra.ShoeBox(room_dim, fs=16000, materials=pra.Material(e_absorption))
# room.add_source([2.5, 3.73, 1.76])


# mic_locs = np.c_[[6.3, 4.87, 1.2]]
# room.add_microphone_array(mic_locs)
# room.compute_rir()
# print(room.rir[0][0])

# config = load_config("config.yaml")

# print(config["num_mics"])
# print(config["num_sources"])
