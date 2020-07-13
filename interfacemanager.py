import tkinter as tk
import menumanager as menu


class interface:
    def __init__(self):
        self.setFilePath()
        self.setIsEntry()
        self.setMainWindow()
        self.setTextWindow()
        self.setBottomBar()
        self.setMenuItens()

    def setIsEntry(self, isEntry=False):
        self.isEntry = isEntry

    def setFilePath(self, filePath=None):
        self.filePath = filePath

    def changeBottomBar(self, event):
        try:
            self.bottomBar.destroy()
            self.setIsEntry(not self.isEntry)
            self.setBottomBar(self.isEntry)
        except NameError:
            self.setIsEntry(not self.isEntry)
            self.setBottomBar(self.isEntry)
        self.mainWindow.update()

    def setTextWindow(self):
        self.textWindow = tk.Text(self.mainWindow)
        self.textWindow.pack(fill=tk.BOTH, expand=tk.YES)
        self.mainWindow.update()

    def setBottomBar(self, isEntry=False):
        if isEntry is False:
            if self.filePath is None:
                textValue = "Unnamed document"
            else:
                textValue = self.filePath

            self.bottomBar = tk.Label(self.mainWindow, text=textValue)
            self.textWindow.config(state=tk.NORMAL)
            self.textWindow.focus()
            self.bottomBar.pack()
        else:
            self.bottomBar = tk.Entry(self.mainWindow)
            self.textWindow.config(state=tk.DISABLED)
            self.bottomBar.pack(fill=tk.X)
            self.bottomBar.focus()
        self.mainWindow.update()

    def setMenuItens(self):
        self.menuItens = menu.menumanager()
        self.menuItens.setMenuBar(self.mainWindow)
        self.mainWindow.config(menu=self.menuItens.menubar)
        

    def setMainWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Coral Text Editor")
        self.mainWindow.geometry()
        self.mainWindow.bind('<Escape>', self.changeBottomBar)
        self.mainWindow.protocol("WM_DELETE_WINDOW", quit)
