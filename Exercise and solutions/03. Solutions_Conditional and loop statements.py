# 1. Check if a number is positive
num = 5
if num > 0:
    print("Positive")

# 2. Check if a number is negative or zero
num = -3
if num < 0:
    print("Negative")
else:
    print("Zero")

# 3. Check if a number is even or odd
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Check if a student passed (marks ≥ 50)
marks = 65
if marks >= 50:
    print("Passed")
else:
    print("Failed")

# 5. Adult or Minor
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 6. Eligible to vote
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 7. Largest of two numbers
a, b = 5, 10
if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")

# 8. Largest of three numbers
a, b, c = 5, 10, 7
if a > b and a > c:
    print(a, "is largest")
elif b > c:
    print(b, "is largest")
else:
    print(c, "is largest")

# 9. Check divisible by 5
num = 20
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 10. Divisible by 3 and 5
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# 11. Divisible by 3 or 5
num = 7
if num % 3 == 0 or num % 5 == 0:
    print("Divisible by 3 or 5")
else:
    print("Not divisible by 3 or 5")

# 12. Triangle type by sides
a, b, c = 5, 5, 5
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# 13. Triangle type by angles
a, b, c = 60, 60, 60
if a == 90 or b == 90 or c == 90:
    print("Right")
elif a < 90 and b < 90 and c < 90:
    print("Acute")
else:
    print("Obtuse")

# 14. Leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

# 15. Vowel or consonant
ch = 'a'
if ch.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 16. Uppercase or lowercase
ch = 'A'
if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

# 17. Multiple of 7
num = 14
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not multiple of 7")

# 18. Prime number (simplified for small numbers)
num = 7
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

# 19. Grade based on marks
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# 20. Eligible for loan
age, salary = 25, 40000
if age >= 21 and salary >= 30000:
    print("Eligible")
else:
    print("Not eligible")

# 21. Wear coat
temperature = 5
if temperature < 10:
    print("Wear a coat")
else:
    print("No need for coat")

# 22. Number in range 1–100
num = 50
if 1 <= num <= 100:
    print("In range")
else:
    print("Out of range")

# 23. Number outside 1–10
num = 12
if num < 1 or num > 10:
    print("Outside range")
else:
    print("Within range")

# 24. Smallest of three numbers
a, b, c = 5, 10, 3
if a < b and a < c:
    print(a, "is smallest")
elif b < c:
    print(b, "is smallest")
else:
    print(c, "is smallest")

# 25. Scholarship (marks ≥ 90)
marks = 92
if marks >= 90:
    print("Scholarship awarded")
else:
    print("No scholarship")

# 26. Roller coaster ride
height = 130
if height >= 120:
    print("Can ride")
else:
    print("Cannot ride")

# 27. Triangle can be formed
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Cannot form triangle")

# 28. Single, double, or triple digit
num = 75
if 0 <= num <= 9:
    print("Single-digit")
elif 10 <= num <= 99:
    print("Double-digit")
else:
    print("Triple-digit")

# 29. Season based on month
month = 7
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Autumn")

# 30. Weekend or weekday
day = 6
if day in [6,7]:
    print("Weekend")
else:
    print("Weekday")

# 31. Age category
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# 32. Input yes or no (case-insensitive)
answer = "Yes"
if answer.lower() == "yes":
    print("You said yes")
else:
    print("You said no")

# 33. Divisible by 2, 3, or 5
num = 15
if num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 2,3,5")

# 34. Numbers in ascending order
a, b, c = 5, 10, 15
if a < b < c:
    print("Ascending order")
else:
    print("Not ascending")

# 35. Positive, negative, or zero
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 36. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 37. Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

# 38. Print all even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

# 39. Print all odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

# 40. Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i**2)

# 41. Print cubes of numbers from 1 to 10
for i in range(1, 11):
    print(i**3)

# 42. Multiplication table of a given number
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 43. Sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)

# 44. Print all elements of a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 45. Print all elements of a tuple
numbers = (1, 2, 3)
for n in numbers:
    print(n)

# 46. Print each character of a string
word = "Python"
for ch in word:
    print(ch)

# 47. Count vowels in a string
text = "Python Programming"
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels count:", count)

# 48. Print numbers divisible by 3 in a list
numbers = [1, 3, 5, 6, 9]
for n in numbers:
    if n % 3 == 0:
        print(n)

# 49. Factorial of a number using for loop
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)

# 50. Fibonacci sequence up to n terms
n = 7
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

# 51. Iterate over a dictionary
student = {"name":"Alice", "age":20, "grade":"B"}
for key, value in student.items():
    print(key, ":", value)

# 52. Print indices and values of a list using range()
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# 53. Print a list in reverse order
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])

# 54. Print all positive numbers in a list
numbers = [-2, 3, -5, 6, 0]
for n in numbers:
    if n > 0:
        print(n)

# 55. Pattern using nested for loops (triangle of stars)
rows = 5
for i in range(1, rows+1):
    print("*" * i)


# 56. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 57. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 58. Sum numbers from 1 to 100
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum:", total)

# 59. Factorial of a number
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# 60. Fibonacci series using while loop
n = 7
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1

# 61. Print numbers divisible by 5 up to 50
i = 1
while i <= 50:
    if i % 5 == 0:
        print(i)
    i += 1

