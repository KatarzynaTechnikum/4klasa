#https://www.geeksforgeeks.org/python-measure-time-taken-by-program-to-execute/

# Code to Measure time taken by program to execute.
import time

def silnia(n):
  if n==1: 
    return 1
  else:
    return n*(silnia(n-1))

def silniaFor(n):
  silnia =1
  for i in range(1,n+1):
    silnia *=i
  return silnia
  
a =800

# store starting time
begin = time.time()
silnia(a)
time.sleep(1)
# store end time
end = time.time()
# total time taken
totalTime = end - begin
print(f"Total runtime of the program rek  is {totalTime}")

# store starting time
begin1 = time.time()
silniaFor(a)
time.sleep(1)
# store end time
end1 = time.time()
# total time taken
totalTime1 = end1 - begin1
print(f"Total runtime of the program For is {totalTime1}")
if totalTime1> totalTime:
  print("Petla For działa dłużej")
else: #tu nie podaję wartunku
  print("Rekurencja działa dłużej")

