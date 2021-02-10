#Pirple Assignment 4 - loops

# classic fizzbuzz problem with the addition of finding prime numbers
# isPrime is not maximally optimized

def isPrime(num):
  if num > 1:
    for i in range(2, num): 
      if num % i == 0 : # mod = 0 implies this is not a prime
        return False
    return True #if we have exited the loop, we found no devisor with mod = 0, so this is prime
  else:
    return False

def FizzBuzz(max):
  for i in range(1, max + 1): # do not exclude passed "max" number
    if isPrime(i):
      print("PRIME    ", i)
    elif i % 15 == 0 : # %3 and %5 can be simplified to %15
      print("FizzBuzz ", i)
    elif i % 5 == 0 :
      print("Buzz     ", i)
    elif i % 3 == 0 :
      print("Fizz     ", i)
    else:
      print(i)

FizzBuzz(100)