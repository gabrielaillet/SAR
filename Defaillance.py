import tkinter as tk
class Defaillance :
    def __init__(self, message) :
        self.message = message
        self.fenetre = tk.Tk()
    def afficher_message(self):
        label = tk.Label(self.fenetre,text=self.message)
        label.pack()
        self.label = label
    def enlever_message(self):
        self.label.destroy()
    def new_message(self):
        self.enlever_message()
        self.afficher_message()