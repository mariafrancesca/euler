#!/usr/bin/python

def orfor():
  sum = 0
  for i in xrange(1,1000):
    if(i%3==0 or i%5==0):
      sum += i
  print sum

def twofor():
  sum = 0
  i = 0
  while(i<1000):
    sum += i
    i += 5
  i = 0
  while(i<1000):
    if(i%5 != 0):
      sum += i
    i += 3
  print sum

def main():
  orfor()
  twofor()

if __name__ == '__main__':
  main()
