__author__ = 'admin'

# Decoration to add to a function
class theDecorator(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering: ", self.f.__name__, " <- Decoration")
        self.f()
        print("Exited: ", self.f.__name__, " <- Decoration\n")

# Function will be decorated with @entry_exit
@theDecorator
def firstFunction():
    print("Inside: firstFunction() <- Provided by original function")

# Function will be decorated by @entry_exit
@theDecorator
def secondFunction():
    print("Inside: secondFunction() <- Provided by original function")

# Function will be decorated by @entry_exit
def thirdFunction():
    print("Inside: thirdFunction() <- Provided by original function")

print("firstFunction call:")
firstFunction()
print("secondFunction call:")
secondFunction()
print("thirdFunction call:")
thirdFunction()