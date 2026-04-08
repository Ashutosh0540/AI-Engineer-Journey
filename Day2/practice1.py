with open("Day2/numbers.txt","r") as f:
    data=f.read().split()# list of strings
numbers = list(map(int, data))
numbers = [int(x) for x in data]
# apply int() to every element in data
#map() gives a special objects, not a list
print("Numbers:", numbers)
print("Sum:",sum(numbers))
print("Max:",max(numbers))

evens = [i for i in numbers if i % 2 == 0]
print("Even Numbers:", evens)

"""f.read()        → "1 2 3 4 5"
.split()        → ['1','2','3','4','5']
map(int, data)  → 1,2,3,4,5
list(...)       → [1,2,3,4,5]"""

data = ['10', '20', '30']
nums = list(map(int, data))
print(nums)

data = ['10', '20', 'abc', '40']
nums = []

for x in data:
    try:
        nums.append(int(x))
    except ValueError:
        print(f"Skipping invalid value: {x}")

print(nums)
nums = [int(x) for x in data if x.isdigit()]

#finalll
data = ['10', '20', 'abc', '40']
nums = []

for x in data:
    try:
        nums.append(int(x))
    except ValueError:
        print(f"Skipping invalid value: {x}")

print("Valid Numbers:", nums)

if nums:
    print("Sum:", sum(nums))
    print("Max:", max(nums))
    
    evens = [i for i in nums if i % 2 == 0]
    print("Even Numbers:", evens)
else:
    print("No valid numbers found.")
