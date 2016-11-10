__author__ = "Thimo, Koen, Remon en Edo"
__copyright__ = "Copyright 2016, Groep 4 HU"
__credits__ = ["Nederlandse Spoorwegen", "Hogeschool Utrecht", "Hans Stol - Totaldesign"]
__license__ = "GNU GPL"
__version__ = "0.8"

# Module Import
from tkinter import *
from api import *
from tkinter import messagebox
from tkinter import simpledialog
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

def station_check(station,UI):

    if check(station):
        vertrekTijden(station)
    else:
        messagebox.showerror('NS Automaat', 'U heeft geen geldig station ingevoerd. Probeer het opnieuw!')
        UI.destroy()

def vertrekTijden(station):

    # UI Vertrekbord details:
    top_font = ("Helvetica", 25, "bold")
    UIBackground = "#ffffff" # Geel
    front_text = "#002d72"  # Blauw
    back_text = "#ffffff"  # Blauw
    knop = ('Helvetica', 10)
    klein = ('Helvetica', 8)
    verandering_font = "#FF0000"
    # UI Vertrekbord:
    UIVertrekbord = Tk()
    UIVertrekbord.configure(height=690, width=500, background=UIBackground)
    UIVertrekbord.title('Vertrekbord NS')

    vertrekdict = vertrektijden(station)

    y_as = 85
    stations = 0
    Tijd = Button(UIVertrekbord, text=''+strftime("%H:%M"), foreground=front_knop, background=back_knop, font=knop, height=(2), width=5, command=UIVertrekbord.destroy).place(x=5, y=0)
    Label(UIVertrekbord,text='Vertrek van de treinen',font=top_font, foreground=front_text, background=back_text).place(x=85,y=0)

    Label(UIVertrekbord,text='Station ' +station,font=klein, foreground=front_text, background=back_text).place(x=350,y=40)
    Label(UIVertrekbord, text = 'tijd', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 5, y = 65)
    Label(UIVertrekbord, text = 'naar', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 50, y = 65)
    Label(UIVertrekbord, text = 'spoor', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 170, y = 65)
    Label(UIVertrekbord, text = 'treinsoort', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 220, y = 65)
    Label(UIVertrekbord, text = 'opmerkingen', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 320, y = 65)
    Label(UIVertrekbord, text = 'vertraging', font = ('Helvetica', 10, 'bold'), foreground=front_text, background=back_text).place(x = 420, y = 65)

    for vertrek in vertrekdict['ActueleVertrekTijden']['VertrekkendeTrein']:
        if stations == 30:
            break
        Label(UIVertrekbord, text = vertrek['VertrekTijd'][11:16], font=klein,anchor='w', foreground=front_text, background=back_text).place(x=5, y= y_as)
        Label(UIVertrekbord, text = vertrek['EindBestemming'], font=klein,anchor='w', foreground=front_text, background=back_text).place(x=50, y=y_as)
        Label(UIVertrekbord, text = vertrek['VertrekSpoor']['#text'], font=klein,anchor='w',  foreground=front_text, background=back_text).place(x=170, y=y_as)
        Label(UIVertrekbord, text = vertrek['TreinSoort'], font=klein,anchor='w',  foreground=front_text, background=back_text).place(x=220, y=y_as)
        if vertrek['VertrekSpoor']['@wijziging'] == 'true':
            spoorwijziging = 'Gewijzigd spoor'
        if vertrek['VertrekSpoor']['@wijziging'] == 'false':
            spoorwijziging = '  '
        Label(UIVertrekbord, text=spoorwijziging, font=klein, anchor='w', foreground=front_text, background=back_text).place(x=320,y=y_as)
        try:
            if "PT" in vertrek['VertrekVertraging']:
                vertraging = vertrek['VertrekVertraging'][2:3]+'min'
        except KeyError:
            vertraging = '  '
            pass
        Label(UIVertrekbord, text=vertraging, font=klein, anchor='w', foreground=verandering_font, background=back_text).place(x=420,y=y_as)
        y_as += 20
        stations +=1

def excuses():
    messagebox.showinfo('NS Automaat','Helaas is deze functie niet in gebruik. Excuses!')

def UI_update(UI):
    UI.configure(height=400, width=635, background=UIBackground)

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
DoorUI = Label(UI, text='Door: Thimo, Koen, Remon en Edo', foreground=front_text, background=back_text).place(x=230, y=180)

# Knoppen in UI
KnopAMS = Button(UI, text='Ik wil naar \nAmsterdam', foreground=front_knop, background=back_knop, font=knop, command=lambda: vertrekTijden("Amsterdam Centraal")).place(x=50, y=100)
KnopKaart = Button(UI, text='Kopen \nlos kaartje', foreground=front_knop, background=back_knop, font=knop, command=excuses).place(x=160, y=100)
KnopOV = Button(UI, text='Sluit scherm\n', foreground=front_knop, background=back_knop, font=knop, command=UI.destroy).place(x=260, y=100)
KnopBuitenland = Button(UI, text='Ik wil naar \nhet buitenland', foreground=front_knop, background=back_knop, font=knop, command=excuses).place(x=380, y=100)
KnopVertrek = Button(UI, text='Huidige \nvertrektijden', foreground=front_knop, background=back_knop, font=knop, command=lambda: UI_update(UI)).place(x=500, y=100)

Label(UI, text='Voer plaatsnaam in: ', foreground=front_text, background=back_text).place(x=255, y=245)
invoerPlaats = Entry(UI)
invoerPlaats.place(x=255, y=270)
KnopZoek = Button(UI, text='Zoek vertrektijden', foreground=front_knop, background=back_knop, font=knop, command=lambda: station_check(invoerPlaats.get(),UI))
KnopZoek.place(x = 260, y = 295)

UI.mainloop()
