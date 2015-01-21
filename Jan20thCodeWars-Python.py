# PROBLEM 3 BELOW 
''' An anagram is the result of rearranging the letters of a word to produce a new word. (Ref wikipedia).

Note: anagrams are case insensitive

Examples

foefet is an anagram of toffee
Buckethead is an anagram of DeathCubeK
The challenge is to write the function isAnagram (or is_anagram in Python) to return true if the word test is an anagram of the word original and false otherwise. The function prototype is as given below:

def is_anagram(test, original):
  pass
'''

#SOLUTION TO PROBLEM 3

# write the function is_anagram
def is_anagram(test, original): #take the two list
    answer = sorted(original.lower()) == sorted(test.lower()) #if we lower case it
    #we have no issues with caps, and sorted order of both should be equal for an anagram
    return answer  #here we return the boolean value, yes it can be done in one line 
   