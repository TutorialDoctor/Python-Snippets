# By the Tutorial Doctor
# Mon Aug 24 19:45:19 EDT 2015

# This is the start of a simple custom command line python script

import random
import datetime
import editor
import os
#------------------------------------------------------------------------------
name = raw_input('What is your name? ')
files = []
#------------------------------------------------------------------------------


# Main Loop
#------------------------------------------------------------------------------
def Main():
	displayCommands()
	running=True
	
	while running:
		command=raw_input('Type a command %s:'%name).upper()
		
		if command=='STOP':
			print '...Terminated'
			return False  
		
		prompt(command)
#------------------------------------------------------------------------------


# The Shell
#------------------------------------------------------------------------------
def prompt(c):
	
	#ADD COMMANDS HERE:
	dates(c)
	greet(c)
	mood_changers(c)
	OS(c)
	
	if c=='LIST':
		list_files()
	elif c=='FILE':
		new_file()
	elif c=='PRINT':
		display()
	elif c=='MOOD':
		mood()
#------------------------------------------------------------------------------


# Functions
#------------------------------------------------------------------------------	
def displayCommands():
	print
	print 'COMMAND LIST\n'+'-'*79
	print 'Key Commands: stop,print,file'
	print 'Greetings: hello,hi,hola,konnichiwa'
	print 'Dates: date,day,month,year,today'
	print 'Personal: mood'
	print 'OS: path,folder,folders'
	print '-'*79
	print
	
def greet(c):
	greetings=['HELLO','HI','HOLA','KONNICHIWA']
	if c in greetings:
		print greetings[random.randint(0,3)].capitalize() + ' ' + name

def display():
	output=raw_input('Print what? ')
	print output
		
def mood():
	moods =['happy','normal','sad']
	mood = moods[random.randint(0,2)].capitalize()
	print mood
	return mood
		
def mood_changers(c):
	insults=['STUPID','DUMB']
	compliments=['PRETTY']
	cloudy=False
	hungry=False
	clean=False
	insulted=False
	delighted=False 
			
	if c in insults:
		insulted = True
	if c in compliments:
		delighted = True
	
	if insulted:
		print '%s is a bad word.'%cmnd
	if delighted:
		print 'thank you for saying %s'%cmnd

# This can be made more compact with a 'with' statement				
def new_file():
	file_name=raw_input('File name: ')+'.txt'
	file = open(file_name,'w')
	text=raw_input('What to write: ')
	file.write(text)
	file.close()
	files.append(file_name)
	answer=raw_input('Read the file? ')
	if answer.upper() == 'Y':
		file=open(file_name,'r')
		print file.read()
	else:
		print 'File not read'
		print 'Files: %s'%files

def newFolder(name):
	this_directory=os.getcwd()
	try:
		new_directory = os.mkdir(this_directory+'/{}'.format(name))
		print('Directory created.')
	except:
		print('Directory already exists.')
	
def newFolders(folders):
	this_directory=os.getcwd()
	# Create multiple directories
	try:
		os.makedirs(this_directory+'/{}'.format(folders))
		print('Directories created.')
	except:
		print('Those directories already exist.')

		
def dates(c):
	"""
	#%b month abbroviation
	#%B full month name
	#%y two digit year
	#%Y four digit year
	#%a day of the week abbreviates
	#%A day of the week
	#%d date
	"""
	today = datetime.date.today()
	year = today.year
	month = today.month
	day = today.day
	#Add times later	
	
	if c=='DAY':
		print today.strftime('%A')
	elif c=='MONTH':
		print today.strftime('%B')
	elif c=='YEAR':
		print today.strftime('%Y')
	elif c=='TIME':
		pass
	elif c == 'TODAY':
		print today
	elif c == 'DATE':
		print today.strftime('%A %B %d, %Y')
			
def list_files():
	print files			

def confirm(x):
	if x.upper() in ['Y','YES']:
		return True 
	elif x.upper() in ['N','NO'] :
		return False
		
def OS(c):
	if c == 'PATH':
		print(os.path)

	# Create a directory/folder in a path
	if c == 'FOLDER':
		name=raw_input('Name: ')
		newFolder(name)
	if c=='FOLDERS':
		print 'Example: A/B/C'
		names=raw_input('Names: ')
		newFolders(names)
#------------------------------------------------------------------------------

if __name__ == '__main__':
	Main()

