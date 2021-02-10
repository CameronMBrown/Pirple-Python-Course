#Pirple Python Assignment 3 - if statements

#returns True if at least 2 values match
#"1" and 1 considered the same
def ifTwoTrue(a, b, c):
  if checkMatch(a, b) or checkMatch(b, c) or checkMatch(a, c):
    return True
  else:
    return False

#compares two values and returns true if they match
def checkMatch(a, b):
  a = intIfPossible(a)
  b = intIfPossible(b)
  if a == b:
    return True
  else:
    return False

#converts arg to int type if possible
def intIfPossible(a):
  if isinstance(a, str):
    if a.isdigit():
      return int(a)
  return a

print(ifTwoTrue("1", 1, 2))           #true
print(ifTwoTrue("cat", "dog", 10))    #false