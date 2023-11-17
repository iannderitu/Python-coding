#identation
if 5 > 2:
  print("five is greater than two")
 #variables
  userage = 100
  username = "Ian"
  print(userage)
  print(username)
#typesofvariables
  myVariableName = "Camel Case Ian"
  MyVariableName = "Pascal Case Ian"
  my_variable_name = "Snake Case Ian"
  print(myVariableName)
  print(MyVariableName)
  print(my_variable_name)
#printfuction
  x = "My Name is ian, First of his Name, Ruler of united states, Leader of the universe"
  print(x)
  a = "ian Snow"
  b = "is"
  c = "cool"
  print(a, b, c)
#datatype
digit = 5
print(digit)
print(type(digit))

digit2 = 1.5
print(digit2)
print(type(digit2))

#randomlibrary
import random
print(random.randrange(1,100))
#casting
y=int(1)
z=int(1.5)
t=int(1)
print(type(y))
print(type(z))
print(type(t))

b = float(1)
c = float(2.0)
d= float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#strings
string1 = ("I am the strongest, the brightest, the most awesome hero"
           ""
           " in the world")
print(string1)
print(type(string1))
#concatenation
string2 = " He is also a super hero - Spider Man"
string3 = string1+string2
print(string3)

#python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("Digit 5 is more than Digit 4")
else:
    print("Digit 4 is less than Digit 5")
#artimatic operators
#sun
h=28
i=30
j=h+i
print(j)
#subtration
k=1
print(k)
#multiplication
j=h*i
print(j)
#divition
m=h/i
print(m)
 #modulus
n=1
#list
thislist =["Apple","Bannana","Cherry","Mango","Pears","Avocado"]
print(thislist)
#Asseslists
print(thislist[0])
#NegativeIndexing
print(thislist[-1])
#RangeofIndexes
print(thislist[1:4])

#whileloop
o = 1
while o < 6:
    print(o)
    o+=1

#breakstatement
p = 1
while p < 6:
    print(p)
    if p==3:
        break
    p+=1

#else statment
q = 1
while q < 6:
    print(q)
    q+=1
else:
    print("q is more than 1")

#forloops
cars = ["Mercedes Benz","ferrari","lamborgini","Pagani","tesla","buggati"]
for x in cars:
    print(x)

#function
def myfunction():
    print("This is a funtion")
myfunction()

#INPUT
name = input ("what is your name:")
print("Your name is:" +name )

















