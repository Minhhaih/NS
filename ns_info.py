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
	