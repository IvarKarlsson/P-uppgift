
import random

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
    
    def get_gamesp2(self):
        return self.__gamesp2
    
    def get_setsp1(self):
        return self.__setsp1
    
    def get_setsp2(self):
        return self.__setsp2
    
    def set_games(self):
        self.__gamesp1= self.get_gamesp1()+1
        
    
    
    
    
    def set_points(self,player):
        isplayer1 = None
        currentpoints = None
        opponentspoint= None
        if player.get_name()== self.get_player1().get_name():
            currentpoints= self.get_pointsp1()
            opponentspoint= self.get_pointsp2()
            isplayer1=True
        else:
            currentpoints= self.get_pointsp2()
            opponentspoint= self.get_pointsp1()
            isplayer1=False
        if currentpoints < 30:
            currentpoints+=15
            self.__pointsp1 = currentpoints
        elif currentpoints == 30:
            currentpoints += 10
        elif currentpoints == 40 and opponentspoint<40:
            if isplayer1:
                self.set_games()
            else:
                self.set_games()
        elif currentpoints == 40 and opponentspoint==40:
            currentpoints = 50
        elif currentpoints == 50 and opponentspoint == 50:
            currentpoints = 40  
            opponentspoint = 40
        elif currentpoints == 50 and opponentspoint<=40:
            if isplayer1:
                self.set_games()
            else:
                self.set_games()
            



    def points(self):
        server = self.get_server()
        playername = server.get_name()
        servepercentage = server.get_serve()
        if servepercentage >= random.random():
            self.set_points(server)
        else:
            if playername== self.get_player1().get_name():
                self.set_points(self.get_player2())
            else:
                self.set_points(self.get_player1())
        print(self.get_player1().get_name() +" " + str(self.get_pointsp1()))
        print(self.get_player2().get_name() +" " + str(self.get_pointsp2()))

            







    

