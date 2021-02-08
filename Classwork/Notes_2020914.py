#This is an example of a list
numList = [3, 6, 8, 4]
print (numList)

#Indexing
#Python Indexing starts at 0
#represents position 3 in the list. In this example it represents integer 8
numList[2]
print (numList[2])

#Its possible to index using negative numbers too.
#Works the same exact way, but backwards
#So working from the right to left, pos -3 is the integer 6
numList[-3]
print (numList[-3])

#lists can also be strings, which also work with indexing
sL = ['h', 'e', 'l', 'l', 'o']
#Both of the following print 'o'
print (sL[4])
print (sL[-1])

#Lists can be mixed too! Lists can be nested within each other as well.
bag = [2, 'bruh', 7, 'D20 Dice', [2, 3]]

#Technically, strings are lists as well. Meaning they can be indexed
String = "gaming belligerently"
print (String[3])

#Lists, however, can be changed, unlike strings.
bag[2] = 'new object'
print (bag[2])

#One final general note on lists, they can be, in fact, concatinated

#Slicing
#For the following, starting index is included, but last is not
#The following will drop at 'D20 Dice'
#You can slice with negative indexing as well
print (bag[0:3])

#Omitting an index when slicing uses the following defaults
## 0 for the left extrema (starts at the beginning)
## len(...) for the right extrema

#So far, we've been slicing with 2 arguments. There is actually 3, though its optional.
##Third argument is called the 'stride'
##Tells program when to skip characters
print (bag[0:4:2])
