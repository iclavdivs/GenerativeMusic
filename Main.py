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
	

# new Class: cantusFirmusFunction
class CantusFirmusFunction:
	def defaultFunct(self, input ):
		return 1
		
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
	

# new Class: noteQuantizer
###DOES NOT WORK
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
	

# new Class: counterPointFunction
class CounterPointFunction:
	def defaultFunct(self, input ):
		return input+2
# new Class: counterPointGenerator : is initialized with a counterPointFunction and noteQuantizer

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
	
	


	
	
	