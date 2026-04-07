#List(mutable)
arr = [1, 2, 3]
arr.append(4)
print(arr)

#tuple(immutable)
t = (1, 2, 3)

#set(unique values)
s = {1, 2, 3}

#dictionary()
student = {
    "name": "Ashutosh",
    "age": 20
}
print(student)

#functions
def greet(name):
    return "Hello " + name

print(greet("Ashu"))


#practice:
n=int(input("Enter a number:"))
def oddn(n):
    for i in range(1, n+1):
        if i % 2 != 0:
           print(i, end=" ")
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= 1
    return fact

oddn(n)
print("\nFactorial:",factorial(n))

def evenn(n):
    print("Even Numbers:")
    for i in range(1,n+1):
        if i % 2==0:
            print(i,end=" ")

def sumofnum(n):
    ttl = 0
    for i in range(1,n+1):
        ttl +=i
    print(sum)


n = int(input("Enter a number: "))

evens = [i for i in range(1, n+1) if i % 2 == 0]
total = sum(range(1, n+1))

print("Even Numbers:", evens)
print("Sum:", total)

#combined code
n = int(input("Enter a number: "))

def oddn(n):
    print("Odd Numbers:", end=" ")
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def evenn(n):
    print("Even Numbers:", end=" ")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def sumofnum(n):
    ttl = 0
    for i in range(1, n+1):
        ttl += i
    return ttl

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Calling all functions
oddn(n)
evenn(n)
print("Sum:", sumofnum(n))
print("Factorial:", factorial(n))

#append = add as one | extend = break and add
arr.append([4,5])   #→ [1,2,3,[4,5]]
arr.extend([4,5])   #→ [1,2,3,4,5]