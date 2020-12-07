from tkinter import *

from main import jouer
from database import recuperer_infos_joueurs
from database import recuperer_pseudos_joueurs

# Choix du profils
window_profils = Tk()

# Personnalisation de la fenêtre
window_profils.title("Connexion")
window_profils.geometry("1080x720")
window_profils.minsize(480, 360)
window_profils.iconbitmap("logo.ico")
window_profils.config(background='#121517')

# Titre
label_titre_profils = Label(window_profils, text="Choississez votre profil\n", font=("Arial", 40), bg='#121517', fg='white')
label_titre_profils.pack()

# Menu déroulant
listeOptions = recuperer_pseudos_joueurs()
v = StringVar()
v.set(listeOptions[0])
menu_deroulant = OptionMenu(window_profils, v, *listeOptions)
menu_deroulant.pack()

# Affichage
window_profils.mainloop()


# M E N U
def fenetre_menu():
    # Création de la fenêtre
    window_menu = Tk()

    # Personnalisation de la fenêtre
    window_menu.title("Space Invaders")
    window_menu.geometry("1080x720")
    window_menu.minsize(480, 360)
    window_menu.iconbitmap("logo.ico")
    window_menu.config(background='#121517')

    # Création de la frame
    frame = Frame(window_menu, bg='#121517')

    # Titre
    label_titre = Label(window_menu, text="Space Invaders", font=("Arial", 40), bg='#121517', fg='white')
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
    window_menu.mainloop()


# Affichage des SCORES (fenêtre des scores)
def fenetre_score():
    # Création de la fenêtre
    window_scores = Tk()

    # Personnalisation de la fenêtre
    window_scores.title("Scores")
    window_scores.geometry("1200x400")
    window_scores.minsize(480, 360)
    window_scores.iconbitmap("score.ico")
    window_scores.config(background='#660000')

    # Création des frames
    frame_scores = Frame(window_scores, bg='#660000')
    frame_scores_retour = Frame(window_scores, bg='#660000')

    # Ajout des textes et boutons
    label_scores = Label(window_scores, text="Scores", font=("Arial", 35), bg='#660000', fg='white')
    label2_scores = Label(window_scores, text="{Pseudo, xp, argent}\n", font=("Arial", 15), bg='#660000', fg='black')
    label3_scores = Label(frame_scores, text=recuperer_infos_joueurs(), font=("Arial", 15), bg='#660000', fg='white')
    bouton_scores_retour = Button(frame_scores_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                  command=window_scores.destroy)

    label_scores.pack()
    label2_scores.pack()
    label3_scores.pack()
    bouton_scores_retour.pack()

    # Ajout des frames
    frame_scores.pack()
    frame_scores_retour.pack(pady=25, fill=X, side=BOTTOM)

    # Affichage
    window_scores.mainloop()


# Affichage de la BOUTIQUE (fenêtre de la boutique)
def fenetre_boutique():
    # Création de la fenêtre
    window_boutique = Tk()

    # Personnalisation de la fenêtre
    window_boutique.title("Boutique")
    window_boutique.geometry("500x500")
    window_boutique.minsize(480, 360)
    window_boutique.iconbitmap("boutique.ico")
    window_boutique.config(background='#660000')

    # Création des frames
    frame_boutique = Frame(window_boutique, bg='#660000')
    frame_boutique_retour = Frame(window_boutique, bg='#660000')

    # Ajout des textes et boutons
    label_boutique = Label(window_boutique, text="Boutique", font=("Arial", 35), bg='#660000', fg='white')
    label2_boutique = Label(frame_boutique, text="", font=("Arial", 15), bg='#660000', fg='white')
    bouton_boutique_retour = Button(frame_boutique_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                    command=window_boutique.destroy)
    label_boutique.pack()
    label2_boutique.pack()
    bouton_boutique_retour.pack()

    # Ajout des frames
    frame_boutique.pack()
    frame_boutique_retour.pack(pady=25, fill=X, side=BOTTOM)

    # Affichage
    window_boutique.mainloop()
