__author__ = "Thimo, Koen, Remon en Edo"
__copyright__ = "Copyright 2016, Groep 4 HU"
__credits__ = ["Nederlandse Spoorwegen", "Hogeschool Utrecht"]
__license__ = "GNU GPL"
__version__ = "0.01"

# Module Import
from tkinter import *
from api import *
from tkinter import messagebox
from time import strftime

# Build nummer updater
build = 0
with open("build.txt", "r") as f:
    contents = f.read()
    f.close()

build = int(contents) + 1

with open("build.txt", "w") as f:
    f.write(str(build))
    f.close()

# UI van Vertrektijden
def zoekStad():

    # UI zoekStad details:
    top_font = ("Helvetica", 20, "bold")
    UIBackground = "#fcc917" # Geel
    front_text = "#002d72"  # Blauw
    back_text = "#fcc917"  # Blauw
    front_knop = "#ffffff" # Wit
    back_knop = "#002d72" # Blauw
    knop = font=("Helvetica", 10)
    fontje = ('Helvetica', 10, 'bold')

    # UI Vertrektijden:
    UIVertrek = Tk()
    UIVertrek.configure(height=250, width=635, background=UIBackground)
    UIVertrek.title('Vertrektijden NS')

    # Labels in UIVertrek
    Label(UIVertrek,text='Het is nu: ' +strftime("%H:%M:%S"),font=fontje, foreground=front_text, background=back_text).place(x=250,y=0)
    Label(UIVertrek,text='Vertrektijden',font=top_font, foreground=front_text, background=back_text).place(x=235,y=30)
    Label(UIVertrek,text='Voer plaatsnaam in: ',font=fontje, foreground=front_text, background=back_text).place(x=250,y=75)
    invoerPlaats = Entry(UIVertrek)
    invoerPlaats.place(x=255, y = 110)

    # Knop in UIVertrek
    KnopTerug = Button(UIVertrek, text='Terug', foreground=front_knop, background=back_knop, font=knop, command=UIVertrek.destroy).place(x=5, y=5)
    KnopZoek = Button(UIVertrek, text='Zoek tijden', foreground=front_knop, background=back_knop, font=knop, command=lambda: vertrekTijden(invoerPlaats.get(),UIVertrek))
    KnopZoek.place(x = 280, y = 140)

    UIVertrek.mainloop()

def vertrekTijden(station, UIVertrek):

    # UI Vertrektijden details:
    top_font = ("Helvetica", 10, "bold")
    UIBackground = "#fcc917" # Geel
    front_text = "#002d72"  # Blauw
    back_text = "#fcc917"  # Blauw
    fontje = ('Helvetica', 8)

    y_as = 240
    test = 0

    Label(UIVertrek,text='U heeft gekozen voor: Station ' +station,font=top_font, foreground=front_text, background=back_text).place(x=200,y=180)
    UIVertrek.configure(height=625, width=635, background=UIBackground)
    Label(UIVertrek, text = 'Tijd: \tEindbestemming: \tSpoor: \tWijzigingen:', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 125, y = 210)

    if check(station):
        vertrekdict = vertrektijden(station)

        for vertrek in vertrekdict['ActueleVertrekTijden']['VertrekkendeTrein']:
            if test == 15:
                break

            Label(UIVertrek, text = vertrek['VertrekTijd'][11:16], font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=125, y= y_as)
            Label(UIVertrek, text = vertrek['EindBestemming'], font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=180, y=y_as)
            Label(UIVertrek, text = vertrek['VertrekSpoor']['#text'], font=fontje,anchor='w',  foreground=front_text, background=back_text).place(x=350, y=y_as)
            if vertrek['VertrekSpoor']['@wijziging'] == 'true':
                edit = 'Haha kut NS #altijdtelaat'
            if vertrek['VertrekSpoor']['@wijziging'] == 'false':
                edit = '       '
            Label(UIVertrek, text=edit, font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=408,y=y_as)

            y_as += 20
            test +=1
    else:
        messagebox.showerror('NS Automaat', 'U heeft geen geldig station ingevoerd. Probeer het opnieuw!')

def excuses():
    messagebox.showinfo('NS Automaat','Helaas is deze functie niet in gebruik. Excuses!')

# UI Baisscherm details:
top_text = ("Helvetica", 20, "bold")
UIBackground = "#fcc917" # Geel
front_text = "#002d72"  # Blauw
back_text = "#fcc917"  # Blauw
front_knop = "#ffffff" # Wit
back_knop = "#002d72" # Blauw
knop = font=("Helvetica", 10)

# UI Basisscherm:
UI = Tk()
UI.configure(height=250, width=635, background=UIBackground)
UI.title('NS Automaat')

# Labels in UI
Label(UI, text='Build versie: ' + str(build), foreground=front_text, background=back_text).place(x=0, y=0)
Label(UI, text='Welkom bij NS', font=top_text, foreground=front_text, background=back_text).place(x=215, y=30)
Label(UI, text='Door: Thimo, Koen, Remon en Edo', foreground=front_text, background=back_text).place(x=230, y=215)

# Knoppen in UI
KnopAMS = Button(UI, text='Ik wil naar \nAmsterdam', foreground=front_knop, background=back_knop, font=knop, command=excuses).place(x=50, y=100)
KnopKaart = Button(UI, text='Kopen \nlos kaartje', foreground=front_knop, background=back_knop, font=knop, command=excuses).place(x=160, y=100)
KnopOV = Button(UI, text='Sluit scherm\n', foreground=front_knop, background=back_knop, font=knop, command=UI.destroy).place(x=260, y=100)
KnopBuitenland = Button(UI, text='Ik wil naar \nhet buitenland', foreground=front_knop, background=back_knop, font=knop, command=excuses).place(x=380, y=100)
KnopVertrek = Button(UI, text='Huidige \nvertrektijden', foreground=front_knop, background=back_knop, font=knop, command=zoekStad).place(x=500, y=100)

UI.mainloop()
