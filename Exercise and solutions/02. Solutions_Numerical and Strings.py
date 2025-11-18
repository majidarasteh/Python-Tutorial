#Numerical Data Types (1–25)
# 1
x = 10
print(type(x))  # <class 'int'>

# 2
y = 3.14
print(type(y))  # <class 'float'>

# 3
z = 2 + 3j
print(z.real)   # 2.0
print(z.imag)   # 3.0

# 4
a = 6e8
print(a)        # 600000000.0

# 5
b = 6e-8
print(b)        # 0.00000006

# 6
print(0.1 + 0.2 == 0.3)  # False

# 7
from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.07')
total = price + price * tax
print(total)    # 21.3893

# 8
from fractions import Fraction
a = Fraction(3, 4)
b = Fraction(5, 6)
print(a + b)    # 19/12
print(a - b)    # -1/12
print(a * b)    # 5/8
print(a / b)    # 9/10

# 9
print(float(Fraction(3, 4)))  # 0.75

# 10
print(isinstance(5, int))    # True
print(isinstance(5.0, float))# True

# 11
import math
radius = 5.5
area = math.pi * radius ** 2
print(area)

# 12
print(10 + 3.5 * 2)  # 17.0

# 13
print(int('1010', 2))  # 10

# 14
print(int('12', 8))    # 10

# 15
print(int('A', 16))    # 10

# 16
x_bin = 0b1010
x_oct = 0o12
x_hex = 0xA
print(x_bin, x_oct, x_hex)  # 10 10 10

# 17
c1 = 2+3j
c2 = 1-2j
print(c1 + c2)  # (3+1j)
print(c1 * c2)  # (8-1j)

# 18
c = Fraction(0.75)
print(c)        # 3/4

# 19
d = Fraction("0.6")
print(d)        # 3/5

# 20
print((5.0).is_integer())  # True

# 21
print(round(3.14159265359, 2))  # 3.14

# 22
print(round(3.14159265359, 4))  # 3.1416

# 23
print(abs(-3.14))  # 3.14
print(abs(2+3j))   # 3.605551275463989

# 24
print(2 ** 3)          # 8
print(math.sqrt(16))   # 4.0

# 25
print(10 // 3)  # 3
print(10 % 3)   # 1


# Strings and Basics (26–50)
# 26
s1 = 'Hello'
s2 = "World"
print(s1, s2)

# 27
multi = """Hello
Python
World"""
print(multi)

# 28
print("He said \"Hello\"")

# 29
print("It's raining")

# 30
print("Hello\nWorld")

# 31
print(r"C:\Users\Name\Desktop")

# 32
s = "Python"
print(s[0], s[-1])  # P n

# 33
print(s[-4])  # t

# 34
print(s[0:2])  # Py

# 35
print(s[2:5])  # tho

# 36
print(s[3:])   # hon

# 37
print(s[::-1]) # nohtyP

# 38
print(s[::2])  # Pto

# 39
print("Hello" + " " + "World")  # Hello World

# 40
print("Hi " * 3)  # Hi Hi Hi 

# 41
print("Py" in s)  # True

# 42
print("Java" not in s)  # True

# 43
s = "Python"
s = "A" + s[1:]
print(s)  # Aython

# 44
Str = "Hello"
del Str
# print(Str) would give error

# 45
print(str(123))  # "123"

# 46
print(str(3.14)) # "3.14"

# 47
print(str(True)) # "True"

# 48
def add(a, b):
    """Returns the sum of a and b"""
    return a + b

# 49
print(ord('A'))  # 65
print(ord('a'))  # 97

# 50
print(chr(65))   # 'A'
print(chr(97))   # 'a'


# String Methods and Manipulation (51–75)
# 51
print("python".upper())  # PYTHON

# 52
print("PyThOn".lower())  # python

# 53
s = "banana"
print(s.count("a"))      # 3

# 54
print("hello".find("l")) # 2

# 55
print("hello world".replace("world", "Python"))  # hello Python

# 56
print("one two three".split())  # ['one', 'two', 'three']

# 57
print("-".join(["a", "b", "c"]))  # a-b-c

# 58
print("abc123".isalnum())  # True

# 59
print("12345".isdigit())   # True

# 60
print("age1".isidentifier())  # True
print("1age".isidentifier())  # False

# 61
print("Hello World".istitle())  # True

# 62
print("python".capitalize())  # Python

# 63
print("PyThOn".swapcase())   # pYtHoN

# 64
print("  hello  ".strip())  # hello

# 65
txt = "I could eat bananas all day"
print(txt.partition("bananas"))  # ('I could eat ', 'bananas', ' all day')

# 66
print("hello".startswith("he"))  # True

# 67
print("hello".endswith("lo"))    # True

# 68
print("   ".isspace())           # True

# 69
print("Hello\nWorld!".isprintable())  # False

# 70
print("½".isnumeric())           # True

# 71
name = "Ali"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 72
print("Hello\nWorld")

# 73
print("Name:\tMajid")

# 74
print("He said \"Python is easy!\"")

# 75
print("This is a backslash: \\")


# Advanced String Operations (76–100)
# 76
print(r"C:\Users\Majid\Desktop")

# 77
total = 10 + 20 + 30 + \
        40 + 50
print(total)  # 150

# 78
s = "Python"
print(s[::2])  # Pto

# 79
print(s[::-1]) # nohtyP

# 80
for i, c in enumerate(s):
    print(i, c)

# 81
s = "Hello World"
print("World" in s)  # True

# 82
print("Data" + "Science")  # DataScience

# 83
print("Ha" * 5)  # HaHaHaHaHa

# 84
s = "Python Programming"
print(s[7:])  # Programming

# 85
print(s[:6])   # Python

# 86
print(s[4:10]) # on Pro

# 87
print(s.replace("Python", "Java"))  # Java Programming

# 88
num = 42
print(str(num) + " is the answer")  # 42 is the answer

# 89
s = "Hello World"
print(s.count("o"))  # 2

# 90
s = "apple,banana,orange"
print(s.split(","))  # ['apple','banana','orange']

# 91
lst = ["apple","banana","orange"]
print(", ".join(lst))  # apple, banana, orange

# 92
print("   Hello World   ".strip())  # Hello World

# 93
print("PyThOn".swapcase())          # pYtHoN

# 94
print("Hello123".isalnum())         # True

# 95
print("123".isdigit())              # True

# 96
name = "Ali"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 97
print("Hello\nWorld")

# 98
print("Name:\tMajid")

# 99
print(r"C:\Users\Majid")

# 100
def square(n):
    """
    Returns the square of n
    """
    return n ** 2
