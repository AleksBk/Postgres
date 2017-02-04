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

    def insert(self, data): # odrazu mozna krotke przeslac
        query = "INSERT INTO Players (id, nick, p_name, p_surname, money) VALUES (%s,%s,%s,%s,%s);"

        self.cur.execute(query, data)
        self.connection.commit()

    def update(self, data):
        query = "UPDATE Players SET (id, nick, p_name, p_surname, money) VALUES (%s,%s,%s,%s,%s) WHERE id = %s;"

        self.cur.execute(query, data)
        self.connection.commit()

    def write(self):
        self.cur.execute('SELECT * FROM players')
        for ver in self.cur:
            print ver

    def __del__(self):
            if self.connection:
                self.connection.close()
                print 'connection destroy'


class Player(ConnectPg):

    id = 0
    nick = ""
    name = ""
    surname = ""
    money = 0
    db_con = None

    def __init__(self, player_id, player_nick, player_name, player_surname, player_money=1000):
        self.db_con = ConnectPg()

        self.id = player_id
        self.nick = player_nick
        self.name = player_name
        self.surname = player_surname
        self.money = player_money

        self.db_con.insert((self.id, self.nick, self.name, self.surname, self.money))

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

def betOnRulet():
    print "Bet on numers"
    numbers = raw_input()
    print "How many money you bet on : %s" % (x for x in numbers) # TODO: jakos to ogarnac !


def gra():
    colorDictionary = {"red": (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36),
                       "black": (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)}
    #obstawianie
    betOnRulet()

def main():
    user1 = Player(6, "olo123", "Ola", "Bak")
    user1.db_con.write()
#    gra()

main()


