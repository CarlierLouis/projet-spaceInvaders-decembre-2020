import mysql
from mysql import connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='infos')
cursor = cnx.cursor()


def create_Table_Profils():
    cursor.execute("CREATE TABLE Profils (id int primary key not null auto_increment,"
                   "pseudo varchar(255), xp int(255), money int(255))")


def fill_Table_Profils():
    sql = "INSERT INTO Profils (pseudo, xp, money) VALUES (%s, %s, %s)"
    value = ("test", 12, 123)
    cursor.execute(sql, value)
    cnx.commit()


