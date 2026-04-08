#Functions-Default arguments
def greet(name="Guest"):
    return "Hello " + name

print(greet())        # Hello Guest
print(greet("Ashu"))  # Hello Ashu

#multiple Arguments
def add(a,b):
    return a+b

#multiple Values= *args
def total(*numbers):
    return sum(numbers)
print(total(1,2,3,4))

#**kwargs(dictionary input)
def info(**data):
    print(data)
info(name="Ashu", age =20)

#Lambda functions
square = lambda x: x*x
print(square(5)) #25

#List comprehension
squares = [i*i for i in range(5)]
#with conditions
evens = [i for i in range(10) if i % 2 == 0]


# File Handling
# write file
with open("data.txt", "w") as f:
    f.write("Hello AI")

#read file
with open("data.txt","r") as f:
    print(f.read())

#Error handling
try:
    x = int(input())
except ValueError:
    print("Enter a number")

#Modules
import math
print(math.sqrt(16))
