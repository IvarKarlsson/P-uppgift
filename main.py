from cProfile import label
import statistics
import tkinter
from Player import Player

from match import Match

from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import random
import os
import time


#Skapar ett grafisktfönster.
def windowconfig():
    dataoption = 0
    window = Tk() 
    window.geometry("600x500") 
    window.resizable(False , False) 
    window.title("Tennis simulator")
    return window

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

#Funktionen uppdaterar statistiken i tabellen där spelarna väljs inför en match.
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

#Denna funktion generar en tom tabell där statistiken sedan kan föras in.
def tablemaker(basewindow,listsorted, playersname):
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
    
    
    # Funktion som gör att användaren kan välja vilka som ska delta i matchen.
    def selectplayers(playersname):
        playersname.set("")
        selecteditems = table.selection()
        
        if(len(selecteditems) == 2):
    
            matchupname1 = table.item(selecteditems[0])['values'][0]
            matchupname2 = table.item(selecteditems[1])['values'][0]
            playersname.set(matchupname1.strip() + "-" + matchupname2.strip())
            
        
            

    table.bind('<ButtonRelease-1>',lambda x: selectplayers(playersname))
    for i in range(len(listsorted)):
        table.insert(parent='',index='end',iid=i,text='',
        values=(listsorted[i].get_name(),int(listsorted[i].get_serve()*100),listsorted[i].get_wins(),round(listsorted[i].get_ratio()*100,3)))
    
    table.grid(columnspan=len(listsorted),column=1,row=1)
    return table

#Funktion som uppdaterar poängställningen i matchen med points,games och sets
def button_and_label_config(playerlist, table,windows,playersname):
    isplaying = BooleanVar(value=False)
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

    stringvars = [player1serv_var,player2serv_var,player1adv_var,player2adv_var,player1name_var,player2name_var,server_var,player1games_var,player2games_var,player1sets_var,player2sets_var,player1points_var,player2points_var,playersname]
    
    
    print(player1name_var.get())
    serverlabel1 = Label(windows,textvariable=player1serv_var)
    serverlabel1.grid(row=5,column=0)
    namelabel1 = Label(windows,textvariable=player1name_var)
    namelabel1.grid(row=5,column=1)
    pointslabel1 = Label(windows,textvariable=player1points_var)
    pointslabel1.grid(row=5,column=2)
    gameslabel1 = Label(windows,textvariable=player1games_var)
    gameslabel1.grid(row=5,column=3)
    setslabel1 = Label(windows,textvariable=player1sets_var)
    setslabel1.grid(row=5,column=4)
    advlabel1 = Label(windows,textvariable=player1adv_var)
    advlabel1.grid(row=5,column=5)
   
    
    

    serverlabel2 = Label(windows,textvariable=player2serv_var)
    serverlabel2.grid(row=6,column=0)
    namelabel2 = Label(windows,textvariable=player2name_var)
    namelabel2.grid(row=6,column=1)
    pointslabel2 = Label(windows,textvariable=player2points_var)
    pointslabel2.grid(row=6,column=2)
    gameslabel2 = Label(windows,textvariable=player2games_var)
    gameslabel2.grid(row=6,column=3)
    setslabel2 = Label(windows,textvariable=player2sets_var)
    setslabel2.grid(row=6,column=4)
    advlabel2 = Label(windows,textvariable=player2adv_var)
    advlabel2.grid(row=6,column=5)
    

    # Framställer en knapp. Vid tryck av knappen börjar simuleringen.
    def simulator(playersname):
        
        if "-" in playersname.get() and isplaying.get() == False:
            isplaying.set(True)
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

                #Denna del av funktionen visar vem av spelarna som servar
                if servername == player1name_var.get():
                    player1serv_var.set("(S)")
                    player2serv_var.set("")
                
                elif servername == player2name_var.get():
                    player2serv_var.set("(S)")
                    player1serv_var.set("")
                #Denna del av funktionen visar om en spelare har fördel (ADV)
                if match.get_player1().get_adv()== True:
                    player1adv_var.set("ADV")
                    player2adv_var.set("")
                
                elif match.get_player2().get_adv()== True:
                    player2adv_var.set("ADV")
                    player1adv_var.set("")
                
                windows.update()
                time.sleep(0.2)
            
            # Denna del av funktionen uppdaterar statistiken i spelartabellen och skriver ut när matchen är avgjord.
            for var in stringvars:
                var.set("")
            updatedstatistics(match)
            updatedlist = filetolists()
            sortedlist = sorted(updatedlist)
            resetStats(playerlist)

            for i in range(len(sortedlist)):
                table.delete(i)
                table.insert(parent='',index='end',iid=i,text='',
                values=(sortedlist[i].get_name(),int(sortedlist[i].get_serve()*100),sortedlist[i].get_wins(),round(sortedlist[i].get_ratio()*100,3)))
            isplaying.set(False)
            windows.update()
            messagebox.showinfo("Match avslutad",match.get_matchwinner().get_name() + " vann matchen! Statistiken är uppdaterad")
        else:
            messagebox.showerror("Error","Välj två spelare eller vänta tills matchen är klar!")
    
               
    
    simulatebutton= Button(windows, command=lambda : simulator(playersname), text="Simulate",width=7, height=1)
    simulatebutton.grid(ipady=15,ipadx=25,column=int(0), rowspan=5,row=10)
    
    #En paus_knapp framställs. Vid tryck stannar simuleringen.
    def pause():
        messagebox.showinfo("Pausad","Matchen är pausad, tryck på OK för att återuppta.")

    pausebutton = Button(windows,command=pause, text="Pause simulation", width=7, height=1)
    pausebutton.grid(ipady=15,ipadx=25,column=int(0), rowspan=5,row=20)

#Nollställer points,games och sets från den tidigare matchen.
def resetStats(listofplayers):
    for i in range(len(listofplayers)):
        listofplayers[i].reset_gamesendofmatch()
        listofplayers[i].reset_setsendofmatch()
        listofplayers[i].reset_pointsendofmatch()

# En textruta som förklarar displayen, samt vad användaren ska göra.
def explanatorytext(windows):
    infolabel = Label(windows, text = "ADV= Fördel\n  (S)= Spelaren som servar\n\n Markera två spelare i listan för att starta")
    infolabel.grid(ipady=0,ipadx=1,column=0, rowspan=5)

# Funktion där alla andra funktioner kallas på 
def main():
    windows = windowconfig()
    playersname = StringVar()
    playersname.set("")
        

    explanatorytext(windows)
    playerlistfromfile = filetolists()
    sortedlist = sorted(playerlistfromfile)
    table = tablemaker(windows,sortedlist,playersname)
    button_and_label_config(playerlistfromfile,table, windows, playersname)
    windows.mainloop()
    
    
    
main()