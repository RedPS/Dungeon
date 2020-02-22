import tkinter as tk
from tkinter import filedialog, Text 
import os 

# the body, the whole structure 
root = tk.Tk()

apps = []

'''
adding the app
'''
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(("executetables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    # print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()

'''
Running the app
'''
def runApps():
    for app in apps:
       os.startfile(app) 

'''
# for linux or MacOS
def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener,app])
'''
# create a canvas to get a better environment in the root 
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attach the canvas 
canvas.pack()

# attach another container to the canvas 
frame = tk.Frame(root, bg="white")
# place it and center it 
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

# Button for opening files 
openFile = tk.Button(root, text="Open File", padx=10, 
                     pady=5, fg="white", bg="red", command=addApp)
openFile.pack()

# Button for running apps 
RunApps = tk.Button(root, text="Run Apps", padx=10, 
                    pady=5, fg="white", bg="red", command=runApps)
RunApps.pack()

root.mainloop()
