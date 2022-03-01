
class Player:
   # Klassens konstruktor. Objekt skapas utifrån textfilen
    def __init__(self,name,serve,wins,gamesplayed):
        self.__name = name
        self.__serve = serve
        self.__wins = wins
        self.__gamesplayed = gamesplayed
        self.__points = 0
        self.__games= 0
        self.__sets = 0
        self.__adv = False
        self.__changeserver = False

    def get_change_server(self):
        return self.__changeserver

    def set_change_server(self, tochange):
        self.__changeserver = tochange

    #Mängd getters,setters och resetters
    def reset_points(self,other):
        self.__points = 0
        other.__points = 0
        self.__adv = False
        other.__adv = False

    def set_points(self, points):
        self.__points += points

    def set_games(self):
        self.__games+=1
        
    def set_sets(self):
        self.__sets+=1
    
    def get_points(self):
        return self.__points
    
    def get_games(self):
        return self.__games
     
    def get_sets(self):
        return self.__sets
    
    def get_adv(self):
        return self.__adv

    def set_adv(self):
        self.__adv = not self.__adv
    
    def reset_games(self,other):
        self.__games = 0
        other.__games = 0
    
    def get_serve(self):
        return self.__serve

    def get_wins(self):
        return self.__wins
    
    def reset_gamesendofmatch(self):
        self.__games = 0
    
    def reset_setsendofmatch(self):
        self.__sets = 0
    
    def reset_pointsendofmatch(self):
        self.__points = 0
    
    def get_gamesplayed(self):
        return self.__games

    def get_name(self):
        return self.__name

    def get_serve(self):
        return self.__serve

    def get_wins(self):
        return self.__wins

    def get_gamesplayed(self):
        return self.__gamesplayed

    def get_ratio(self):
        return round((self.__wins)/(self.__gamesplayed),3)

    #Funktion som sätter avgör games utifrån points
    def __gt__(self,other):
        
        if other.get_points() < 40 and self.get_points() < 40:
            if self.get_points() == 30:
                self.set_points(10) 
            else:
                self.set_points(15)
        elif self.get_points() < 40 and other.get_points() == 40:
            if self.get_points() == 30:
                self.set_points(10) 
            else:
                self.set_points(15)
                
        elif self.get_points()== 40 and other.get_points() < 40:
            self.reset_points(other)
            self.set_games()

        elif self.get_points()==40 and other.get_points()==40:
            if other.get_adv() == False and self.get_adv() == False:
                self.set_adv()
            elif other.get_adv() == False and self.get_adv() == True:
                self.reset_points(other)
                self.set_games()
            elif other.get_adv() == True and self.get_adv() == False:
                other.set_adv()
                
        if self.get_games() >= (other.get_games() + 2) and self.get_games() >= 6:
            self.set_sets()
            self.reset_games(other)
            self.set_change_server(True)
        
        elif other.get_games() >= (self.get_games() + 2) and other.get_games() >= 6:
            other.set_sets()
            self.reset_games(other)
            self.set_change_server(True)
 
    
    
    

