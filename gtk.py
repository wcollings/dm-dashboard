import gi
import os
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

chars=list()
charInfo=list()
class charList(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Character List")
        #charlist - the list of characters on the left side
        self.charList = Gtk.ListBox()
        #charBox - the box I'm packing the charList into
        self.charBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        self.loadChars(self.charList)
        self.charBox.pack_start(self.charList, True, True, 0)
        self.charBox.pack_start(charInfo[0], True, True, 0)
        self.add(self.charBox)
       
    #don't need this right now, but this is how you make a button work 
    def on_button_clicked(self, index):
        print("placeholder")        
    
    #load the character list
    def loadChars(self,l):
        files=os.listdir("chars")
        print(files)
        index=0
        #just open the files and load them into the program
        for file in files:
            with open("chars/"+file) as f:
                chars.append(json.load(f))
        #putting them all in the lefthand box
        CHARLABEL= Gtk.Label("Characters")
        self.charBox.pack_start(CHARLABEL, True, True, 0)
        for char in chars:
            #listBoxRow - the row of a list box. It makes sense but took me a while to wrap my
            #head around or find
            row = Gtk.ListBoxRow()
            box= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
            row.add(box)
            label1=Gtk.Label(char['name'])
            box.pack_start(label1, True, True, 0)
            l.add(row)
            index+=1
        self.createCharBoxes()
    #makes the info pane for each person/monster. Monster functionality isn't actually made yet
    def createCharBoxes(self):
        for char in chars:
            box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
            for item in char:
                b=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
                l1=Gtk.Label(item)
                l2=Gtk.Label(char[item])
                b.pack_start(l1, True, True, 0)
                b.pack_start(l2, True, True, 0)
                box.pack_start(b, True, True, 0)
            charInfo.append(box)

win= charList()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
