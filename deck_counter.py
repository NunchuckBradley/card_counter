# Import Module
from tkinter import *
import numpy as np

suits = ["♠️", "♥️", "♦️", "♣️"]
suitsCol = ["black", "red", "red", "black"]
runs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deckCount = 1

fullRange = True

drawnCards = []
redoBuffer = []

# create root window
root = Tk()

# root window title and dimension
root.title("Deck Counter")
# Set geometry(widthxheight)
root.geometry('900x500')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item) # yup ok, nonsene menu
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text = "Number of decks:")
lbl.grid()

# # adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)



# function to display user text when
# button is clicked
def clicked():

    res = "You wrote" + txt.get()
    lbl.configure(text = res)

def increaseDeck():
    global deckCount
    global drawnCards
    deckCount = deckCount + 1
    drawnCards = []
    updateCards(-1, -1, True)

def decreaseDeck():
    global deckCount
    global drawnCards
    deckCount = deckCount - 1
    drawnCards = []
    updateCards(-1, -1, True)

def undoMove():
    global drawnCards
    global redoBuffer
    redoBuffer.append(drawnCards.pop())
    print(drawnCards)
    updateCards(-1, -1, True)

def redoMove():
    global drawnCards
    global redoBuffer
    drawnCards.append(redoBuffer.pop())
    updateCards(-1, -1, True)

# button widget with red color text inside
btn = Button(root, text = "/\\" ,
             fg = "green", command=increaseDeck)
# Set Button Grid
btn.grid(column=2, row=0)

# button widget with red color text inside
btn2 = Button(root, text = "\\/" ,
             fg = "red", command=decreaseDeck)
# Set Button Grid
btn2.grid(column=3, row=0)



# button widget with red color text inside
undo = Button(root, text = "↩️" ,
             fg = "green", command=undoMove)
# Set Button Grid
undo.grid(column=1, row=20)

# button widget with red color text inside
redo = Button(root, text = "↪️" ,
             fg = "red", command=redoMove)
# Set Button Grid
redo.grid(column=2, row=20)







def updateCards(ic, jc, refresh=False):
    if (deckCount - drawnCards.count(str(ic) + ":" + str(jc))) < 1 and fullRange == True:
        return

    lbl = Label(root, text = ((deckCount * len(suits) * len(runs)) - len(drawnCards)) ).grid(column=4,row=0)

    if fullRange:
        if refresh == False:
            drawnCards.append(str(ic) + ":" + str(jc))
            redoBuffer = []
        for i, suit in enumerate(suits):
            for j, run in enumerate(runs):
                comp = str(i) + ":" + str(j)
                left = deckCount - drawnCards.count(comp)
                chances = "%.1f" % (100 * left / ((deckCount * len(suits) * len(runs)) - len(drawnCards)) ) + "%"

                lbl = Label(root, text = left).grid(column=j+1,row=2+(i*3))
                lbl = Label(root, text = chances).grid(column=j+1,row=3+(i*3))
    
    else:
        if refresh == False:
            drawnCards.append(jc)
            redoBuffer = []

    # get chances of any in suit
    for j, run in enumerate(runs):
        total = len(suits) * deckCount
        comp = j
        if fullRange:
            for i, suit in enumerate(suits):
                comp = str(i) + ":" + str(j)
                total = total - drawnCards.count(comp)
                
        else:
            total = total - drawnCards.count(comp)

        chances = "%.1f" % (100 * total / ((deckCount * len(suits) * len(runs)) - len(drawnCards)) ) + "%"
        lbl = Label(root, text = total).grid(column=j+1,row=4+(len(suits)*3))
        lbl = Label(root, text = chances).grid(column=j+1,row=5+(len(suits)*3))
    
    lbl = Label(root, text = "Total: ").grid(column=0,row=4+(len(suits)*3))
    lbl = Label(root, text = "Chances: ").grid(column=0,row=5+(len(suits)*3))


        

    print(drawnCards)

    # null and print history
    for i in range(10):
        Label(root, text = "").grid(row=20, column=3+i)
    for i, val in enumerate(reversed(drawnCards[-10:])):
        fg = "black"
        if fullRange == False:
            text = runs[val]
        else:
            text = runs[int(val.split(":")[1])] + suits[int(val.split(":")[0])]
            fg = suitsCol[int(val.split(":")[0])]
        # if fullRange:
            # text = text + suits[val]
        lbl = Label(root, text = text, fg = fg).grid(row=20, column=3+i)



for i, suit in enumerate(suits):
    if fullRange == False:
        i = 0
        suit = ""
    for j, run in enumerate(runs):
        card = Button(root, fg=suitsCol[i], text = run + suit, command=lambda i=i,j=j: updateCards(i, j))
        card.grid(column=j+1,row=1+(i*3));




# Execute Tkinter
root.mainloop()