from Player import Player

from tkinter import ttk

from tkinter import *
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
    table = ttk.Treeview(basewindow)
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

    for i in range(len(listsorted)):
        table.insert(parent='',index='end',iid=i,text='',
        values=(listsorted[i].get_name(),listsorted[i].get_serve(),listsorted[i].get_wins(),listsorted[i].get_ratio()))
    
    table.pack()



# Funktion där alla andra funktioner kallas på 
def main():
    windows = windowconfig()
    playerlistfromfile = filetolists()
    sortedlist = comparisonwin(playerlistfromfile)
    tablemaker(windows,sortedlist)
    
    windows.mainloop()
    
main()









