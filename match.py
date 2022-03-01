
import random

#En match klass där de spelarna som valts skapas som matchobjekt.
class Match:
    def startserving(self, player1,player2):
        
        return random.choice([player1,player2])
    
    def __init__(self,player1,player2):
        
        self.__player1 = player1
        self.__player2 = player2
        self.__pointsp1 = 0
        self.__pointsp2 = 0
        self.__gamesp1 = 0
        self.__gamesp2 = 0
        self.__setsp1 = 0
        self.__setsp2 = 0
        self.__server = self.startserving(player1,player2)
        self.__matchongoing = True
        self.__matchwinner = None
        self.__matchloser = None
        
    #En mängd getters och setters.
    def get_player1(self):
        return self.__player1
    
    def get_player2(self):
        return self.__player2

    def get_server(self):
        return self.__server

    def get_pointsp1(self):
        return self.__pointsp1
    
    def get_pointsp2(self):
        return self.__pointsp2
    
    def get_gamesp1(self):
        return self.__gamesp1
    
    def set_gamesp1(self):
        self.__gamesp1+=1
    
    def set_gamesp2(self):
        self.__gamesp2+=1

    def reset_gamesp1(self):
        self.__gamesp1= 0

    def reset_gamesp2(self):
        self.__gamesp2= 0
    
    def get_gamesp2(self):
        return self.__gamesp2
    
    def get_setsp1(self):
        return self.__setsp1
    
    def get_setsp2(self):
        return self.__setsp2
    
    def set_matchwinner(self,winner):
        self.__matchwinner = winner

    def set_matchloser(self,loser):
        self.__matchloser = loser

    def get_matchloser(self):
        return self.__matchloser

    def get_matchwinner(self):
        return self.__matchwinner

    def set_sets(self):
        self.__setsp1 = self.get_setsp1()+1
        self.set_server()
        
    def get_matchongoing(self):
        return self.__matchongoing
    
    def set_matchongoing(self):
        self.__matchongoing = not self.__matchongoing
    
    #Funktion som ändrar den som servar
    def set_server(self):
        if self.get_player1().get_name()== self.get_server().get_name():
            self.__server= self.get_player2()
        else:
            self.__server= self.get_player1()
        
    
    #Funktion som simulerar en point och byter server vid gem.
    def points(self):
        server = self.get_server()
        playerservername = server.get_name()
        servepercentage = server.get_serve()
        otherplayer = self.get_player1()
        if playerservername == self.get_player1().get_name():
            otherplayer = self.get_player2()

        if servepercentage >= random.random():
            server.__gt__(otherplayer)
        else:
            if playerservername == self.get_player1().get_name():
                self.get_player2().__gt__(self.get_player1())
            else:
                self.get_player1().__gt__(self.get_player2())



        # if self.get_gamesp2()>= (self.get_gamesp1() + 2) and self.get_gamesp2()>= 6:
        #     print("p2: " + str(self.get_gamesp2()))
        #     self.set_server()
        #     self.reset_gamesp1()
        #     self.reset_gamesp2()

        # if self.get_gamesp1()>= (self.get_gamesp2() + 2) and self.get_gamesp1()>= 6:
        #     self.set_server()
        #     self.reset_gamesp1()
        #     self.reset_gamesp2()

        
        if(self.get_gamesp1() < self.get_player1().get_games()):
            self.set_server()
            self.set_gamesp1()
        
        if(self.get_gamesp2() < self.get_player2().get_games()):
            self.set_server()
            self.set_gamesp2()
        
        if(self.get_player1().get_change_server() == True):
            self.set_server()
            self.get_player1().set_change_server(False)
            self.reset_gamesp1()
            self.reset_gamesp2()

        if(self.get_player2().get_change_server() == True):
            self.set_server()
            self.get_player2().set_change_server(False)
            self.reset_gamesp1()
            self.reset_gamesp2()


        
        if self.get_player1().get_sets()== 3:
            self.set_matchongoing()
            self.set_matchwinner(self.get_player1())
            self.set_matchloser(self.get_player2())
            
            
        if self.get_player2().get_sets()== 3:
            self.set_matchongoing()
            self.set_matchwinner(self.get_player2())
            self.set_matchloser(self.get_player1())
           
        print("\n")
        print("(S) " + self.get_server().get_name())
        print(self.get_player1().get_name() +" " + str(self.get_player1().get_points())+" ADV: " + str(self.get_player1().get_adv()) + " Gems:"+ str(self.get_player1().get_games())+" Sets:"+ str(self.get_player1().get_sets()))
        print(self.get_player2().get_name() +" " + str(self.get_player2().get_points())+" ADV: " + str(self.get_player2().get_adv()) + " Gems:"+ str(self.get_player2().get_games())+" Sets:"+ str(self.get_player2().get_sets()))
        

            




