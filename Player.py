class Player:
    id = 0
    nick = ""
    money = 1000

    def __init__(self, id, name ):
        self.id = id
        self.nick = name
        #connect with postgres;
        # wpisanie urzytkownika;

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

  #  def findPlayer(self):
        # poszukanie po bazie danych czy isteniej  zwrocenie jego id ;


user1 = Player(1, "Ola")
print user1.nick;

