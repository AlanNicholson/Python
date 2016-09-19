#https://adriann.github.io/programming_problems.html
#Elementary
#Number 1
print("Hello World!")
#Number 2 + 3
name=input("What's your name?")
if name in ("Alice","Bob"):
    print("Hello",name)
else:
    print("Hello Sir")
#Number 4 + 5
n=input("Enter a Number: ") #n=17
a1=range(0,int(n)+1,3)
a2=range(0,int(n)+1,5)
print(sum(a1)+sum(a2))
#Number 6
import math
n=int(input("Enter a Number: "))
nR=range(0,int(n)+1,1)
mC=input("sum or prod?: ")
if mC in ("Sum","sum","s","S"):
    print(sum(nR))
elif mC in ("Prod","prod","p","P"):
    print(math.factorial(int(n)))
else:
    print("none")
#Number 7 Multiplication Tables
num1=int(input("Enter a number: "))
for i in range(1,13):
    print(num1,"x",i,"=",num1*i)
#Number 8 All Primes
num2=int(input("Primes up to: "))
allP=[x for x in range(2,num2+1)
      if all(x % y != 0 for y in range(2,x) )]
print("The Primes are: ",allP)
#Number 9 Secret Number, > < , count trys, same try counts as one.
import random
secret=random.randrange(0,1000)
guess=int()
tryList=[]
while guess != secret:
    guess=int(input("Guess a number between 0 and 1000. "))
    if guess > secret:
        if guess not in tryList:
            tryList.append(guess)
        print("Lower")
    elif guess < secret:
        if guess not in tryList:
            tryList.append(guess)
        print("Higher")
    elif guess==secret:
        tryList.append(guess)
print("Success!! It took ",len(tryList),"attempts.")
#Number 10 Next 20 Leap Years
from datetime import date
now=(date.today().year)
leapList=[i for i in range(now,now+80) if i >= now and i % 4 ==0]
print(leapList)
#Number 11 compute  PI  4⋅∑k=1106(−1)k+12k−1=4⋅(1−1/3+1/5−1/7+1/9−1/11…).
from decimal import *
import time
total=0

start_time = time.time()

def sumOf(i):
    x=(4*((-1)**(i+1))/((2*i)-1))
    return x

for i in range(1,10**6):
    total+=sumOf(i)
    
print(Decimal(total))
print("Pi approximated in",(time.time() - start_time),"seconds.")