# 62. Print numbers until a number > 20 is reached in a list
numbers = [5, 12, 18, 25, 8]
i = 0
while i < len(numbers):
    if numbers[i] > 20:
        break
    print(numbers[i])
    i += 1

# 63. Count digits in a number
num = 12345
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print("Number of digits:", count)

# 64. Reverse a number
num = 1234
rev = 0
temp = num
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print("Reversed:", rev)

# 65. Sum of digits of a number
num = 123
total = 0
temp = num
while temp > 0:
    total += temp % 10
    temp //= 10
print("Sum of digits:", total)

# 66. Check if a number is a palindrome
num = 121
temp = num
rev = 0
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not palindrome")

# 67. Input numbers until user enters 0, then sum all
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Sum:", total)

# 68. Find the largest number in a list
numbers = [4, 7, 1, 9, 3]
max_num = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1
print("Largest number:", max_num)

# 69. Print all prime numbers less than 50
num = 2
while num < 50:
    is_prime = True
    i = 2
    while i <= num//2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
    num += 1

# 70. Generate a countdown timer
seconds = 5
while seconds > 0:
    print(seconds)
    seconds -= 1
print("Time's up!")


# 71. Print numbers 1–10 but stop at 6 using break
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 72. Print numbers 1–10 skipping 5 using continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 73. Search for a number in a list, print "Found" and break
numbers = [2, 4, 6, 8]
target = 6
for n in numbers:
    if n == target:
        print("Found")
        break

# 74. Print all numbers in a list except negative numbers
numbers = [3, -2, 5, -7, 8]
for n in numbers:
    if n < 0:
        continue
    print(n)

# 75. Print even numbers in a list using continue
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 != 0:
        continue
    print(n)

# 76. Exit a while loop when user enters a negative number
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    print("You entered:", num)

# 77. Skip processing numbers divisible by 3 in a loop
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# 78. Stop asking input when user types "exit"
while True:
    text = input("Enter text (type 'exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You entered:", text)

# 79. Skip vowels while printing characters of a string
word = "Python"
for ch in word:
    if ch.lower() in "aeiou":
        continue
    print(ch)

# 80. Break out of nested loops when a condition is met
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            break
        print(i, j)


# 81. Search for a number in a list and use else to print "Not found"
numbers = [1, 3, 5, 7]
target = 4
for n in numbers:
    if n == target:
        print("Found")
        break
else:
    print("Not found")

# 82. Loop through a string and use else to print "No vowels" if none found
text = "rhythm"
for ch in text:
    if ch.lower() in "aeiou":
        print("Vowel found:", ch)
        break
else:
    print("No vowels")

# 83. Check if a number is prime using for-else
num = 13
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

# 84. Loop through a list to find the first even number, else print "No even numbers"
numbers = [1, 3, 5, 7]
for n in numbers:
    if n % 2 == 0:
        print("First even:", n)
        break
else:
    print("No even numbers")

# 85. Input numbers until 0, else print "All positive numbers"
total = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    if num < 0:
        print("Negative number entered")
        break
    total += num
else:
    print("All positive numbers entered")

# 86. Use for-else to detect repeated elements in a list
numbers = [1, 2, 3, 4]
seen = []
for n in numbers:
    if n in seen:
        print("Repeated:", n)
        break
    seen.append(n)
else:
    print("No repeats")

# 87. Use while-else to iterate until sum > 50, else print "Sum did not exceed 50"
numbers = [10, 15, 5, 7]
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    if total > 50:
        break
    i += 1
else:
    print("Sum did not exceed 50")

# 88. Use for-else to find divisible numbers by 7 in a range
for n in range(1, 20):
    if n % 7 == 0:
        print(n, "is divisible by 7")
        break
else:
    print("No numbers divisible by 7 found")

# 89. Use while-else to print "Loop finished" if break never occurs
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")

# 90. Use for-else to check if a password contains digits, else print "No digits in password"
password = "Python"
for ch in password:
    if ch.isdigit():
        print("Digit found in password")
        break
else:
    print("No digits in password")

# 91. Combine if and for: print even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        print(n)

# 92. Combine while and if: input numbers until negative, print even numbers only
while True:
    num = int(input("Enter number (negative to stop): "))
    if num < 0:
        break
    if num % 2 == 0:
        print(num)

# 93. Nested if: classify numbers into positive even, positive odd, negative even, negative odd
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative even")
    else:
        print("Negative odd")
else:
    print("Zero")

# 94. Nested loops: print multiplication table from 1 to 5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("")

# 95. Loop inside if: print numbers divisible by 3 if a condition is True
check = True
if check:
    for i in range(1, 20):
        if i % 3 == 0:
            print(i)

# 96. Use break inside nested loops to exit all loops
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            break
        print(i, j)
    else:
        continue
    break

# 97. Use continue to skip numbers divisible by 5 in a for loop
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)

# 98. Count how many numbers in a list are greater than 10
numbers = [5, 12, 18, 7, 20]
count = 0
for n in numbers:
    if n > 10:
        count += 1
print("Numbers greater than 10:", count)

# 99. Check for prime numbers from 1 to 50 using nested loops and if
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is prime")

# 100. Print a pattern using for loop and if-else conditions
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print("")

