from Defaillance import Defaillance

class Defaillance_eclairage(Defaillance):
    def __init__(self, eclairage):
        self.eclairage = eclairage

    def changer_eclairage(self, couleur):
        self.eclairage.master['background'] = couleur

    def peu_eclairage(self):
        self.changer_eclairage('#FFFC9D')

    def pas_eclairage(self):
        self.changer_eclairage('#000000')

    def haut(self):
        self.changer_eclairage('#FEF82B')
        self.eclairage.master.after(500, self.bas)

    def bas(self):
        self.changer_eclairage('#FFFC9D')
        self.eclairage.master.after(500, self.haut)


