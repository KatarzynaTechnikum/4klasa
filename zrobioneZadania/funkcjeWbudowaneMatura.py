#wbudowane funkcje 
#importuje bibliotekę math
#from math import factorial #inny sposób importu samej biblioteki
import math

a = 6
b=3.444444444
tab_liczbowy = [3,4,5,6,7]

#funkcja pierwiastek
print(math.sqrt(a))
#power (liczba, wykładnik)
print(math.pow(a,a))
#absolute valu
print(math.fabs(a))

#podłoga - zaokrąglenie do dołu
print(math.floor(b))
#sufit - zaokrąglenie w dół
print(math.ceil(b))
#jak dodam ,end=" " - to bedzie pisać w nowej lini


#wbudowana funkcja silnia
print(math.factorial(a))
#sortuje wszystko co można by posortować
print(sorted(tab_liczbowy))
print(sorted("ciąg fibbonaciego"))

#czy liczby są anagranami
a1= "heart"
a2= "earth"
print(sorted(a1)==sorted(a2))
#największy wspólny dzielnik - nawet dla większej liczby parametrów
print(math.gcd(4,64,8))

#zbiór utworzony z napisu
print(set('rekurencja'))

list1=[1,1,1,2,3,3,3,4]
print(set(list1))

#praca z ciągami
list_from_str = "sequence"
l1 =list(list_from_str)
print(l1)
#suma licz z ciągu
print(sum(tab_liczbowy)) #biblioteka wbudowana
print(math.fsum(tab_liczbowy))
#min max - jak w bazach danych select max() from 
print(min(tab_liczbowy)) #biblioteka wbudowana
print(max(tab_liczbowy)) 
print(min(l1))#najmniejszy kod ascii
print(max(l1))#największy kod ascii

print(chr(74))#podaj liczbę dziesiętną

#konwersja
liczba = -12.45
liczba2 = -12.75
print(int(liczba)+1)
print(int(liczba2)+1)
print(int(liczba))
#konwertowanie do innego systemu liczbowego, (liczba, system liczbowy)
liczba_dwojkowa="11101"
print(int(liczba_dwojkowa,2))

liczba_szesnastkowa="A0"
print(int(liczba_szesnastkowa,16))

#funkcje str()
x = 23232.2323
print(str(x)*3)
print(str(x)+"aba")

# w konsoli dostępne dir(zmianna)
#help potem wybieramy funkcje