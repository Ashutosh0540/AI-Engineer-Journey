# 🐍 Python — My First Step Towards AI Engineer

## 🚀 Why Python?
Python is the most widely used language in AI, Machine Learning, and Data Science due to its simplicity and powerful libraries.



## 📅 Day 1 — Getting Started

### ✅ Topics Covered
- Variables and Data Types
- Lists, Tuples, Sets, Dictionaries
- Conditional Statements (if-else)
- Loops (for, while)
- Functions

---

## 💻 Practice Code

```python
# Even numbers, sum, squares

n = 5

even_numbers = []
total_sum = 0
squares = []

for i in range(1, n + 1):
    total_sum += i
    squares.append(i * i)
    
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers:", even_numbers)
print("Sum:", total_sum)
print("Squares:", squares)
