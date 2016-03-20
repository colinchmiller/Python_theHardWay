#first print, %d is the 10 following the text, also assigning a variable to be used later
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#order only seems to matter with the % assignment
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

#print the concatenation of two variables
print (w + e)
