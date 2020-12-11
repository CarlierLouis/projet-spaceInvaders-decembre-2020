from tkinter import *


class Entite:

    def __init__(self, x, y, vie, pas, img, canvas):
        self.x = x
        self.y = y
        self.vie = vie
        self.pas = pas
        self.img = img
        canvas.move(self.img, x, y)

    def tir(self):
        self.tir = Tir()


class Joueur(Entite):

    def __init__(self, x, y, vie, pas, img, canvas):
        Entite.__init__(self, x, y, vie, pas, img, canvas)
        self.scores = 0
        self.nom = ""
        self.argents = 0

    def deplacement(self, canvas):
        if 900 >= self.x >= 100:
            canvas.move(self.img, 10 * self.pas, 0)
            self.x = self.x + (10 * self.pas)
        if self.x < 100:
            canvas.move(self.img, 10 * -self.pas, 0)
            self.x = 106.5
        if self.x > 900:
            canvas.move(self.img, 10 * -self.pas, 0)
            self.x = 896.5
        return canvas


class Alien(Entite):
    def __init__(self, x, y, vie, pas, img, canvas):
        Entite.__init__(self, x, y, vie, pas, img, canvas)

    def deplacement(self, canvas, x, y):
        self.x += x
        self.y += y
        canvas.move(self.img, x*self.pas, y)
        return canvas


class Tir:

    def __init__(self, x, y, pas, image):
        self.x = x
        self.y = y
        self.pas = pas
        self.image = image

    def deplacement(self):
        pass

    def colission(self):
        pass
