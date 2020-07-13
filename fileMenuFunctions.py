from tkinter import filedialog
import documentManager


def getFileContent():
    dmObject = documentManager.DocumentManager()
    dmObject.set_filePath(filedialog.askopenfilename())
    try:
        with open(dmObject.get_filePath()) as content:
            dmObject.set_fileContent(content.read())
    except Exception:
        dmObject.set_filePath()
        dmObject.set_fileContent()
    return dmObject
