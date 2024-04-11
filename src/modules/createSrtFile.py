class CreateSrtFile:
    def __init__(self, responseModel):
        self.chunks = responseModel['chunks']
        self.text = ""
        self.convertFileToSrt()

    def convertFileToSrt(self):
        for sequence, chunk in enumerate(self.chunks):
            timestamp = chunk["timestamp"]
            self.text += self.formatText(sequence, timestamp, chunk["text"])

    def formatText(self, sequence, timestamp, text):
        subtitle = ""
        start, end = timestamp
        start = self.format_timestamp(start)
        end = self.format_timestamp(end)
        subtitle += f"{sequence}\n"
        subtitle += f"{start} --> {end}\n"
        subtitle += f"{text.strip()}\n\n"
        return subtitle

    def format_timestamp(self, timestamp):
        if timestamp is None:
            return "00:00:00,000"
        
        hours = int(timestamp // 3600)
        minutes = int((timestamp % 3600) // 60)
        seconds = int(timestamp % 60)
        milliseconds = int((timestamp % 1) * 1000)
        formatted_timestamp = (
            f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
        )

        return formatted_timestamp

    def writeToDisk(self, filename):
        with open(filename, "w") as file:
            file.write(self.text)
        return

    def getFile(self):
        return self.text