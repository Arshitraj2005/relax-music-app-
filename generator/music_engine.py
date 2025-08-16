import numpy as np
from scipy.io.wavfile import write
import os

def generate_music():
    os.makedirs("static/audio", exist_ok=True)
    sample_rate = 44100
    duration = 10
    freq = 440.0

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * freq * t)
    audio = np.int16(waveform * 32767)

    write("static/audio/generated_track.wav", sample_rate, audio)
