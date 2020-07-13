class DocumentManager:
    def __init__(self):
        self.set_filePath()

    def set_filePath(self, path=None):
        self.filePath = path

    def get_filePath(self):
        return self.filePath

    def set_fileContent(self, fileContent=None):
        self.fileContent = fileContent

    def get_fileContent(self):
        return self.fileContent
