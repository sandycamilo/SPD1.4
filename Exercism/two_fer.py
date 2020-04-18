# Two-fer or 2-fer is short for two for one. One for you and one for me.

# Given a name, return a string with the message:

# One for X, one for me.
# Where X is the given name.

# However, if the name is missing, return the string:

# One for you, one for me.

# PROBLEM SOLVING STRATEGY
 # Generate reasonable test inputs 
 # Understand & solve the problem - simplify if needed
 # Find a pattern in your solution
 # Make a plan - write pseudocode 
 # Follow your plan - write real code 
 # Check your work - test your code


 # return text with the message 'one for x, one for you' where x is name  
 # but if there is no name, return one for you and one for me


def two_fer(name={}):
    if name is two_fer.__defaults__[0]:
        sentence = "One for you, one for me."
        return sentence
    else:
        sentence = "One for {name}, one for me.".format(name = name)
        return sentence


print(two_fer('Sandy'))
print(two_fer())
