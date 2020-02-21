from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def doNothing():
    x = 0


def isModifiedText():
    global text, filePath

    t = text.get("1.0", "end-1c")

    if ((filePath is None) and (len(t) > 0)):
        return True
    if ((filePath is None) and (len(t) == 0)):
        return False

    with open(filePath) as f:
        tf = f.read()
    return False if t == tf else True


def quit():
    global mainWindow, filePath
    modifiedText = isModifiedText()
    
    if modifiedText:
        isToSaveDocument = messagebox.askyesnocancel(title="Close - Save document", 
        message="The document was modified. Do you want save it?", parent=mainWindow)

        if isToSaveDocument:
            if filePath is None:
                saveAs()
            else: 
                save()
        elif isToSaveDocument is None:
            return

    mainWindow.quit()
    mainWindow.destroy()


def createMainWindow():
    root = Tk()
    root.title("Coral Text Editor")
    root.geometry();
    root.bind('<Escape>', changeBottom)
    root.protocol("WM_DELETE_WINDOW", quit)
    return root


def addTextWidget(mainWindow):
    text=Text(mainWindow)
    text.pack(fill=BOTH, expand=YES)
    return text


def addSaveButton(mainWindow):
    button = Button(mainWindow, text="Save", command=saveAs)
    button.pack(side=RIGHT, padx=5, pady=5)


def addOpenButton(mainWindow):
    button = Button (mainWindow, text="Open")
    button.grid()


def saveAs():
    global filePath, bottomBar
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    try:
        file1 = open(savelocation, "w+")
        file1.write(t)
        file1.close()
        filePath = savelocation
        bottomBar.destroy()
        setBottomBar()
    except Exception:
        filePath = None


def save():
    global filePath
    t = text.get("1.0", "end-1c")
    if filePath is None:
        saveAs()
    else:
        file1 = open(filePath, "w+")
        file1.write(t)
        file1.close()
        bottomBar.destroy()
        setBottomBar()


def setText(value):
    global mainWindow
    text.delete(1.0, END)
    text.insert(END, value)


def openFile():
    global filePath, bottomBar
    
    openlocation = filedialog.askopenfilename()
    try: 
        with open(openlocation) as f: 
            t = f.read()
    except Exception:
        openlocation = None
        t = ""
    filePath = openlocation
    bottomBar.destroy()
    setBottomBar()
    setText(t)
    
    


def addMenuBar(root):
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save as", command=saveAs)
    fileMenu.add_command(label="Save", command=save)
    fileMenu.add_command(label="Exit", command=quit)
    
    settingsMenu = Menu(menubar, tearoff=0)
    settingsMenu.add_command(label="Change color scheme", command=doNothing)
    
    helpMenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Settings", menu=settingsMenu)
    menubar.add_cascade(label="Help", menu=helpMenu)
    return menubar


def changeBottom(event):
    global mainWindow, isEntry, bottomBar
    bottomBar.destroy()
    if isEntry == False:
        isEntry = True
        setBottomBar(isEntry)
    else: 
        isEntry = False
        setBottomBar(isEntry)

def setBottomBar(isEntry=False):
    global bottomBar, mainWindow, filePath, text
    
    if isEntry == False:
        bottomBar = Label(mainWindow, text="Unnamed document" if filePath is None else filePath)
        text.config(state=NORMAL)
        text.focus()
        bottomBar.pack()
    else:
        bottomBar = Entry(mainWindow)
        text.config(state=DISABLED)
        bottomBar.pack(fill=X)
        bottomBar.focus()
    mainWindow.update()

def main():
    global text, filePath, mainWindow, isEntry, bottomBar
    filePath = None
    isEntry = False
    mainWindow = createMainWindow();
    text = addTextWidget(mainWindow)
    setBottomBar(isEntry)
    menubar = addMenuBar(mainWindow)
    
    mainWindow.config(menu=menubar)
    mainWindow.mainloop()

    
if __name__ == '__main__':
    main()