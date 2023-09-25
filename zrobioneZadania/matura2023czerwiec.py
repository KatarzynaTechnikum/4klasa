#zadanie maturalne rekurencja
def iloczyn(x,y):
  k=0
  z=0
  if y==1:
    return x
  else:
    k= y//2
    z=iloczyn(x,k)
    if y%2==0:
      return z+z
    else:
      return x+z+z

#print(iloczyn(9,11))

#zadanie maturalne
def Iloczyn(x,y):
  z = 0
  while y>=1:
    if y%2== 1:
      z +=x
    x +=x
    y = y//2
  return z

print(Iloczyn(4,5))