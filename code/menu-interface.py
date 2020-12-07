from tkinter import *
from tkinter import messagebox

from main import jouer
from database import recuperer_infos_joueurs


# Affichage des scores (fenêtre des scores)
def fenetre_score():
    window_score = Tk()

    window_score.title("Scores")
    window_score.geometry("1200x400")
    window_score.minsize(480, 360)
    window_score.iconbitmap("score.ico")
    window_score.config(background='#660000')

    frame_scores = Frame(window_score, bg='#660000')
    frame_scores_retour = Frame(window_score, bg='#660000')

    label_scores = Label(window_score, text="Scores", font=("Arial", 35), bg='#660000', fg='white')
    label2_scores = Label(window_score, text="{Pseudo, xp, argent}\n", font=("Arial", 15), bg='#660000', fg='black')
    label3_scores = Label(frame_scores, text=recuperer_infos_joueurs(), font=("Arial", 15), bg='#660000', fg='white')
    label_scores_retour = Button(frame_scores_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                 command=window_score.destroy)

    label_scores.pack()
    label2_scores.pack()
    label3_scores.pack()
    label_scores_retour.pack()

    frame_scores.pack()
    frame_scores_retour.pack(pady=25, fill=X, side=BOTTOM)

    window_score.mainloop()


# Affichage de la boutique (fenêtre de la boutique)
def fenetre_boutique():
    window_boutique = Tk()

    window_boutique.title("Boutique")
    window_boutique.geometry("500x500")
    window_boutique.minsize(480, 360)
    window_boutique.iconbitmap("boutique.ico")
    window_boutique.config(background='#660000')

    frame_boutique = Frame(window_boutique, bg='#660000')
    frame_boutique_retour = Frame(window_boutique, bg='#660000')

    label_boutique = Label(window_boutique, text="Boutique", font=("Arial", 35), bg='#660000', fg='white')
    label2_boutique = Label(frame_boutique, text="", font=("Arial", 15), bg='#660000', fg='white')
    label_boutique_retour = Button(frame_boutique_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                   command=window_boutique.destroy)
    label_boutique.pack()
    label2_boutique.pack()
    label_boutique_retour.pack()

    frame_boutique.pack()
    frame_boutique_retour.pack(pady=25, fill=X, side=BOTTOM)

    window_boutique.mainloop()


# M E N U
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
bouton_score = Button(frame, text="Scores", font=("Arial", 25), bg='white', fg='#121517', bd="10", relief="ridge",
                      command=fenetre_score)
bouton_boutique = Button(frame, text="Boutique", font=("Arial", 25), bg='white', fg='#121517', bd="10", relief="ridge",
                         comman=fenetre_boutique)
bouton_jouer.pack(pady=25, fill=X)
bouton_score.pack(pady=25, fill=X)
bouton_boutique.pack(pady=25, fill=X)

# Ajout de la frame
frame.pack(expand=YES)

# Affichage
window.mainloop()
