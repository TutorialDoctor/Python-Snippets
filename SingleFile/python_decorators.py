# A decorator is a function that takes a function as an argument and adds a bow tie on top of it.
def decorator(func):
	return func
#This "decorator" doesn't really decorate the input function. It just returns the input function.

@decorator
def aFunc():
	print('hello\n')
aFunc()



#The decorator above doesn't have a bow tie. Let's create a decorator that can decorate an input function with a bowtie.
def decorate_with_bowtie(func):
	print('>-<') 
	#This bow tie could be whatever logic you want it to be. The key is that the bow tie code is executed "before" (on top of) the input-function.
	return func

@decorate_with_bowtie
def aFunc2():
	print('I am decorated with a bow tie')
aFunc2()

#I can decorate multiple functions with a bow tie now
@decorate_with_bowtie
def aFunc3():
	print('I am decorated with a bow tie also')
aFunc3()



# Now we are going to wrap the input function and add a bow tie to it
def wrap_and_tie(func):
	def wrapped():
		#Bow tie
		print('>-<')
		#Call the function
		func()	
		print('..Your function has been wrapped and bow-tied')
	#Return the wrapped function
	return wrapped

@wrap_and_tie
def aFunc4():
	print('gift')
aFunc4()



#Decorate a divide function with a check for a valid denominator value.
def prevent_divide_by_zero(func):
	#To pass the arguments of the function to the wrapper:
	def wrapped(*args,**kwargs):
		#If the 2nd argument is not 0:
		denominator = args[1]
		if denominator !=0: 
			print("The quotient is:")
			#Call the input-function, passing in the keyword arguments
			func(*args,**kwargs)
		#Otherwise print that they cannot divide by zero.
		else:
			print("Can't divide by 0")
	#Return the wrapped function
	return wrapped

@prevent_divide_by_zero
def divide(a,b):
	print(a/b)

divide(20,0)
divide(20,6.0)



#Now for something more useful. Decorate an attempt to create a user with a user validation
def validate_user(func):
	def wrapped(*args,**kwargs):
		#If the username argument is 'admin' and the password argument is 'password':
		if kwargs['username']=='admin' and kwargs['password']=='password':
			print('ACCESS GRANTED: \n{}'.format(kwargs))
			#execute the input-function
			func()
			#No arguments needed because the arguments have default values. 
		#Otherwise:
		else:
			#Not needed, but first, print the keyword arguments entered 
			print(kwargs)
			print('This user does not have administrative privilages.')
			print('ACCESS DENIED')
	#and return the nicely wrapped function.
	return wrapped

@validate_user
def create_user(username="admin",password="password"):
	response = {'msg':"User created successfully","User":{"username":username,"password":password}}
	print(response)

print('\n')
create_user(username='joe',password='smith')
print('\n')
create_user(username='admin',password='password')

#-Tutorial Doctor 
