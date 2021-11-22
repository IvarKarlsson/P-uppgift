from Player import Player

from tkinter import ttk

from tkinter import *

dataoption = 0
window = Tk() 
window.geometry("600x500") 
window.resizable(False , False) 
window.title("Tennis simulator")

diagramlistbox = Listbox(window, width=40, selectmode="multiple", height=4)
diagramlistbox.pack(pady=15)

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
# Denna funktion skapar en lista med strängar av spelarnas namn och dess statistik som är redo för listboxen.
def diagram(playerlist):
    diagramlist=[]
    diagramlist.append("Name       Serve%      Wins       Win%")
    for i in range(len(playerlist)):
        diagramlist.append(playerlist[i].__str__())
    return diagramlist
#  Lägger in lista med strängar i en listbox
def listboxdiagram(playerstrings):
    for i in range(len(playerstrings)):
        diagramlistbox.insert(END,playerstrings[i])
# Funktion där alla andra funktioner kallas på 
def main():
    playerlistfromfile = filetolists()
    sortedlist = comparisonwin(playerlistfromfile)
    diagramSTR = diagram(sortedlist)
    listboxdiagram(diagramSTR)

main()
window.mainloop()





