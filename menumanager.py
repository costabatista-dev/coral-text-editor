import filemanager as fm
import interfacemanager as im
import tkinter as tk


class menumanager:
    def setMenuBar(self, interfaceWindow):
        fmanager = fm.fileManager(interfaceWindow)
        self.menubar = tk.Menu(interfaceWindow)
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Open",
                                  command=self.doNothing)
        self.fileMenu.add_command(label="Save as", command=self.doNothing)
        self.fileMenu.add_command(label="Save", command=self.doNothing)
        self.fileMenu.add_command(label="Exit", command=self.doNothing)
        self.settingsMenu = tk.Menu(self.menubar, tearoff=0)
        self.settingsMenu.add_command(label="Change color scheme",
                                      command=self.doNothing)
        self.helpMenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Settings", menu=self.settingsMenu)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)

    def doNothing(self):
        pass
