__author__ = "Thimo, Koen, Remon en Edo"
__copyright__ = "Copyright 2016, Groep 4 HU"
__credits__ = ["Nederlandse Spoorwegen", "Hogeschool Utrecht"]
__license__ = "GNU GPL"
__version__ = "0.01"

# Module Import
from tkinter import *
from tkinter.messagebox import *
# Bij gebruik van afbeeldingen
from PIL import Image, ImageTk

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
    fontje = ('Helvetica', 15, 'bold')

    # UI Vertrektijden:
    UIVertrek = Tk()
    UIVertrek.configure(height=250, width=635, background=UIBackground)
    UIVertrek.title('Vertrektijden NS')

    # Labels in UIVertrek
    Label(UIVertrek,text='Vertrektijden',font=top_font, foreground=front_text, background=back_text).place(x=235,y=30)
    Label(UIVertrek,text='Voer plaatsnaam in: ',font=fontje, foreground=front_text, background=back_text).place(x=230,y=70)
    invoerPlaats = Entry(UIVertrek)
    invoerPlaats.place(x=255, y = 110)

    # Knop in UIVertrek
    KnopTerug = Button(UIVertrek, text='Terug', foreground=front_knop, background=back_knop, font=knop, command=UIVertrek.quit).place(x=5, y=5)
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


    for i in range(0,16):
        if test == 15:
            break

        Label(UIVertrek, text = "17:35", font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=125, y= y_as)
        Label(UIVertrek, text = "Gouda-Goverwelle", font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=200, y=y_as)
        Label(UIVertrek, text = "5a", font=fontje,anchor='w',  foreground=front_text, background=back_text).place(x=365, y=y_as)
        Label(UIVertrek, text = "Wijzigingen?", font=fontje,anchor='w', foreground=front_text, background=back_text).place(x=415,y=y_as)

        y_as += 20
        test +=1

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
KnopAMS = Button(UI, text='Ik wil naar \nAmsterdam', foreground=front_knop, background=back_knop, font=knop).place(x=50, y=100)
KnopKaart = Button(UI, text='Kopen \nlos kaartje', foreground=front_knop, background=back_knop, font=knop).place(x=160, y=100)
KnopOV = Button(UI, text='Sluit scherm', foreground=front_knop, background=back_knop, font=knop, command=UI.quit).place(x=260, y=100)
KnopBuitenland = Button(UI, text='Ik wil naar \nhet buitenland', foreground=front_knop, background=back_knop, font=knop).place(x=380, y=100)
KnopVertrek = Button(UI, text='Huidige \nvertrektijden', foreground=front_knop, background=back_knop, font=knop, command=zoekStad).place(x=500, y=100)

UI.mainloop()
