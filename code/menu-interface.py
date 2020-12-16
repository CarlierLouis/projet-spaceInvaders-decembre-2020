from tkinter import *
from tkinter import messagebox

from database import recuperer_infos_joueurs
from database import recuperer_pseudos_joueurs
from database import remplir_table_Profils


# Fonstion qui appelle le script du jeu
def jouer():
    from main import main
    main(recup_profil)


# Choix du profil

# Création de la fenêtre
window_profils = Tk()

# Personnalisation de la fenêtre
window_profils.title("Connexion")
window_profils.geometry("720x600")
window_profils.minsize(480, 360)
window_profils.iconbitmap("images/logo.ico")
window_profils.config(background='#121517')

# Création de la frame
frame_profls = Frame(window_profils, bg="#121517")

# Titre
label_titre_profils = Label(window_profils, text="Choississez votre profil\n", font=("Arial", 40), bg='#121517',
                            fg='white')
label_titre_profils.pack()

# Menu déroulant
listeOptions = recuperer_pseudos_joueurs()
v = StringVar(window_profils)
v.set(listeOptions[0])
menu_deroulant = OptionMenu(window_profils, v, *listeOptions)
menu_deroulant.pack()

# Saut de ligne
label_saut = Label(frame_profls, text="\n", font=("Arial", 15), bg='#121517', fg='white')
label_saut.pack()

# Bouton validation
validation = Button(frame_profls, text="Valider", font=("Arial", 15), bg='white', fg='black',
                    command=window_profils.destroy)
validation.pack()

# Titre ajout nouveau joueur
label_nouveau = Label(frame_profls, text="\n\n______________________\n\n\n\n"
                                         " Vous êtes un nouveau joueur, ajoutez votre pseudo ici : \n",
                      font=("Arial", 15), bg='#121517', fg='white')
label_nouveau.pack()


# Entry du nouveau pseudo
def recup_nouveau_pseudo():
    recup_nouveau = entry_pseudo.get()
    # Condition pour que le nouveau pseudo soit accepté
    if recup_nouveau in recuperer_pseudos_joueurs() or recup_nouveau == "":
        messagebox.showinfo("erreur", "Le pseudo que vous avez choisi est déjà pris "
                                      "ou ne correspond pas aux normes.")
    elif " " in recup_nouveau:
        messagebox.showinfo("erreur", "Le pseudo que vous avez choisi est déjà pris "
                                      "ou ne correspond pas aux normes.")
    elif len(recup_nouveau) < 3 or len(recup_nouveau) > 10:
        messagebox.showinfo("erreur", "Le pseudo que vous avez choisi est déjà pris "
                                      "ou ne correspond pas aux normes.")
    else:
        # Fonction (de database.py) qui ajoute le pseudo dans la db
        remplir_table_Profils(recup_nouveau, 0, 0)


entry_pseudo = Entry(frame_profls, font=("Arial", 13), fg="red")
entry_pseudo.pack()

# Bouton qui déclanche l'appel de la fonction pour remplir la db avec le  nouveau pseudo
bouton_recup = Button(frame_profls, text="Enregistrer le nouveau pseudo", font=("Arial", 10),
                      command=recup_nouveau_pseudo)
bouton_recup.pack()

# Commenataire ajout nouveau profil
commentaire_profil = Label(frame_profls,
                           text="\n\n\n Une fois votre nouveau pseudo enregistré,"
                                " veillez relancer le jeu afin de pouvoir selectionner votre nouveau profil",
                           font=("Arial", 10), bg="#121517", fg='red')
commentaire_profil.pack()

# Ajout de la frame
frame_profls.pack()

# Affichage
window_profils.mainloop()

# Mise en mémoire du profils sélecionné
recup_profil = v.get()
print(recup_profil)


# M E N U
def fenetre_menu():
    # Création de la fenêtre
    window_menu = Tk()

    # Personnalisation de la fenêtre
    window_menu.title("Space Invaders")
    window_menu.geometry("1080x720")
    window_menu.minsize(480, 360)
    window_menu.iconbitmap("images/logo.ico")
    window_menu.config(background='#121517')

    # Création de la frame
    frame_menu = Frame(window_menu, bg='#121517')

    # Titre
    label_titre = Label(window_menu, text="Space Invaders", font=("Arial", 40), bg='#121517', fg='white')
    label_titre.pack()

    # Ajout des boutons
    bouton_jouer = Button(frame_menu, text="Jouer", font=("Arial", 25), bg='white', fg='#121517', bd="10",
                          relief="ridge", command=jouer)
    bouton_score = Button(frame_menu, text="Scores", font=("Arial", 25), bg='white', fg='#121517', bd="10",
                          relief="ridge", command=fenetre_score)
    bouton_boutique = Button(frame_menu, text="Boutique", font=("Arial", 25), bg='white', fg='#121517', bd="10",
                             relief="ridge", command=fenetre_boutique)

    bouton_jouer.pack(pady=25, fill=X)
    bouton_score.pack(pady=25, fill=X)
    bouton_boutique.pack(pady=25, fill=X)

    # Ajout de la frame
    frame_menu.pack(expand=YES)

    # Affichage
    window_menu.mainloop()


# Affichage des SCORES (fenêtre des scores)
def fenetre_score():
    # Création de la fenêtre
    window_scores = Tk()

    # Personnalisation de la fenêtre
    window_scores.title("Scores")
    window_scores.geometry("800x500")
    window_scores.minsize(480, 360)
    window_scores.iconbitmap("images/score.ico")
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
    window_boutique.geometry("800x500")
    window_boutique.minsize(480, 360)
    window_boutique.iconbitmap("images/boutique.ico")
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


fenetre_menu()
