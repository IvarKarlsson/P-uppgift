class Player:
#kommentar
   # Klassens konstruktor
    def __init__(self,name,serve,wins,gamesplayed):
        self.__name = name
        self.__serve = serve
        self.__wins = wins
        self.__gamesplayed = gamesplayed

    def __str__(self):
        finalstr = ""
        playerstatslist = [self.get_name(),str(round(self.get_serve(),3)),str(self.get_wins()), str(round(self.get_ratio(),3))]
        for i in range(len(playerstatslist)):
            numdiff = 12 - len(playerstatslist[i])
            finalstr += playerstatslist[i]
            for x in range(numdiff):
                finalstr += " "
        return finalstr

    def get_name(self):
        return self.__name

    def get_serve(self):
        return self.__serve

    def get_wins(self):
        return self.__wins

    def get_gamesplayed(self):
        return self.__gamesplayed

    def get_ratio(self):
        return (self.__wins)/(self.__gamesplayed)



