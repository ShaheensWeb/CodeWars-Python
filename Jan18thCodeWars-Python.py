#PROBLEM #1
'''Attention Agent.
The White House is currently developing a mobile app that it can use to issue instructions to it's undercover agents.
Part of the functionality of this app is to have messages that can be read only once, and are then destroyed.
As our best undercover developer, we need you to implement a SecureList class that will deliver this functionality.
Behaviour different to the traditional list is outlined below:
Accessing an item at any index should delete the item at that index eg:
messages=SecureList([1,2,3,4])
print messages[1]  # prints 2
print messages     # prints [1,3,4]
Printing the whole list should clear the whole list eg:
messages=SecureList([1,2,3,4])
print messages     # prints [1,2,3,4]
print messages     # prints []
The viewing the representation of the list should also clear the list eg:
messages=SecureList([1,2,3,4])
print "my messages are: %r."%messages     # prints "my messages are: [1,2,3,4].
print messages     # prints []
To complete this kata you need to be able to define a class that implements getitem(), str() and repr().
Good luck Agent.'''

#SOLUTION TO PROBLEM #1
class SecureList():
  #init function below 
  def __init__(self, list): #import self due to object behaviour, then 1 new var
      self.list = list[:] #declare list in self, imported in other helper func below

  def __getitem__(self, index): #we are now fetching an item
    return (self.list).pop(index) #pop the index, it will print and remove it

  def __str__(self): #we need a representation of current secure list
    temp, self.list = self.list, [] #clone a copy of it 
    return str(temp)  #return the temp clone as representation of list at that moment

  def __repr__(self): #return representation of the list
    temp, self.list = self.list, [] #clone a copy
    return repr(temp) #repr(var) instead of str(var). <-- this confuses me slightly 

  def __len__(self): #len of a list given itself only
      return len(self.list) #return length of list from self var defined in init
