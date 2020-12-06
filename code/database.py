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
    return infos_joueurs
