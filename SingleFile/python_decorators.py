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

# Decorator with arguments
def add(num):
    def add(func):
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs) + num
        return wrapper
    return add

@add(3)
def add(a,b):
    return a+b

print(add(34,1))


#Decorate a divide function with a check for a valid denominator value.
def prevent_divide_by_zero(func):
	#To pass the arguments of the function to the wrapper:
	def wrapped(*args,**kwargs):
		#If the 2nd argument(denominator) is not 0:
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

#Decorate a user function with a check for admin privillages
def admin_only(func):
	#To pass the arguments of the function to the wrapper:
	def wrapped(*args,**kwargs):
		#If the 2nd argument(denominator) is not 0:
		role = args[1]
		if role =="admin": 
			print("This user is admin")
			#Call the input-function, passing in the keyword arguments
			func(*args,**kwargs)
		#Otherwise:
		else:
			print("This user is not admin")
	#Return the wrapped function
	return wrapped

@admin_only
def User(name,role):
	print(name,role)

a_user = User('Raphael','user')
a_user2 = User('Pierre','admin')

#-Tutorial Doctor 

# DECORATING A CLASS METHOD
def time_this_1(original_function):      
    def new_function(*args,**kwargs):
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {0}".format(after-before))     
        return x                                             
    return new_function   

class ImportantStuff(object):
    @time_this_1
    def do_stuff_1(self):
        print('3')
    @time_this_1
    def do_stuff_2(self):
        print('3')
    @time_this_1
    def do_stuff_3(self):
        print('3')

t = ImportantStuff()
t.do_stuff_3()

# DECORATING AN ENTIRE CLASS
def time_this(original_function):      
    print("decorating")                   
    def new_function(*args,**kwargs):
        print("starting timer")      
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {0}".format(after-before))      
        return x                                             
    return new_function  

def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to 
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and 
            the attribute is an instance method then `time_this` is applied.
            """
            try:    
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:      
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return time_this(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls

#now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):
    def a(self):
        print("entering a")
        import time
        time.sleep(3)
        print("exiting a")

oF = Foo()
oF.a()

# PERMISSIONS

def requires_permission(sPermission):                            
    def decorator(fn):                                            
        def decorated(*args,**kwargs):                            
            lPermissions = get_permissions(current_user_id())     
            if sPermission in lPermissions:                       
                return fn(*args,**kwargs)                         
            raise Exception("permission denied")                  
        return decorated                                          
    return decorator       
    
    
def get_permissions(iUserId): #this is here so that the decorator doesn't throw NameErrors
    return ['logged_in',]

def current_user_id():        #ditto on the NameErrors
    return 1

#and now we can decorate stuff...                                     

@requires_permission('administrator')
def delete_user(iUserId):
   """
   delete the user with the given Id. This function is only accessible to users with administrator permissions
   """

@requires_permission('logged_in')
def new_game():
    """
    any logged in user can start a new game
    """
    
@requires_permission('premium_member')
def premium_checkpoint():
   """
   save the game progress, only accessable to premium members
   """

