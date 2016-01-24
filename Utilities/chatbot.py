#coding: utf-8
# AI Command
# By the Tutorial Doctor
# Wednesday September 02, 2015 (age relative to this)
# Only add valid commands to the memory
# a single command can trigger several functions
#------------------------------------------------------------------------------
class AI(object):
	pass
#------------------------------------------------------------------------------


# GLOBAL VARIABLES
#------------------------------------------------------------------------------
memory = ['null']
username = raw_input('What is your name? ')

# Fuzzy Data
cold = (0,60)
high = (10,60)
it = 32 # current value

#------------------------------------------------------------------------------

# AI Traits
#------------------------------------------------------------------------------
import sys
ai = AI()
ai.age = 1
ai.creationday = 'Wednesday September 02, 2015'
ai.__name__ = 'TD001' #__ means DON'T' TOUCH!
# But you can touch it anyway :)
ai.weight = str(sys.getsizeof(ai)) + ' bytes'
ai.info = 'My name is {}. I am {}. I was created on {} by The Tutorial Doctor. I am currently {} and not ashamed.'.format(ai.__name__,ai.age,ai.creationday,ai.weight)
#------------------------------------------------------------------------------


# Main Loop
#------------------------------------------------------------------------------
def Main():
	displayCommands()
	running=True
	while running:
		command=raw_input('Type a command %s:'%username).upper()
		
		if command=='STOP':
			print '{} Terminated'.format(ai.__name__)
			return False  
			
		prompt(command)
#------------------------------------------------------------------------------


# The Shell
#------------------------------------------------------------------------------
def prompt(c):
	greet(c)
	checkMemory(c)
	dates(c)
	eraseConsole(c)
	askInfo(c)
	randomStatement(c)
	train(c)
	Fuzz(c)
#------------------------------------------------------------------------------


# AI (Add your own functions here)
#------------------------------------------------------------------------------
import random,datetime,console

def displayCommands():
	print('\n')
	print('Console: erase,stop')
	print('Memory: mem,memory,int()')
	print('Personality: rant')
	print('Info: info,age,name,birthday,weight')
	print('Date: date,day,month,year')
	print('Ask: good/evil,')
	print('FuzzyLogic: cold?,high?')
	print('\n')

def greet(c):
	greetings=['HELLO','HI','HOLA','KONNICHIWA']
	if c in greetings:
		greeting = greetings[random.randint(0,3)].capitalize() + ' ' + username
		block = (c,greeting)
		print greeting
		memory.append(block)

def checkMemory(c):
	if c in ['MEMORY','MEM']:
		print(str(len(memory)) + ' ' + str(memory))

	try:
		print(memory[int(c)])
	except:
		None 
		
def askInfo(c):
	# perhaps use all() or any()?
	# not working (and)
	if c == 'AGE':
		print('I am {}.').format(ai.age)
	if c == 'NAME':
		print('My name is {}'.format(ai.__name__))
	if c in ['BIRTH','BIRTHDAY']:
		print('I was created on {}'.format(ai.creationday))
		if ai.creationday == datetime.date.today().strftime('%A %B %d, %Y'):
			print("It's my creationday!")
	if c in ['SIZE','WEIGHT','SZ']:
		print 'I am ' + ai.weight
	if c in ['INFO','NFO']:
		print ai.info
		
	#subtract add dates?

def dates(c):
	"""
	#%b month abbreviation
	#%B full month name
	#%h month abbreviation
	#%y two digit year
	#%Y four digit year
	#%a day of the week abbreviation
	#%A day of the week
	#%d date
	#%m minutes
	#%s seconds
	#%s am/pm
	#%c date & time
	"""
	today = datetime.date.today()
	year = today.year
	month = today.month
	day = today.day
	#Add times later	
	
	if c=='DAY':
		print 'It is ' + today.strftime('%A ') + username
	elif c=='MONTH':
		print 'It is ' + today.strftime('%B ') + username
	elif c=='YEAR':
		print 'It is ' + today.strftime('%Y ') + username
	elif c=='TIME':
		pass
		#print datetime.time()
	elif c == 'TODAY':
		pass
	elif c == 'DATE':
		print 'It is ' + today.strftime('%A %B %d, %Y ') + username

def eraseConsole(c):
	if c in ['...','ER','ERASE']:
		print('o')
		console.clear()

def randomStatement(c):
	if c in ['RAN','RANT','RANDOM']:
		s1 = 'Follow me on Twitter @TutorialDoctor'
		s2 = 'Python is a cool programming language!'
		s3 = 'What goes up, must come down. Unless it has 0 gravity of course.'
		s4 = 'The grass is always greener on the other side. So true for deserts.'
		s5 = 'Haha, that is such a blooper.'
		s6 = 'WHO YOU CALLING FAT!. I am only {}'.format(ai.weight)
		s = [s1,s2,s3,s4,s5,s6]
	
		print random.choice(s)

def train(c):
	moral_data = {'GOOD':True,'EVIL':False}
	if c in moral_data:
		print moral_data[c]
		block = (c,moral_data[c])
		memory.append(block)

# Fuzzy Logic
#------------------------------------------------------------------------------
def Membership(x,List):
	"Returns the membership of a value in a list."
	top=(float(x)-List[0])
	bottom=(List[-1]-List[0])
	M= top/bottom
	return M
	
def Is(x,List):
	"Returns true if a value is in the value range of a list"
	#If a value is greater than the first item in a list..
	if x >= List[0]:
		#And if it is smaller than the last item in the list...
		if x<= List[-1]:
			#print the membership of the item in the list...
			print Membership(x,List)
			#And return True
			return True
	#No else statement is needed since the return statement will exit the function.
	#Print the membership and return False if the above condition is false.
	print Membership(x,List)
	return False

def Fuzz(c):
	if c == 'COLD?':
		print Is(it,cold)
	if c == 'HIGH?':
		print Is(it,high)
#------------------------------------------------------------------------------
Main()



