import tkinter as tk
class Defaillance :
    def __init__(self, message) :
        self.message = message

    def afficher_message(self):
        root = tk.Tk()
        label = tk.Label(root,text=self.message)
