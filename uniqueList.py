"""
Pirple Python Assignment 4 - lists

my instict would be to write a loop that checks for matches at each index then appends to the
correct array. However, at this point in the course loops have not been introduced.
Nicely, the "in" operator results in a much more consice function, however relying apon it for
most of the logic in this function.
"""
myUniqueList = [] #all values will be unique
myLeftovers = [] #composed of all values that were not allowed in unique list

def uniqueAdd(value):
  if isinstance(value, bool): #for "in" operator to work properly with booleans, they need to be converted to strings
    value = str(value)
  if value in myUniqueList: #is value contained in list?
    myLeftovers.append(value) #if yes, add to leftovers
    return False
  else :
    myUniqueList.append(value) #if not, is a new unique value
    return True

uniqueAdd(1)
uniqueAdd("dog")
uniqueAdd("Cameron")
uniqueAdd(True)
uniqueAdd(1)
uniqueAdd("Pirple")
uniqueAdd("dog")

print(isinstance(True, bool))
print(myUniqueList) #[1, 'dog', 'Cameron', True, 'Pirple']
print(myLeftovers)  #[1, 'dog']