from tkinter import *
import time

master = Tk()

click = 0
multi = 1
multi_number = 0
price_multi = 10
price_cps = 100
cps = 0

def update():
    mainClickButton["text"] = "Clicks: " + str(click)
    Label1["text"] = "Multiplier: " + str(multi)
    TwoxClickButton["text"] = "Purchase Double Clicks: " + str(price_multi)
    persecClickButton["text"] = "Clicks Per Second: " + str(price_cps)
    Label2["text"] = "Clicks Per Second: " + str(cps)

def buy2x():
    global click
    global multi
    global price_multi
    global multi_number
    if click < price_multi:
        print("Too Expensive!")
    elif click >= price_multi:
        multi_number += 1
        multi = multi*1.1
        click = click - price_multi
        price_multi = price_multi*1.15**multi_number
        print("Bought!")
    update()

def buttonCommand():
    global click
    global multi
    click = click + 1*(multi)
    print(str(click)+ " Damage Done to")
    update()

def buyautoclick():
    global click
    global price_cps
    global cps
    if click < price_cps:
        print("Too Expensive!")
    elif click >= price_cps:
        click = click - price_cps
        price_cps = price_cps*2
        cps = cps + 1
        autoclick()
    update()

def autoclick():
    global click
    global multi
    global cps
    click = click + 0.1
    master.after(1000, autoclick)
    update()
    
#def hacks():
#    global click
#    click = click + 100000

Label1 = Label(master, text="Multipler: ")
Label1.pack()

Label2 = Label(master, text="Clicks Per Second: ")
Label2.pack()

mainClickButton = Button(master, text="Clicks: ", command = buttonCommand, height = 10, width = 50)
mainClickButton.pack(fill=X)

TwoxClickButton = Button(master, text="Purchase Multiplier x0.1: ", command = buy2x)
TwoxClickButton.pack(fill=X)

persecClickButton = Button(master, text="Purchase +1 Click Per Second: ", command = buyautoclick)
persecClickButton.pack(fill=X)

master.title("Clicker! v0.5")
master.geometry("200x300")
master.resizable(width=False, height=False)

update()

master.mainloop()
