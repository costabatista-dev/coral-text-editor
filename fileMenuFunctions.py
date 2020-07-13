from tkinter import filedialog
from documentManager import DocumentManager


def getFileContent():
    dmObject = DocumentManager()
    dmObject.set_filePath(filedialog.askopenfilename())
    try:
        with open(dmObject.get_filePath()) as content:
            dmObject.set_fileContent(content.read())
    except Exception:
        dmObject.set_filePath()
        dmObject.set_fileContent()
    return dmObject


def saveFileContentAs(content=""):
    dmObject = DocumentManager()
    filePath = filedialog.asksaveasfilename()
    dmObject.set_filePath(filePath)
    dmObject.set_fileContent(content)
    try:
        fileToSave = open(dmObject.get_filePath(), "w+")
        fileToSave.write(dmObject.get_fileContent())
        fileToSave.close()
    except Exception:
        dmObject.set_filePath()
        dmObject.set_fileContent()
    return dmObject
