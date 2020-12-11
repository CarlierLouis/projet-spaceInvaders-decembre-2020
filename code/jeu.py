import classes
from tkinter import *


def clavier(event):
    touche = event.keysym

    if touche == "Right":
        global canvas
        ship.pas = 1
        canvas = ship.deplacement(canvas)

    elif touche == "Left":
        ship.pas = -1
        canvas = ship.deplacement(canvas)


def deplacement_alien(aliens):
    global canvas

    for i in range(len(aliens)):
        print(i)
        for j in range(len(aliens[i])):
            canvas = aliens[i][j].deplacement(canvas, 5, 0)

    canvas.after(1000, deplacement_alien, aliens)


fenetre = Tk()
fenetre['background'] = 'black'
fenetre.minsize(1000, 500)
fenetre.maxsize(1000, 500)

canvas = Canvas(fenetre, width=1000, height=500)
canvas.pack()

# img_ship = canvas.create_image(-33, -28, anchor=NW, image=PhotoImage(file="ship.gif"))
img_ship = canvas.create_rectangle(0, 0, -33, -28, fill='Black')
ship = classes.Joueur(516.5, 495, 1, 5, img_ship, canvas)
aliens_canvas = [[0] * 10] * 5
aliens = [[0] * 10] * 5

y = 0

for i in range(len(aliens)):
    y += 30
    x = 106.5
    for j in range(len(aliens[i])):
        x += 50
        aliens_canvas[i][j] = canvas.create_rectangle(0, 0, -33, -28, fill='Red')
        aliens[i][j] = classes.Alien(x, y, 1, 1, aliens_canvas[i][j], canvas)
print(aliens)
deplacement_alien(aliens)
fenetre.bind("<Key>", clavier)
fenetre.mainloop()
