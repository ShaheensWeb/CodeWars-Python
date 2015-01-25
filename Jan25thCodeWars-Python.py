#Problem set number 8, Python-CodeWars
'''Write a function that finds the sum of all its arguments.

eg:

sum(1, 2, 3) # => 6
sum(8, 2) # => 10
sum(1, 2, 3, 4, 5) # => 15
Note that Python's function name is sum_args, as to avoid confusion with the preexistsing sum function. 
Ruby's Array#sum has been removed to make it a bit more interesting! '''


#Solution to problem set 8

def sum_args(*args): #we are unaware of the amount of args, so we have *args telling func unknown amount of inputs n
    return sum(args) #here we sum all inputs given in args, using sum(fn) and return the val as an int. 

