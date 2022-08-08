from cProfile import label
import json
from threading import local
import requests
import wget
from tkinter import *
import tkinter.font as tkFont
from zipfile import ZipFile
from PIL import Image, ImageTk
import os
import sys

LinkApi, Links = 'https://api.github.com/repos/polymc/polymc/releases/latest', []
Content = requests.get(LinkApi).text
ContentJson = json.loads(Content)
Api_tag_name, Api_Assets = ContentJson['tag_name'], ContentJson["assets"]
Sistema, Lagacy, Portable = "Windows", "Lagacy", "Portable"


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

for i in range(len(Api_Assets)):
    Links.append(Api_Assets[i]["browser_download_url"])

for i in Links:
    if Sistema in i and Portable in i and not Lagacy in i:
        FinalLinks = str(i)
    else:
        pass


class App:
    def __init__(self, root):
        width = 300
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)

        # setting title
        root.title("PolyUpdater")
        root.iconbitmap('launcher.ico')
        root.config(bg=_from_rgb((46, 52, 64)))
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # setting window size

        ft = tkFont.Font(family='Arial', size=10)

        my_img = ImageTk.PhotoImage(Image.open('logo.png'))
        My_label = Label(image=my_img, bg=_from_rgb((46, 52, 64)))
        My_label.photo = my_img
        My_label.pack(padx=25, pady=25)

        Info = Label(root)
        Info["text"] = "Your version is: %s" % Api_tag_name
        Info["bg"] = _from_rgb((46, 52, 64))
        Info["fg"] = _from_rgb((230, 230, 230))
        Info.pack()
        GButton_931 = Button(root)
        GButton_931["anchor"] = "center"
        GButton_931["bg"] = "#87b759"
        
        GButton_931["borderwidth"] = "0px"
        GButton_931["cursor"] = "mouse"
        GButton_931["font"] = ft
        GButton_931["fg"] = "#ffffff"
        GButton_931["justify"] = "center"
        GButton_931["text"] = "Update"
        GButton_931["relief"] = "flat"
        GButton_931.place(x=50, y=210, width=209, height=52)
        GButton_931["command"] = self.GButton_931_command

    def GButton_931_command(self):
        exeFile = "polymc.exe"
        local_file = "polyMC.zip"
        wget.download(FinalLinks, local_file)
        with ZipFile(local_file) as zf:
            zf.extractall()
            ZipFile.close(zf)
        try:
            os.system("cls")
        except:
            os.system("clear")
        os.remove(local_file)
        os.system("start %s" % exeFile)
        exit()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
