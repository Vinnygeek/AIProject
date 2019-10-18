class FileHandle:    
    def readFileWords(self, filename):
        _labirinth = [] 
        with open(filename, 'r') as f:
                _lineFromFile = f.readlines()
                for line in _lineFromFile:
                    _line = []
                    for loneWords in line:
                        _line.append(loneWords.rstrip('\n')) 
                    _labirinth.append(_line)

        #Popping the empty character at the last position of the array.
        for _elem in _labirinth:
            _elem.pop()
        return _labirinth

    def fileWriting(self, file, strList):
        file = open(file,'w') 
        for i in strList:
            for _char in i:
                file.write(_char)
            file.write('\n')
        file.close()

    def readAndWriteExample(self,labirinth, solvedLabirinth):

        #Open a supost to be empty file
        myfile2 = self.readFileWords(labirinth)

        #Performe the GA on the myfile2 matrix

        #Saving the file after the GA manipulation
        self.fileWriting(solvedLabirinth,myfile2)

        #Opening and showing the solved Labirinth
        myfile3 = self.readFileWords(solvedLabirinth)
        for element in myfile3:
            print(element.__len__())
            print(element)

