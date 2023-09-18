def potegaPN(a,n):
  if n==0:
    return 1
  else:
    if n%2==0:
      w= potegaPN(a,n/2)
      return w*w
    else:
      return a*(potegaPN(a,n-1))
      
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
