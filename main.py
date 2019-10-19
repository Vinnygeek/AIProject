import GA
import FileHandle as fh

myFileHandle = fh.FileHandle()

#myFileHandle.readAndWriteExample("files/LabirintoExemplo01.txt","files/solvedLabirintoExemplo01.txt")

newGA = GA.GA("files/LabirintoExemplo01.txt",10,2,56,0,13,27)
newGA.printConfigData()

#myfile = readFileWords("files/LabirintoExemplo01.txt")
#beginGA("labirinth","population","Crossoverindex","mutationindex","ngenerations")
