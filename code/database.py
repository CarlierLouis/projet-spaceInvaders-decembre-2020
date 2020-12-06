import mysql
from mysql import connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='infos')
cursor = cnx.cursor()

infos_joueurs = []


def creation_table_Profils():
    cursor.execute("CREATE TABLE Profils (id int primary key not null auto_increment,"
                   "pseudo varchar(255), xp int(255), argent int(255))")


def remplir_table_Profils():
    sql = "INSERT INTO Profils (pseudo, xp, argent) VALUES (%s, %s, %s)"
    value = ("Diego", 108, 34)
    cursor.execute(sql, value)
    cnx.commit()


def recuperer_infos_joueurs():
    cursor.execute("SELECT pseudo, xp, argent FROM Profils")
    for i in cursor.fetchall():
        infos_joueurs.append(i)
    liste = [x for elem in infos_joueurs for x in elem]
    j = 0
    liste2 = []
    while j < len(liste) - 2:
        liste3 = [liste[j], liste[j + 1], liste[j + 2]]
        liste2.append(liste3)
        j += 3
    return liste2

