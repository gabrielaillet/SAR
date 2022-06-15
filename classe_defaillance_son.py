import numpy as np
from scipy.io import wavfile
import sounddevice as sd
from math import sin, pi
import simpleaudio as sa
import tkinter as tk
import tkinter.ttk as ttk


def alarm():
    read_sond('alarm')

def read_sond(name,played = True):
    sa.stop_all()
    c, a = wavfile.read(name)
    if played:
        v = sd.play(a, c, loop=True, blocking=False)
    return c,a

class classe_defaillance_son:
    def __init__(self,son):
        self.son = son
        read_sond(son)

    def son_normal(self):
        read_sond(self.son)

    def son_sinus(self):
        a,b = read_sond(self.son,played = False)
        for i in range(len(b)):
            b[i] = b[i] * sin(1/2 * pi * i/a)
        sd.play(b, a, loop=True,blocking=False)

    def son_sature(self):
        a,b = read_sond(self.son,played = False)
        b = b * 10
        sd.play(b, a, loop=True,blocking=False)

    def son_null(self):
        sd.stop()

def son_sature(son):
    son.son_sature()
def son_sinus(son):
    son.son_sinus()
def son_null(son):
    son.son_null()
def son_normal(son):
    son.son_normal()

def son():
    fenetre = tk.Tk()
    son = classe_defaillance_son('musique.wav')
    label = ttk.Label(fenetre, text="Classe défaillance son")
    fenetre.geometry("200x200")

    bouton5 = ttk.Button(fenetre, text="son_normal", command=lambda: son_normal(son))
    bouton = ttk.Button(fenetre, text="son_sature",command= lambda: son_sature(son))
    bouton2 = ttk.Button(fenetre, text="son_sinus", command=lambda: son_sinus(son))
    bouton3 = ttk.Button(fenetre, text="son_stop", command= lambda: son_null(son))
    bouton4 = ttk.Button(fenetre, text="alarm not playing", command=lambda: son_null(son))

    label.pack()
    bouton5.pack()
    bouton.pack()
    bouton2.pack()
    bouton3.pack()
    bouton4.pack()

    fenetre.mainloop()




