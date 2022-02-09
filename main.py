import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, messagebox, ttk
import os
import pyautogui
import time
import codecs


root = tk.Tk()
maps = []

username = os.getlogin()

SLEEP_SECONDS = 30

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
        maps = list(dict.fromkeys(maps))




def addMap():
    global frame

    for widgets in frame.winfo_children():
        widgets.destroy()

    filename = filedialog.askopenfilename(initialdir=r"C:\Users\{0}\Desktop\BUMM V1 Package\maps".format(username),
                                                      title="Select Map", filetypes=(("pictures", "*.png"), ("all files", "*.")))


    maps.append(filename)
    print(filename)


    for index, Map in enumerate(maps):
        list(dict.fromkeys(maps))
        file_label = tk.Label(frame, text=Map, bg="white")
        file_label.grid(row=index, column=1)
        openbutton = tk.Button(frame, text="Edit/View", padx=10, pady=5, fg="black", bg="#ffff00", command=openmap)
        openbutton.grid(row=index, column=2)


def openmap():
    for Map in maps:
        os.startfile(Map)


def createmap():
    try:
        os.startfile(r"C:\Users\{0}\Desktop\BUMM V1 Package\Krita (x64).lnk".format(username))
    except:
        os.startfile(r"C:\Users\{0}\Desktop\Krita (x64).lnk".format(username))


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
filemenu.add_command(label="Add Map", command=addMap)
filemenu.add_command(label="Create New Map", command=createmap)
filemenu.add_command(label="Exit", command=root.quit)

versionLabel = tk.Label(root, text="[BETA] Pre-Alpha V0.1 100% free and open source developed by the Paint Legion")
versionLabel.grid(row=1, column=1)

root.after(SLEEP_SECONDS*1000, autosave)
root.after(SLEEP_SECONDS*1000, automove)

root.mainloop()


with open('save.txt', 'w') as f:
    for Map in maps:
        f.write(Map + ',')
