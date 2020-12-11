import classes
from tkinter import *


def clavier(event):
    touche = event.keysym
    global canvas
    if touche == "Right":
        ship.pas = 1
        canvas = ship.deplacement(canvas)

    elif touche == "Left":
        ship.pas = -1
        canvas = ship.deplacement(canvas)

    elif touche == "space":
        try:
            ship.tir(-1, canvas)
        except:
            pass


def deplacement_alien(aliens):
    global canvas
    for i in range(len(aliens)):
        if aliens[i].x >= 956.5:
            for j in range(len(aliens)):
                aliens[j].pas = -1
                aliens[j].deplacement(canvas, 0, 5)
        elif aliens[i].x <= 56.5:
            for j in range(len(aliens)):
                aliens[j].pas = 1
                aliens[j].deplacement(canvas, 0, 5)
        canvas = aliens[i].deplacement(canvas, 0.5, 0)

    canvas.after(5, deplacement_alien, aliens)


fenetre = Tk()
fenetre['background'] = 'black'
fenetre.minsize(1000, 500)
fenetre.maxsize(1000, 500)
canvas = Canvas(fenetre, width=1000, height=500)
canvas.config(bg='black')
canvas.pack()

# img_ship = canvas.create_image(-33, -28, anchor=NW, image=PhotoImage(file="ship.gif"))
ship = classes.Joueur(516.5, 495, 1, 5, canvas.create_rectangle(0, 0, -33, -28, fill='white'), canvas)
aliens = []

y = 0
x = 106.5
for i in range(50):
    x += 50
    if i % 10 == 0:
        y += 30
        x = 106.5
    aliens.append(classes.Alien(x, y, 1, 1, canvas.create_rectangle(0, 0, -33, -28, fill='Red'), canvas))

deplacement_alien(aliens)
fenetre.bind("<Key>", clavier)
fenetre.mainloop()
