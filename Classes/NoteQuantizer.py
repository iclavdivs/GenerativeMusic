__author__ = 'Iclavdivs'
# new Class: noteQuantizer
class NoteQuantizer:


    mini = 0
    maxi = 7

    def __init__(self):
        self.quant = {}
        #self.constructOctaveMap()

    def constructOctaveMap(self):

        for x in range(self.mini,self.maxi):
            self.quant[x] = chr( ord('A') + x)


    def quantizeToNumber(self,x):
        if x <= min:
            return min
        elif x >= max:
            return max
        else:
            return x

    def quantizeToNote(self,x):
        if x in self.quant.keys():
            return self.quant[x]
        return 'n'

    def quantizeRangeToNotes(self,domain):
        quantizedNotes = []
        for x in domain:
            quantizedNotes.append(self.quantizeToNote(x))

        return quantizedNotes
