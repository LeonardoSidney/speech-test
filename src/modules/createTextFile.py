class createTextFile:
    def __init__(self, path, responseModel):
        self.path = path
        self.text = responseModel['text']

    def writeToDisk(self):
        with open(self.path, "w") as file:
            file.write(self.text)
