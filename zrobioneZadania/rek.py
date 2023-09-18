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

#program obliczajacy sume cyfr
def suma_cyfr(x):
  if x<10 :
    return x
  else:
    return int(suma_cyfr(x/10)) + x %10

#program obliczający potege rekurencyjnie
def potega(a,n):
  if n==0:
    return 1
  else:
    return a * potega(a,n-1)

#potęga o połowę
def potegaPN(a,n):
  if n==0:
    return 1
  else:
    if n%2==0:
      w= potegaPN(a,n/2)
      return w*w
    else:
      return a*(potegaPN(a,n-1))
#potega o połowe inna wersja     
def potegaPN_1(a,n):
  if n==0:
    return 1
  else:
    if n%2==0:
      w= potegaPN(a,n/2)
      return w*w
    else:
      w= potegaPN(a,int(n/2))
      return a*w*w



#print(potegaPN(2,7))
print(potegaPN_1(2,7))

print(suma_cyfr(669))
print(potega(2,8))

print(fib(a))
print(silnia(a))