from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from database import recuperer_infos_joueurs
from database import recuperer_pseudos_joueurs
from database import remplir_table_Profils
from database import payement


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
    window_scores.geometry("600x360")
    window_scores.minsize(600, 360)
    window_scores.maxsize(600, 360)
    window_scores.iconbitmap("images/score.ico")
    window_scores.config(background='white')

    # Création des frames
    frame_scores = Frame(window_scores, bg='#660000')
    frame_scores_retour = Frame(window_scores, bg='white')

    # Ajout des textes et boutons
    '''
    label_scores = Label(window_scores, text="Scores", font=("Arial", 35), bg='#660000', fg='white')
    label2_scores = Label(window_scores, text="{Pseudo, xp, argent}\n", font=("Arial", 15), bg='#660000', fg='black')
    label3_scores = Label(frame_scores, text=recuperer_infos_joueurs(), font=("Arial", 15), bg='#660000', fg='white')
    bouton_scores_retour = Button(frame_scores_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                  command=window_scores.destroy)

    label_scores.pack()
    label2_scores.pack()
    label3_scores.pack()
    bouton_scores_retour.pack()'''

    # Ajout du tableau de scoring avec Treeview
    tree = ttk.Treeview(window_scores)
    tree["columns"] = ("one", "two")
    tree.column("#0", width=200, minwidth=200, stretch=FALSE)
    tree.column("one", width=200, minwidth=200, stretch=FALSE)
    tree.column("two", width=200, minwidth=200, stretch=FALSE)

    tree.heading("#0", text="Pseudo")
    tree.heading("one", text="xp")
    tree.heading("two", text="argent")

    for i in range(len(recuperer_infos_joueurs())):
        tree.insert("", 0, text=recuperer_infos_joueurs()[i][0], values=(recuperer_infos_joueurs()[i][1],
                                                                         recuperer_infos_joueurs()[i][2]))

    tree.pack()

    bouton_scores_retour = Button(frame_scores_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                  command=window_scores.destroy)

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
    def solde_joueur():
        for j in range(len(recuperer_infos_joueurs())):
            if recuperer_infos_joueurs()[j][0] == recup_profil:
                return recuperer_infos_joueurs()[j][2]
    window_boutique.title("Boutique")
    window_boutique.geometry("800x600")
    window_boutique.minsize(480, 360)
    window_boutique.iconbitmap("images/boutique.ico")
    window_boutique.config(background='#660000')

    # Création des frames
    frame_boutique = Frame(window_boutique, bg='#660000')
    frame_boutique_retour = Frame(window_boutique, bg='#660000')

    # Ajout des textes et boutons
    label_boutique = Label(window_boutique, text="Boutique", font=("Arial", 35), bg='#660000', fg='white')
    label_solde = Label(window_boutique, text="Votre solde: " + str(solde_joueur()), font=("Arial", 15), bg='#660000', fg='white')
    label2_boutique = Label(frame_boutique, text="", font=("Arial", 15), bg='#660000', fg='white')
    bouton_boutique_retour = Button(frame_boutique_retour, text="retour", font=("Arial", 15), bg='#660000', fg='white',
                                    command=window_boutique.destroy)
    label_boutique.pack()
    label_solde.pack()
    label2_boutique.pack()
    bouton_boutique_retour.pack()

    # Contenu de la boutique
    # Objet 1
    objet1 = LabelFrame(window_boutique, text="Objet 1", font=("Arial", 20), bg='#660000', padx=20, pady=20)
    objet1.pack(fill="both", expand="yes")
    Label(objet1, bg='#660000', font=("Arial", 15), text="Description objet 1 (prix: 50)").pack()

    def achat1():
        for i in range(len(recuperer_infos_joueurs())):
            if recuperer_infos_joueurs()[i][0] == recup_profil:
                if recuperer_infos_joueurs()[i][2] >= 50:
                    payement(50, recup_profil)
                    messagebox.showinfo("Boutique", "Achat bien effectué !")
                else:
                    messagebox.showinfo("erreur", "Votre solde est insufisant !")

    bouton_achat1 = Button(objet1, text="Acheter", command=achat1)
    bouton_achat1.pack(side=BOTTOM)

    # Objet 2
    objet2 = LabelFrame(window_boutique, text="Objet 2", font=("Arial", 20), bg='#660000', padx=20, pady=20)
    objet2.pack(fill="both", expand="yes")
    Label(objet2, bg='#660000', font=("Arial", 15), text="Description objet 1 (prix: 50)").pack()

    def achat2():
        for i in range(len(recuperer_infos_joueurs())):
            if recuperer_infos_joueurs()[i][0] == recup_profil:
                if recuperer_infos_joueurs()[i][2] >= 50:
                    payement(50, recup_profil)
                    messagebox.showinfo("Boutique", "Achat bien effectué !")
                else:
                    messagebox.showinfo("erreur", "Votre solde est insufisant !")

    bouton_achat2 = Button(objet2, text="Acheter", command=achat2)
    bouton_achat2.pack(side=BOTTOM)

    # Objet 3
    objet3 = LabelFrame(window_boutique, text="Objet 3", font=("Arial", 20), bg='#660000', padx=20, pady=20)
    objet3.pack(fill="both", expand="yes")
    Label(objet3, bg='#660000', font=("Arial", 15), text="Description objet 1 (prix: 50)").pack()

    def achat3():
        for i in range(len(recuperer_infos_joueurs())):
            if recuperer_infos_joueurs()[i][0] == recup_profil:
                if recuperer_infos_joueurs()[i][2] >= 50:
                    payement(50, recup_profil)
                    messagebox.showinfo("Boutique", "Achat bien effectué !")
                else:
                    messagebox.showinfo("erreur", "Votre solde est insufisant !")

    bouton_achat3 = Button(objet3, text="Acheter", command=achat3)
    bouton_achat3.pack(side=BOTTOM)

    # Ajout des frames
    frame_boutique.pack()
    frame_boutique_retour.pack(pady=25, fill=X, side=BOTTOM)

    # Affichage
    window_boutique.mainloop()


fenetre_menu()
