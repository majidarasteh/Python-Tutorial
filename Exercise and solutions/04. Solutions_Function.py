# 1 & 2. Function definition and advantages
# Functions organize code, prevent repetition, and improve readability.

# 4. Simple greeting function
def greet():
    print("Hello, Python!")

greet()  # Output: Hello, Python!

# 5. Docstring example
def greet_doc():
    """Prints a welcome message."""
    print("Hello, Python!")

# 6. Add two numbers
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

# 7 & 8. Positional vs Keyword arguments
def student_info(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)

student_info("Ali", 15, "A")            # Positional
student_info(age=15, name="Ali", grade="A")  # Keyword

# 9. Default parameter
def greet_user(name="User"):
    print("Hello,", name)

greet_user()      # Hello, User
greet_user("Majid")  # Hello, Majid

# 10. Function returning multiple values
def calculate(a, b):
    return a + b, a * b

sum_result, mul_result = calculate(3, 4)
print(sum_result, mul_result)  # Output: 7 12

# 11 & 12. Local vs Global variable
x = 10  # global

def modify_global():
    global x
    x = 5
    print("Inside function:", x)

modify_global()           # Inside function: 5
print("Outside function:", x)  # Outside function: 5

# 13. Scope and lifetime
def local_var():
    y = 20  # local
    print("Inside:", y)

local_var()
# print(y)  # ❌ Error: y not defined

# 14. Function calling another function
def welcome():
    greet()

welcome()  # Output: Hello, Python!

# 15. Function with no return statement
def hello():
    print("Hello")

result = hello()  # Prints Hello
print(result)    # Output: None


# 17. Lambda to square a number
square = lambda x: x * x
print(square(5))  # 25

# 18. Lambda functions can have only one expression

# 19. Lambda to add two numbers
add_nums = lambda a, b: a + b
print(add_nums(4, 3))  # 7

# 20. Lambda = anonymous, no name needed

# 21. Lambda with map()
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)  # [2, 4, 6, 8]

# 22. Lambda with filter()
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)  # [2, 4]

# 23. Lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x*y, [1,2,3,4])
print(product)  # 24

# 24. Combine map and filter
numbers = [1,2,3,4,5,6]
result = list(map(lambda x: x*2, filter(lambda x: x%2==0, numbers)))
print(result)  # [4, 8, 12]

# 29. map() example
numbers = [1,2,3,4]
squares = list(map(lambda x: x*x, numbers))
print(squares)  # [1,4,9,16]

# 30. filter() example
numbers = [1,2,3,4,5,6]
greater_than_5 = list(filter(lambda x: x>5, numbers))
print(greater_than_5)  # [6]

# 31. reduce() example
from functools import reduce
sum_all = reduce(lambda x,y: x+y, numbers)
print(sum_all)  # 21

# 33. Reduce to find maximum
max_value = reduce(lambda x,y: x if x>y else y, [12,7,25,3,18])
print(max_value)  # 25

# 34. Filter names longer than 3
names = ["Ali","Sara","Reza","Tom"]
long_names = list(filter(lambda n: len(n)>3, names))
print(long_names)  # ['Sara','Reza']

# 35. Combine map+filter+reduce
numbers = [1,2,3,4,5,6]
total = reduce(lambda a,b: a+b, map(lambda x:x*x, filter(lambda x:x%2==0, numbers)))
print(total)  # 56 (2²+4²+6²)

# 38. Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120

# 39. Sum 1 to n
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

print(recursive_sum(5))  # 15

# 40. Fibonacci nth
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))  # 8

# 42. Recursive function without base case → RecursionError
# def wrong_recursion(n):
#     return n + wrong_recursion(n-1)  # ❌ will cause error

