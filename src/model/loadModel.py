from model.whisperLarge import WhisperLarge
from model.whisperTiny import WhisperTiny

class LoadModel:
    def __init__(self, model, gpu, file, language, task):
        self.model = model
        self.gpu = gpu
        self.file = file
        self.language = language
        self.task = task
        self.loadModel()

    def loadModel(self):
        if self.gpu == False:
            pass
        if self.model == "openai/whisper-large-v3":
            self.model = WhisperLarge(self.file, self.language, self.task)
        if self.model == "openai/whisper-tiny":
            self.model = WhisperTiny(self.file, self.language, self.task)

    def processFile(self):
        return self.model.processFile()
