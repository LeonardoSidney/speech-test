from modules.loader import Loader
from model.loadModel import LoadModel
from modules.createSrtFile import CreateSrtFile
from modules.createTextFile import createTextFile

def main():
    loader = Loader()
    args = loader.getArgs()
    model = LoadModel(args.model, args.gpu, args.path, args.language, args.task)
    if args.extension == 'txt':
        createFile = createTextFile(args.path, model.processFile())
        createFile.writeToDisk
        pass
    if args.extension == 'srt':
        createFile = CreateSrtFile(model.processFile())
        if args.output is None:
            createFile.writeToDisk(f"{args.path}.srt")

if __name__ == "__main__":
    main()
