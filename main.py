from cProfile import label
import statistics
import tkinter
from Player import Player

from match import Match

from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import random

import time





def windowconfig():
    dataoption = 0
    window = Tk() 
    window.geometry("600x500") 
    window.resizable(False , False) 
    window.title("Tennis simulator")
    return window
windows = windowconfig()
playersname = StringVar()
playersname.set("")
matchupnames = []
# Denna funktion läser in statistiken från listan och skapar en lista med spelarobjekt.
def filetolists():
    playerlist = []
    fil = open("spelare","r")
    playersandstatistics = fil.readlines()

    for i in range(len(playersandstatistics)):
        strippeddata = playersandstatistics[i].strip("\n")
        playerstats = strippeddata.split(" ")
        playerlist.append(Player(playerstats[0], float(playerstats[1]), int(playerstats[2]), int(playerstats[3])))
    return playerlist

def updatedstatistics(match):
            
            fil2= open("spelare","r+")
            
            
            preupdatelist = fil2.readlines()

            

            for i in range(len(preupdatelist)):
                if match.get_matchwinner().get_name() in preupdatelist[i]:
                    preupdatelist[i] = match.get_matchwinner().get_name() +" "+ str(match.get_matchwinner().get_serve())+" "+ str(match.get_matchwinner().get_wins()+1)+" "+str(match.get_matchwinner().get_gamesplayed()+1)+"\n"
                
            
            for x in range(len(preupdatelist)):
                if match.get_matchloser().get_name() in preupdatelist[x]:
                    preupdatelist[x]= match.get_matchloser().get_name() +" "+ str(match.get_matchloser().get_serve())+" "+ str(match.get_matchloser().get_wins())+" "+str(match.get_matchloser().get_gamesplayed()+1)+"\n"
            
            fil2.close()

            updatedstatistics = open("spelare", "w")

            updatedstatistics.writelines(preupdatelist)
            
            fil2.close()

# Denna funktion sorterar spelarobjekten i en lista efter winratio.
def comparisonwin(listofplayerobjects):
    ratiolist=[]
    for i in range(len(listofplayerobjects)):
        ratiolist.append(listofplayerobjects[i].get_ratio())
    ratiolist.sort(reverse=True)

    sortedplayerlist = []
    for i in range(len(ratiolist)):
        for x in range(len(listofplayerobjects)):
            if ratiolist[i] == listofplayerobjects[x].get_ratio():
                sortedplayerlist.append(listofplayerobjects[x])
    return sortedplayerlist


#Denna funktion generar en tabell.
def tablemaker(basewindow,listsorted):
    table = ttk.Treeview(basewindow,height=len(listsorted), selectmode="extended")
    table['columns'] = ('player_name', 'serve%', 'Wins', 'Win%')

    table.column("#0", width=0,  stretch=NO)
    table.column("player_name",anchor=CENTER, width=80)
    table.column("serve%",anchor=CENTER,width=80)
    table.column("Wins",anchor=CENTER,width=80)
    table.column("Win%",anchor=CENTER,width=80)

    table.heading("#0",text="",anchor=CENTER)
    table.heading("player_name",text="Name",anchor=CENTER)
    table.heading("serve%",text="Serve%",anchor=CENTER)
    table.heading("Wins",text="Wins",anchor=CENTER)
    table.heading("Win%",text="Win%",anchor=CENTER)

    
    playerselected = IntVar()
    playerselected.set(0)
    
    
    
    def selectplayers(a):
        playersname.set("")
        selecteditems = table.selection()
        if(len(selecteditems) == 2):
            matchupname1 = table.item(0)['values'][0]
            matchupname2 = table.item(1)['values'][0]
            playersname.set(matchupname1.strip() + "-" + matchupname2.strip())
            

    table.bind('<ButtonRelease-1>', selectplayers)
    for i in range(len(listsorted)):
        table.insert(parent='',index='end',iid=i,text='',
        values=(listsorted[i].get_name(),int(listsorted[i].get_serve()*100),listsorted[i].get_wins(),listsorted[i].get_ratio()*100))
    
    table.grid(columnspan=len(listsorted),)

