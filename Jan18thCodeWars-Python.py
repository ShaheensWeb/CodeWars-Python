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
