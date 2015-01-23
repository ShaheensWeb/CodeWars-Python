#Problem Set 5

'''
Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.) '''

#Solution to problem set 5

def alphabet_position(text): #function name: alphabet_position, function parameter: text
    output = '' #the return var
    for ch in text.lower(): #for each character labelled ch in the lower case version of text
        if ch.isalpha(): #if it meets the criteria of an alphabetical letter
            output = output + str(ord(ch) - 96) + ' ' #find its value, taken from stackoverlfow
    output = output.strip() #strip the bare space
    return output #return the output value