def button_and_label_config(playerlist):
    player1serv_var = StringVar()
    player2serv_var = StringVar()
    player1adv_var = StringVar()
    player2adv_var = StringVar()
    player1name_var = StringVar()
    player2name_var  = StringVar()
    server_var  = StringVar()
    player1games_var  = StringVar()
    player2games_var  = StringVar()
    player1sets_var  = StringVar()
    player2sets_var  = StringVar()
    player1points_var  = StringVar()
    player2points_var  = StringVar()

    stringvars = [player1serv_var,player2serv_var,player2adv_var,player1name_var,player2name_var,player1sets_var,player2sets_var,player1points_var,player2points_var]
    
    
    print(player1name_var.get())
    photo = PhotoImage(file="tennisboll.png")
    serverlabel1 = Label(windows,textvariable=player1serv_var)
    serverlabel1.grid(row=5,column=1)
    namelabel1 = Label(windows,textvariable=player1name_var)
    namelabel1.grid(row=5,column=2)
    pointslabel1 = Label(windows,textvariable=player1points_var)
    pointslabel1.grid(row=5,column=3)
    gameslabel1 = Label(windows,textvariable=player1games_var)
    gameslabel1.grid(row=5,column=4)
    setslabel1 = Label(windows,textvariable=player1sets_var)
    setslabel1.grid(row=5,column=5)
    advlabel1 = Label(windows,textvariable=player1adv_var)
    advlabel1.grid(row=5,column=6)
   
    currentresult = Label(windows,image=photo, width=20,height=20)
    currentresult.grid(row=5,column=7)

    serverlabel2 = Label(windows,textvariable=player2serv_var)
    serverlabel2.grid(row=6,column=1)
    namelabel2 = Label(windows,textvariable=player2name_var)
    namelabel2.grid(row=6,column=2)
    pointslabel2 = Label(windows,textvariable=player2points_var)
    pointslabel2.grid(row=6,column=3)
    gameslabel2 = Label(windows,textvariable=player2games_var)
    gameslabel2.grid(row=6,column=4)
    setslabel2 = Label(windows,textvariable=player2sets_var)
    setslabel2.grid(row=6,column=5)
    advlabel2 = Label(windows,textvariable=player2adv_var)
    advlabel2.grid(row=6,column=6)
    

    
    def simulator():

        if "-" in playersname.get():
            player1tosimulate= None
            player2tosimulate= None
            
            playername1= playersname.get().split("-")[0]
            playername2= playersname.get().split("-")[1]
            for i in range(len(playerlist)):
                if playername1 == playerlist[i].get_name():
                    player1tosimulate = playerlist[i]
                if playername2 == playerlist[i].get_name():
                    player2tosimulate = playerlist[i]
            match = Match(player1tosimulate,player2tosimulate)

            player1name_var.set(playername1)
            player2name_var.set(playername2)
            
            
            
            
            
            while match.get_matchongoing():
                match.points()
                player1adv_var.set("")
                player2adv_var.set("")


                servername = match.get_server().get_name()
                
                server_var.set(match.get_server().get_name())
                player1games_var.set(str(match.get_player1().get_games()))
                player2games_var.set(str(match.get_player2().get_games()))
                player1sets_var.set(str(match.get_player1().get_sets()))
                player2sets_var.set(str(match.get_player2().get_sets()))
                player1points_var.set(str(match.get_player1().get_points()))
                player2points_var.set(str(match.get_player2().get_points()))


                if servername == player1name_var.get():
                    player1serv_var.set("(S)")
                    player2serv_var.set("")
                
                if servername == player2name_var.get():
                    player2serv_var.set("(S)")
                    player1serv_var.set("")
                
                if match.get_player1().get_adv()== True:
                    player1adv_var.set("ADV")
                    player2adv_var.set("")
                
                if match.get_player2().get_adv()== True:
                    player2adv_var.set("ADV")
                    player1adv_var.set("")
                
                windows.update()
                time.sleep(0.01)
            

            for var in stringvars:
                var.set("")
                updatedstatistics(match)
        else:
            messagebox.showerror("Error","Välj två spelare!")
    






            
                    
                    
                    
                        
                    


                



            
        
        


    
    
    simulatebutton= Button(windows, command=simulator, text="Simulate")
    simulatebutton.grid(ipady=15,ipadx=25,column=int(1.5), rowspan=4)

  


        


        
           

         
        

        




# Funktion där alla andra funktioner kallas på 
def main():
    
    playerlistfromfile = filetolists()
    sortedlist = comparisonwin(playerlistfromfile)
    finishedtable = tablemaker(windows,sortedlist)
    button_and_label_config(playerlistfromfile)

    
    
    windows.mainloop()
    
    
main()