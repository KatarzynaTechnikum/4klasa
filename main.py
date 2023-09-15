#wbudowane funkcje 
#importuje bibliotekę math
import math

a = 6
b=3.444444444
tab = [3,4,5,6,7]

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
print(sorted(tab))
print(sorted("biblioteka"))

#czy liczby są anagranami
a1= "katar"
a2= "tarka"
print(sorted(a1)==sorted(a2))
#największy wspólny dzielnik - nawet dla większej liczby parametrów
print(math.gcd(4,64,8))

