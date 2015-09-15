#i want to take a function customFunction.getFunction
#quantize it to a specific set of numbers that represent "available" notes
#	noteQuantizer.getQuantizedNote
# Then feed this quantized output into an accompGen.calcAccomp(x...) that outputs a corresponding note.

##For singple point of X 
# cantusFirmusFunct : f(x) = 1 
# quant : g(x) = [0-6], where [0 = A, ... 6 = G]
	#Limiting range to 1 octave for the initial
# counterPointFunction : h(x) = x + 2
# timeSignature = [1:1] ## quarter: 1/4 * 4 = 1, ## [4:3] : quarter 1/4 * 3 = 3/4###
# measureInput = [0...inputRange] # more details later
			## timesig = [a:b]
			## space of a measure is 1/a * b = d (distance in measure)
			## 
			## meaning increments will be  in n sets of b:
			##   (1/a) / d, ... , ( n * b)(1/a) / d
			## How will I allow for accidentals? Answer later
# input: 2
# output: 
#	x: [0,1,2]
#	CantusFirmus: [B,B,B]
#	CounterPoint: [D,D,D]

from Classes.NoteQuantizer import NoteQuantizer
from Classes.CounterPointGenerator import CounterPointGenerator
from Classes.CantusFirmusGenerator import CantusFirmusGenerator


def testCompose():
	x = range(0,3)
	cfGenerator = CantusFirmusGenerator(x)
	cpGenerator = CounterPointGenerator(cfGenerator.getCantusFirmus())
	quantizer = NoteQuantizer()
	quantizer.constructOctaveMap()
	
	print("Composed!")
	print("x: ",x)
	print("Cantus Firmus: ",cfGenerator.getCantusFirmus())#TODO: quantize
	print("Counter Point: ", cpGenerator.getCounterPoint())#TODO: quantize
	print("\nnote names\n")
	
	print("Cantus Firmus: ",quantizer.quantizeRangeToNotes(cfGenerator.getCantusFirmus()))#TODO: quantize
	print("Counter Point: ", quantizer.quantizeRangeToNotes(cpGenerator.getCounterPoint()))#TODO: quantize



testCompose()
