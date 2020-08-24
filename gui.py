import tkinter as tk
from tkinter import ttk

from getMutatorInfo import getWorkShopInfo
from getId import getWorkShopId

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Workshop ID/URL: ")
        self.label.pack(side="top")
        
        self.entry = tk.Entry(self)
        self.entry.pack(side="top")


        self.search = tk.Button(self)
        self.search["text"] = "Search"
        self.search["command"] = self.searchForId
        self.search.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def searchForId(self):

        id = getWorkShopId(self.entry.get())
        name, size, date = getWorkShopInfo(id)
        print(id)
        print(name)
        print(size)
        print(date)

        modlabel = name + ' (' + size + ') '
        
        self.new_progress_bar = tk.ttk.Progressbar(self)
        self.new_progress_bar.pack(side="right")

        self.remove_mod = tk.Button(self, text="Remove")
        self.remove_mod.pack(side="right")

        self.new_button = tk.Button(self, text="Download")
        self.new_button.pack(side="right")

        self.mod_label = tk.Label(self, text=modlabel)
        self.mod_label.pack(side="right")

        self.new_checkbox = tk.Checkbutton(self)
        self.new_checkbox.pack(side="left")

        
root = tk.Tk()
app = Application(master=root)
app.master.title("KF2 Mod Manager")
app.mainloop()