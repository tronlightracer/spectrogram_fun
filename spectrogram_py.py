import librosa
import librosa.display
from matplotlib import pyplot as plt
import os
import numpy as np

path1 = "Aether & Enzalla - Elysia's Heart [FIN].wav"
# x, sr = librosa.load(path1)
x1, sr1 = librosa.load(librosa.ex("trumpet"))
# D = librosa.stft(x)  # STFT of y
D1 = librosa.stft(x1)
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S1_db = librosa.amplitude_to_db(np.abs(D1), ref=np.max)

plt.figure()
# librosa.display.specshow(S_db)
librosa.display.specshow(S1_db)
plt.colorbar()