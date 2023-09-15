a =int(input())
#rekurencyjnie ciąg fibonnaciego
def fib(n):
  if n==0:
    return 0
  if n==1:
    return 1
  else:
    return fib(n-1) +fib(n-2)
    
#rekurencyjnie silnia
def silnia(a):
  if a==1:
    return 1
  else:
    return a *silnia(a-1)

print(fib(a))
print(silnia(a))