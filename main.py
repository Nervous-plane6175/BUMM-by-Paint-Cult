import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, messagebox, ttk
import os
import pyautogui
import time


root = tk.Tk()
maps = []
selected_maps = []
username = os.getlogin()

SLEEP_SECONDS = 30

root.grid_columnconfigure(10, minsize=100)

def autosave():
    pyautogui.keyDown("Ctrl")
    pyautogui.press("s")
    pyautogui.keyUp("Ctrl")
    pyautogui.press("Enter")
    print('Saving...')


def automove():
    try:
        targetfolder = r"C:\Users\{0}\Desktop\BUMM V1 Package\Maps".format(username) + "\\"
        sourcefolder = r"C:\Users\{0}\Pictures".format(username) + "\\"
        for path, dir, files in os.walk(sourcefolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetfolder + file):
                        os.rename(path + "\\" + file, targetfolder + file)
    except Exception as e:
        print(e)


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempMaps = f.read()
        tempMaps = tempMaps.split(',')
        maps = [x for x in tempMaps if x.strip()]



class SelectLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected = False
        self.bind("<Enter>", self.highlight)
        self.bind("<Leave>", self.dehighlight)
        self.bind("<Button-1>", self.on_click)

    def on_click(self, e):
        self.selected = not self.selected

    def highlight(self, e):
        self.config(bg="blue", fg="white")

    def dehighlight(self, e):
        if not self.selected:
            self.config(bg="white", fg="black")


def addMap():
    global frame

    filename = filedialog.askopenfilename(initialdir=r"C:\Users\{0}\Desktop\BUMM V1 Package\maps".format(username),
                                                      title="Select Map", filetypes=(("pictures", "*.png"), ("all files", "*.")))
    maps.append(filename)
    print(filename)
    maps2 = list(dict.fromkeys(maps))

    for index, Map in enumerate(maps2):
        label = SelectLabel(frame, text=Map)
        label.grid(row=index, column=10)
        selected_maps2 = [x for x in maps2 if x.selected]
    selected_maps.append(selected_maps2)


def openmap():
    for Map in selected_maps:
        os.startfile(Map)


def createmap():
    os.startfile(r"C:\Users\{0}\Desktop\BUMM V1 Package\Krita (x64).lnk".format(username))


def delete_maps():
    os.remove("save.txt")


def button_save_1():
    bs1 = tk.Button(frame, text="Delete Maps", padx=10, pady=5, fg="black", bg="#ffff00", command=deldel)
    bs1.place(x=1350, y=100)


def deldel():
    for widget in frame.winfo_children():
        widget.destroy()

    button_save_1()

    os.remove("save.txt")

def deldel2():
    for widget in frame.winfo_children():
        widget.destroy()

    if os.path.exists("save.txt"):
        open("save.txt", "w").close()

    maps.clear()



root.title("BUMM Pre-alpha 0.1")
root.iconbitmap('BUMM Logo 1.ico')

canvas = tk.Canvas(root, height=800, width=1500, bg="#ffff00")

canvas.grid()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

navmenu = tk.Menu(root)
root.config(menu=navmenu)

filemenu = tk.Menu(navmenu, tearoff=0)

navmenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Delete All Maps", command=deldel2)
filemenu.add_command(label="Exit", command=root.quit)

versionLabel = tk.Label(root, text="[BETA] Pre-Alpha V0.1 100% free and open source developed by the Paint Legion")
versionLabel.grid(row=1, column=1)

openMap = tk.Button(root, text="Add Map", padx=10, pady=5, fg="black", bg="#ffff00", command=addMap)
openMap.grid(row=3, column=0)
createMap = tk.Button(root, text="Create map", padx=10, pady=5, fg="black", bg="#ffff00", command=createmap)
createMap.grid(row=2, column=0)
editMap = tk.Button(root, text="Edit map", padx=10, pady=5, fg="black", bg="#ffff00", command=openmap)
editMap.grid(row=1, column=0)
root.after(SLEEP_SECONDS*1000, autosave)
root.after(SLEEP_SECONDS*1000, automove)


root.mainloop()



with open('save.txt', 'w') as f:
    for Map in maps:
        f.write(Map + ',')





