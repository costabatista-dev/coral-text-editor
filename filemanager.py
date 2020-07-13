from tkinter import filedialog
import interfacemanager as im
import tkinter as tk


class fileManager:
    def __init__(self, interfaceWindow):
        self.text = ""
        self.interfaceWindow = interfaceWindow

    def setText(self):
        self.text = self.interfaceWindow.textWindow.get("1.0", "end-1c")

    def saveAs(self):
        self.setText(self.interfaceWindow)
        saveLocation = filedialog.asksaveasfilename()
        try:
            fileToSave = open(saveLocation, "w+")
            fileToSave.write(self.text)
            fileToSave.close()
            self.interfaceWindow.setFilePath(saveLocation)
            try:
                self.interfaceWindow.bottomBar.destroy
                self.interfaceWindow.setBottomBar()
            except NameError:
                self.interfaceWindow.setBottomBar()
        except Exception:
            self.interfaceWindow.setFilePath(None)

    def save(self, interfaceWindow):
        if interfaceWindow.filePath is None:
            self.saveAs(interfaceWindow)
        else:
            self.setText(interfaceWindow)
            fileToSave = open(interfaceWindow.filePath, "w+")
            fileToSave.write(self.text)
            fileToSave.close()
        try:
            interfaceWindow.bottomBar.destroy()
            interfaceWindow.setBottomBar()
        except NameError:
            interfaceWindow.setBottomBar()
