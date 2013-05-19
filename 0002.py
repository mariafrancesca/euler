#!/usr/python

def main():
  fibn_2 = 1
  fibn_1 = 1
  fib    = 0
  count  = 0

  while(fib<4000000):
    fib = fibn_2 + fibn_1
    fibn_2 = fibn_1
    fibn_1 = fib
    if(fib%2 == 0):
      count += fib

  print count
  

if __name__ == '__main__':
  main()
