import numpy as np
from scipy.io import wavfile
import sounddevice as sd
from math import sin, pi
import simpleaudio as sa
import threading
from tkinter import ttk



class classe_defaillance_son:
    def __init__(self,son):
        self.son = son


    def son_sinus(self):
        sa.stop_all()
        a,b = wavfile.read(self.son)
        print(len(b))
        for i in range(len(b)):
            b[i] = b[i] * sin(1/2 * pi * i/a)
        wave_obj = sa.WaveObject(b)
        a = wave_obj.play()
        a.wait_done()

    def son_sature(self):
        sa.stop_all()
        a,b = wavfile.read(self.son)
        b = b * 10
        wave_obj = sa.WaveObject(b)
        a = wave_obj.play()
        a.wait_done()

    def son_null(self):
        sa.stop_all()

    def son_pas_fort(self):
        sa.stop_all()
        a, b = wavfile.read(self.son)
        b = b * 0.1
        wave_obj = sa.WaveObject(b)
        a = wave_obj.play()
        a.wait_done()


if __name__ == '__main__':
    print('q')

