"""
c. 2017 Alfred S. Matthews
asm13243546@gmail.com
info@appressorium.com

Released under GNU Public License, version 3.
All rights reserved.

#

Project Euler project 1

Python, imperative

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def listnaturalsbelowten():
	pass

def multipleofthree(x):
  if (x % 3 == 0):
    return x

def multipleoffive(x):
  if x % 5 == 0:
    return x

def ismultiple(x):
  if multipleofthree(x):
      return x
  elif multipleoffive(x):
      return x

def test(x):
  if ismultiple(x):
    print(x)

def summultiples(limit, accumulator):
  #print('this ='), accumulator
  for i in range (limit):
    #print(i)
    if test(i):
      print('tested for =',i)
      accumulator.append(i)
      
      # used ?
      print("match ",i)
      print (accumulator)
    return accumulator

# need doctests
def sumaccumulator(x, accumulator):
  #print('limit x  = ',x) # should print 15 or whatever
  #print('accumulator = ',accumulator) # should print '[1,2,5,7,9]'
  sum = 0
  for i in accumulator:
    print ("i =", i)
    sum = sum + i
  print("exiting method, sum =", sum)
  return sum

if __name__ == '__main__':

  #print ("test0= ",test(15))
  #print ("test1= ",sumaccumulator(15, [1,2,5,7,9]))
  
  accumulator = [] 
  for i in range (1000):
    if ismultiple(i):
      accumulator.append(i)

  print ("test2= ",sumaccumulator(1000, accumulator))

  #print(summultiples(1000, []))
  #print(sumaccumulator(summultiples(1000, accumulator = [])))
