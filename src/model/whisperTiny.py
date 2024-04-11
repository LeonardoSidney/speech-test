from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline
import torch


class WhisperTiny:
    def __init__(self, file, language, task):
        self.file = file
        self.language = language
        self.task = task

    def processFile(self):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"

        pipe = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny",
            chunk_length_s=30,
            device=device,
        )

        args = {
            "language": self.language,
            "task": self.task,
        }

        prediction = pipe(
            self.file, batch_size=8, generate_kwargs=args, return_timestamps=True
        )

        return prediction
