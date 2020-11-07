#
# Class to read and convert text to uppercase
#
class CaseConverter:
    def __init__(self):
        self.words = []

    def getString(self):
        self.words = ['Hasta', 'la', 'vista', 'baby']

    def printString(self):
        for i in range(len(self.words)):
           self.words[i] = self.words[i].upper()

        print(len(self.words))
        print(self.words, sep='T')

test = CaseConverter()
test.getString()
test.printString()