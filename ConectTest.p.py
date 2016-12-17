# -*- coding: ISO-8859-2 -*-
import psycopg2
import sys


class ConnectPg:

    connection = None
    cur = None

    def __init__(self):
        try:
            self.connection = psycopg2.connect(database='postgres', user='postgres')
            self.cur = self.connection.cursor()  # define cursor

        except psycopg2.DatabaseError, e:
            print 'Error %s' % e  #Can not connect with Database;
            self.connection.close()
            sys.exit(1)

    def __del__(self):
            if self.connection:
                self.connection.close()
                print 'connection destroy'


class Player(ConnectPg):

    id = 0
    nick = ""
    name = ""
    surname = ""
    money = 1000
    db_con = None

    def __init__(self, player_id, player_nick, player_name, player_surname):
        self.db_con = ConnectPg()
        #self.conn = ConnectPg.__init__(self) .connection   #super constructor why?

        self.id = player_id
        self.nick = player_nick
        self.name = player_name
        self.surname = player_surname

    def insertPlayer(self):
        query = "INSERT INTO Players (id, nick, p_name, p_surname, money) VALUES (%s,%s,%s,%s,%s);"
        data = (self.id, self.nick, self.name, self.surname, self.money)

        self.db_con.cur.execute(query, data)
        self.db_con.connection.commit()

    def updatePlayer(self, id_update):
        query = "UPDATE Players SET (id, nick, p_name, p_surname, money) VALUES (%s,%s,%s,%s,%s) WHERE id = %s;"
        data = (self.id, self.nick, self.name, self.surname, self.money)

        self.db_con.cur.execute(query, data)
        self.db_con.connection.commit()

    def writeAllPlayers(self):
        self.db_con.cur.execute('SELECT * FROM players')
        for ver in self.db_con.cur:
            print ver

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"


def main():
    user1 = Player(1, "olo123", "Ola", "Bak")
    user1.insertPlayer()
    user1.writeAllPlayers()

main()


