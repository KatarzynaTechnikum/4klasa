import math
liczba_dwojkowa="11101"
#print(int(liczba_dwojkowa,2))

liczba_szesnastkowa="A0"
#print(int(liczba_szesnastkowa,16))

def naDwojkowa(a):
  t=[]
  while(a>=1):
    #dołaczam kolejny element do tablicy
    t.append(a%2)
    #biore podłoge bo nie interesuje mnie koncowka
    a= math.floor(a/2)
#zamiana tabeli przod z tyłem
  t= t[::-1]
  #zamienia z tablicy na int 
  new_list = map(str, t)
  string_value = ''.join(new_list)
  number = int(string_value)
  
  return number



print(naDwojkowa(29))
  

  