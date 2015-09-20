__author__ = 'Iclavdivs'
# new Class: counterPointGenerator : is initialized with a counterPointFunction and noteQuantizer
from Classes.CounterPointFunction import CounterPointFunction

class CounterPointGenerator:
    #define function

    #For the time being, I'm going to apply the quantization to real notes outside of the classes. In the future, I may want to start using more complex analysis to create accompaniment, like take derivatives

    def __init__(self, domain):
        self.domain = domain
        self.counterPointFunction = CounterPointFunction()

    #feed domain into function
    # return transformed domain
    def getCounterPoint(self):
        counterPoint = []
        for x in self.domain:
            counterPoint.append (self.counterPointFunction.defaultFunct(x))

        # self.counterPoint = counterPoint

        return counterPoint