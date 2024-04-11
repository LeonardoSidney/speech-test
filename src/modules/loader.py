import argparse


class Loader:
    def __init__(self, *args):
        self.args = args
        self.parse_arguments()

    def parse_arguments(self):

        parser = argparse.ArgumentParser(
            description="É pra ajudar a processar o Whisper."
        )
        parser.add_argument(
            "--path", help="Caminho do video a ser legendado.", required=True
        )
        parser.add_argument(
            "--language",
            default="portuguese",
            help="Linguagem do video a ser legendado.",
        )
        parser.add_argument(
            "--task",
            default="transcribe",
            choices=["transcribe", "translate"],
            help="Tipo de tarefa a ser realizada no video a ser legendado.",
        )
        parser.add_argument("--output", help="Caminho do arquivo de saída.")
        parser.add_argument(
            "--gpu",
            help="Seleciona a GPU para processamento, sem gpu se vou assumir que a CPU vai processar",
            default=False,
            choices=["amd", "nvidia"],
        )
        parser.add_argument(
            "--extension",
            help="Extensão de saída do arquivo",
            choices=["txt", "srt"],
            required=True
        )
        parser.add_argument(
            "--model",
            help="Modelo a ser utilizado",
            default="openai/whisper-tiny",
            choices=["openai/whisper-large-v3", "openai/whisper-tiny"],
        )
        self.args = parser.parse_args()

    def getArgs(self):
        return self.args
