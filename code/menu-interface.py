from tkinter import *
from tkinter import messagebox
from main import jouer

# Création de la fenêtre
window = Tk()

# Personnalisation de la fenêtre
window.title("Space Invaders")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#121517')

# Création de la frame (boîte)
frame = Frame(window, bg='#121517')

# Titre
label_titre = Label(window, text="Space Invaders", font=("Arial", 40), bg='#121517', fg='white')
label_titre.pack()

# Ajout des boutons
bouton_jouer = Button(frame, text="Jouer", font=("Arial", 25), bg='white', fg='#121517', bd="10", relief="ridge",
                      command=jouer)
bouton_score = Button(frame, text="Scores", font=("Arial", 25), bg='white', fg='#121517', bd="10", relief="ridge")
bouton_boutique = Button(frame, text="Boutique", font=("Arial", 25), bg='white', fg='#121517', bd="10", relief="ridge")
bouton_jouer.pack(pady=25, fill=X)
bouton_score.pack(pady=25, fill=X)
bouton_boutique.pack(pady=25, fill=X)

# Ajout de la frame
frame.pack(expand=YES)

# Affichage
window.mainloop()
