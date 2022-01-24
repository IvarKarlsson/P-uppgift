from Player import Player

from match import Match

from tkinter import ttk

from tkinter import *
import random




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
        
        if playerselected.get() < 2:
            matchupplayer = table.focus()
            if playerselected == 0:
                playersname.set((table.item(matchupplayer)['values'][0]).strip())
            else:
                playersname.set((playersname.get()+"-" +table.item(matchupplayer)['values'][0]).strip())
            matchupnames.append(table.item(matchupplayer)['values'][0])
            playerselected.set(playerselected.get()+1)
        
        if playerselected.get() == 2:
            print(playersname.get())

    table.bind('<ButtonRelease-1>', selectplayers)
    for i in range(len(listsorted)):
        table.insert(parent='',index='end',iid=i,text='',
        values=(listsorted[i].get_name(),int(listsorted[i].get_serve()*100),listsorted[i].get_wins(),listsorted[i].get_ratio()*100))
    
    table.grid(columnspan=len(listsorted),)

def buttonconfig(playerlist):
    def simulator():
        player1tosimulate= None
        player2tosimulate= None
        
        playername1= playersname.get().split("-")[1]
        playername2= playersname.get().split("-")[2]
        for i in range(len(playerlist)):
            if playername1 == playerlist[i].get_name():
                player1tosimulate = playerlist[i]
            if playername2 == playerlist[i].get_name():
                player2tosimulate = playerlist[i]
        match = Match(player1tosimulate,player2tosimulate)
        while True:
            match.points()


    
    
    simulatebutton= Button(windows, command=simulator, text="Simulate")
    simulatebutton.grid(ipady=15,ipadx=25,column=int(1.5), rowspan=4)

    

# Funktion där alla andra funktioner kallas på 
def main():
    
    
    playerlistfromfile = filetolists()
    sortedlist = comparisonwin(playerlistfromfile)
    finishedtable = tablemaker(windows,sortedlist)
    buttonconfig(playerlistfromfile)
    
    
    
    windows.mainloop()
    
main()









