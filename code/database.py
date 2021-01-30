import mysql
from mysql import connector


cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='infos')
cursor = cnx.cursor()


def creation_table_Profils():
    """
    Fonction de création de la table des profils dans la db

    PRE:-
    POST:-
    """
    cursor.execute("CREATE TABLE Profils (id int primary key not null auto_increment,"
                   "pseudo varchar(255), xp int(255), argent int(255))")


def remplir_table_Profils(pseudo, xp, argent):
    """
    Fonction pour ajouter de nouveau joueur dans la db

    PRE:
        type(pseudo) == str
        type(xp) == int
        type(argent) == int
    POST:-
    """
    sql = "INSERT INTO Profils (pseudo, xp, argent) VALUES (%s, %s, %s)"
    value = (pseudo, xp, argent)
    cursor.execute(sql, value)
    cnx.commit()


def recuperer_infos_joueurs():
    """
    Fonction récupérant les données des joueurs présentes dans la db

    PRE:-
    POST: return list
    """
    infos_joueurs = []
    cursor.execute("SELECT pseudo, xp, argent FROM Profils")
    for i in cursor.fetchall():
        infos_joueurs.append(i)
    # Transformtion du tuple en liste
    liste = [x for elem in infos_joueurs for x in elem]
    j = 0
    liste2 = []
    # Transformation de la liste simple en liste avec sous-listes
    while j < len(liste) - 2:
        liste3 = [liste[j], liste[j + 1], liste[j + 2]]
        liste2.append(liste3)
        j += 3
    # Tri décroissant en fonction de l'xp du joueur
    liste_finale = sorted(liste2, key=lambda a: a[1], reverse=False)
    return liste_finale


def recuperer_pseudos_joueurs():
    """
    Fonction de récupération des pseudos des joueurs présents dans la db

    PRE:-
    POST: return list
    """
    infos_joueurs = []
    cursor.execute("SELECT pseudo, xp, argent FROM Profils")
    for i in cursor.fetchall():
        infos_joueurs.append(i)
    # Transformtion du tuple en liste
    liste = [x for elem in infos_joueurs for x in elem]
    j = 0
    liste2 = []
    pseudos = []
    # Transformation de la liste simple en liste avec sous-listes
    while j < len(liste) - 2:
        liste3 = [liste[j], liste[j + 1], liste[j + 2]]
        liste2.append(liste3)
        j += 3
    for i in liste2:
        pseudos.append(i[0])
    return pseudos


def ajout_xp(xp, argent, pseudo):
    """
    Fonction d'ajout d'xp et d'argent dans la db en fonction du pseudo

    PRE:
        type(pseudo) == str
        type(xp) == int
        type(argent) == int
    POST:-
    """
    sql = "UPDATE Profils SET xp = xp + %s, argent = argent + %s WHERE pseudo = %s"
    value = (xp, argent, pseudo)
    cursor.execute(sql, value)
    cnx.commit()
