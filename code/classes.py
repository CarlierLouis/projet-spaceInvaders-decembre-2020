from tkinter import *


class Entite:

    def __init__(self, x, y, vie, pas, img, canvas):
        self.x = x
        self.y = y
        self.vie = vie
        self.pas = pas
        self.img = img
        self.tir = ''
        canvas.move(self.img, x, y)

    def tir(self, pas, canvas):
        self.tir = Tir(self.x, self.y, pas, canvas)


class Joueur(Entite):

    def __init__(self, x, y, vie, pas, img, canvas):
        Entite.__init__(self, x, y, vie, pas, img, canvas)
        self.scores = 0
        self.nom = ""
        self.argents = 0

    def deplacement(self, canvas):
        if 956.5 >= self.x >= 56.5:
            canvas.move(self.img, 10 * self.pas, 0)
            self.x = self.x + (10 * self.pas)
        if self.x < 56.5:
            canvas.move(self.img, 10 * -self.pas, 0)
            self.x = 56.5
        if self.x > 956.5:
            canvas.move(self.img, 10 * -self.pas, 0)
            self.x = 956.5
        return canvas


class Alien(Entite):
    def __init__(self, x, y, vie, pas, img, canvas):
        Entite.__init__(self, x, y, vie, pas, img, canvas)
        self.detruit = False

    def deplacement(self, canvas, x, y):
        self.x += x * self.pas
        self.y += y
        canvas.move(self.img, x * self.pas, y)
        return canvas


class Tir:

    def __init__(self, x, y, pas, canvas):
        self.x = x
        self.y = y
        self.pas = pas
        self.image = canvas.create_rectangle(0, 0, -10, -20, fill='Purple')
        canvas.move(self.image, x, y)

    def deplacement(self):
        return 'lol'

    def colission(self):
        pass
