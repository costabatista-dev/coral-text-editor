import tkinter as tk
from bottomBarType import bottomBarType
import fileMenuFunctions as menufunction


class CoralInterface:

    def __init__(self):
        self.initializeRoot()
        self.addTextWindow()
        self.bottomBarType = bottomBarType.textBar
        self.set_filePath()
        self.addBottomBar()
        self.loadMenu()

    def initializeRoot(self):
        self.root = tk.Tk()
        title = "Coral text editor"
        self.root.title(title)
        self.root.geometry()
        self.root.bind('<Escape>', self.changeBottomMode)
        # root.protocol("WM_DELETE_WINDOW", quit)
        # return root
    
    def set_filePath(self, filePath=None):
        self.filePath = filePath
    
    def get_filePath(self):
        return self.filePath

    def addTextWindow(self):
        self.textWindow = tk.Text(self.root)
        self.textWindow.pack(fill=tk.BOTH, expand=tk.YES)
        # return text

    def addBottomBar(self):
        if self.bottomBarType == bottomBarType.textBar:
            bottomBarText = ("Unnamed document" if self.filePath is None
                             else self.filePath)
            self.textWindow.config(state=tk.NORMAL)
            self.bottomBar = tk.Label(self.root, text=bottomBarText)
            self.textWindow.focus()
            self.bottomBar.pack()
        else:
            self.bottomBar = tk.Entry(self.root)
            self.textWindow.config(state=tk.DISABLED)
            self.bottomBar.pack(fill=tk.X)
            self.bottomBar.focus()

    def changeBottomMode(self, event):
        try:
            self.bottomBar.destroy()
        except NameError:
            print("bottomBar is not defined in CoralInterface instance")
        if self.bottomBarType == bottomBarType.textBar:
            self.bottomBarType = bottomBarType.commandBar
            self.addBottomBar()
        else:
            self.bottomBarType = bottomBarType.textBar
            self.addBottomBar()

    def initializeMenuBar(self):
        self.menubar = tk.Menu(self.root)

    def configureMenuBar(self):
        self.root.config(menu=self.menubar)

    def addFileMenu(self):
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.__openFile)
        self.fileMenu.add_command(label="Save as", command=self.doNothing)
        self.fileMenu.add_command(label="Save", command=self.doNothing)
        self.fileMenu.add_command(label="Exit", command=self.doNothing)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

    def loadMenu(self):
        self.initializeMenuBar()
        self.addFileMenu()
        self.configureMenuBar()

    def setTextWindowContent(self, content):
        self.textWindow.delete(1.0, tk.END)
        self.textWindow.insert(tk.END, content)

    def __openFile(self):
        dmObject = menufunction.getFileContent()
        fileContent = dmObject.get_fileContent()
        filePath = dmObject.get_filePath()
        self.set_filePath(filePath)
        self.setTextWindowContent(fileContent)
        try:
            self.bottomBar.destroy()
        except Exception:
            print("Cannot destroy bottombar")
        self.addBottomBar()
        self.root.update()

    def showInterface(self):
        self.root.mainloop()

    def doNothing(self):
        pass
