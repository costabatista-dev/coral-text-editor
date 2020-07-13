class DocumentManager:
    def __init__(self):
        self.set_filePath()
        self.set_fileContent()

    def set_filePath(self, path=None):
        self.filePath = path

    def get_filePath(self):
        return self.filePath

    def set_fileContent(self, fileContent=None):
        self.fileContent = fileContent

    def get_fileContent(self):
        return self.fileContent

    def set_isSavedContent(self, isSaved=False):
        self.isSaved = isSaved

    def get_isSavedContent(self):
        return self.isSaved
