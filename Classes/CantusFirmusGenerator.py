__author__ = 'Iclavdivs'
from Classes.CantusFirmusFunction import CantusFirmusFunction
class CantusFirmusGenerator:
# new Class: cantusFirmusGenerator : is initialized with a cantusFirmusFunction
    #define function
    #cantusFirmusFunctionl 3 = CantusFirmusFunction()

    def __init__(self, domain):
        self.domain = domain
        self.cantusFirmusFunction = CantusFirmusFunction()

    #feed domain into function
    # return transformed domain
    def getCantusFirmus(self):
        cantusFirmus = []
        for x in self.domain:
            cantusFirmus.append (self.cantusFirmusFunction.defaultFunct(x))

        return cantusFirmus
