from pyo import *
import time
import os

def generate_music(weather):
    s = Server().boot()
    s.start()

    # Save path
    output_path = "static/audio/generated_track.wav"
    if os.path.exists(output_path):
        os.remove(output_path)

    # Recorder setup
    rec = Record(Input(), filename=output_path, fileformat=0)
    rec.start()

    # Ambient logic
    if "Rain" in weather:
        freq = 220
        texture = Noise(mul=0.05).mix(2).out()
    elif "Haze" in weather:
        freq = 330
        texture = Sine(freq=330, mul=0.1).out()
    else:
        freq = 440
        texture = Sine(freq=440, mul=0.2).out()

    pad = Sine(freq=freq, mul=0.2).out()
    time.sleep(10)

    rec.stop()
    pad.stop()
    texture.stop()
    s.stop()
