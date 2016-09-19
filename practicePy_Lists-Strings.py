#https://adriann.github.io/programming_problems.html
#Lists, Strings

#1 Function that returns the largest element in a list.
import random
hL=random.sample(range(0,200),30)
firstNum=hL[0]
for i in hL:
    if firstNum < i:
       firstNum=i
print(hL,"The Highest Number is:",firstNum)
#2 Function that reverses a list, preferably in place.
import random
rL=random.sample(range(0,200),30)
print(rL,"Backwards is:",rL[::-1]) # Slice [start:stop:step]
#3 Function that checks whether an element occurs in a list.
my_list=["23", "fgds", "5t", "vuds", "900", "de39f"]
guess=input("enter a guess:")
while guess not in my_list:
    guess=input("try again:")
print("correct")       
#4 Function that returns the elements on odd positions in a list.
import random
rL=random.sample(range(0,200),20)
rLodd=rL[::2]
print(rL,"Numbers in odd positions:",rLodd)
#5 Function that computes the running total of a list.
import random
pL=random.sample(range(0,200),20)
posL=int(input("Enter a position on the list:"))
print(sum(pL[0:posL:1]),pL) #total=0, total+=1
#6 Function that tests whether a string is a palindrome.
wordP=str(input("Is my word a Palindrome?:"))
if wordP==wordP[::-1]:
    print("Yes")
else:
    print("No")
#7 Three functions that compute the sum of the numbers in a list:
# using a for-loop, a while-loop and recursion.
import random
sL=random.sample(range(0,200),20)
total=0
for i in sL:
    total+=i
print(sL)
print("Summed up with FOR is: ",total)
total=0
x=0
a=0
while x < len(sL):
    x+=1
    total+=sL[a]
    a+=1 
print("Summed up with WHILE is: ",total)
total=0
z=len(sL)
b=0
while z != -1:
    if z == 0:
        print("Summed up with RECURSION is: ",total)
        break
    else:
        total+=sL[b]
        z-=1
        b+=1
#8 Function that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.
import math
r=int(input("Perfect Squares up to: "))
w=int(input("List size: "))
bL=range(1,r)
squares=[]
for a in bL:
    if len(squares) == w:
        break
    elif (math.sqrt(a)).is_integer():
        squares.append(a)    
print(squares)
#9 Function that concatenates two lists.
#10 Function that combines two lists by alternatingly
# taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
