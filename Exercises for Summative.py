#!/usr/bin/env python
# coding: utf-8

# # Conditionals (Exercises from Canvas)

# In[16]:


# Create a code that asks the user for two numbers and returns which number is greater and by how much it is greater than the other

# Ask for user input

num_1 = float(input("Enter first number here: ")) # used float to give user flexibility
num_2 = float(input("Enter second number here: "))

if num_1 > num_2:
    greater_num = num_1 - num_2
    print(str(num_1) + " is greater than " + str(num_2) + " by " + str(greater_num))
    
else:
    greater_num2 = num_2 - num_1
    print(str(num_2) + " is greater than " + str(num_1) + " by " + str(greater_num2))


# In[32]:


# A well-ordered number is an integer whose digits increase from left to right. Create a code that will ask the user for a THREE-DIGIT integer and display whether or not the number is well-ordered.

# Ask for user input
user_input = int(input("Enter a three-digit integer here: "))

def well_ordered(number): # number is the parameter
    number_str = str(user_input) # Number is converted to a string to index it. Indexing is NOT applicable for integers.
    if number_str[0] < number_str[1] < number_str [2]:
        return True
    else:
        return False
    
result = well_ordered(user_input) # user_input is the argument
print(result) # To capture and restore the returned value in the function


# In[41]:


# Ask the user to input two integers, and check whether the bigger number is divisible by the smaller one


# Ask for user input
int_1 = int(input("Enter first integer here: "))
int_2 = int(input("Enter second integer here: "))

if int_1 > int_2:
    print(str(int_1) + " is greater than " + str(int_2))
    if int_1 % int_2 == 0:
        print(str(int_1) + " is divisible by " + str(int_2))
    else:
        print(str(int_1) + " is not divisible by " + str(int_2))
        
elif int_1 < int_2:
    print(str(int_2) + " is greater than " + str(int_1))
    if int_2 % int_1 == 0:
        print(str(int_2) + " is divisible by " + str(int_1))
    else:
        print(str(int_2) + " is not divisible by " + str(int_1))
        
else:
    print("Both numbers are equal.") # Must put this as user may input the same integers.


# In[42]:


# A VBA Number is a number that meets the following conditions:
# a. It is divisible by 3.
# b. It is an even number.
# c. It is a perfect square.
# Ask the user to input a number and output whether or not it is a VBA Number.

# Ask for user input
user_input = int(input("Enter a number: "))

if user_input % 3 == 0 and user_input % 2 == 0 and (user_input ** 0.5).is_integer():
    print("It is a VBA Number.")
    
else:
    print("It is not a VBA Number.")


# In[46]:


# Write a function that takes a 5-character string as a parameter and returns the string in reverse order.

string = str(input("Enter a five character word here: "))

def five_character(word):
    if len(string) == 5:
        return word[::-1] # The [::-1] is a slicing notation in Python that reverses the order of elements in a sequence.
    
    else:
        return False

five_character(string)


# In[3]:


# Write a function that takes a 5-character string as a parameter and returns the string in reverse order.

string = str(input("Enter a five character word here: "))

def five_character(word):
        return word[::-1] # The [::-1] is a slicing notation in Python that reverses the order of elements in a sequence.

five_character(string)


# In[15]:


# Write a function that checks whether a string is a palindrome or not. (A palindrome is a word that is spelled the same when read forwards and backwards → racecar, tacocat, abba).

string = str(input("Enter a word here: "))
lowercase_string = string.lower() # Converted user input to lowercase since Python is case-sensitive.

def palindrome_check(word):
    reverse = lowercase_string[::-1] # The [::-1] is a slicing notation in Python that reverses the order of elements in a sequence.
    lowercase_reverse = reverse.lower() # Converted reversed user input to lowercase since Python is case-sensitive.
    if lowercase_reverse == lowercase_string:
        print("It is a palindrome.")
        
    else:
        print("It is not a palindrome.")
    
palindrome_check(string)


# # Loops (Exercises from Canvas)

# In[18]:


# Classic Looping Problem: Write a function that iterates through each number from 1 to 100. Print each number.
# a. If the number is divisible by 3, instead of the number, print "Fizz"
# b. If the number is divisible by 5, instead of the number, print "Buzz"
# c. If the number is divisible by both 3 and 5, instead of the number, print "FizzBuzz"

for number in range (0, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)


# In[37]:


# Find the Greatest Common Factor (GCF) and Least Common Multiple (LCM) of two numbers.
import math

num_1 = int(input("Enter first number here: "))
num_2 = int(input("Enter second number here: "))

def calculate_gcf_lcm(num_1, num_2):
    gcf = math.gcd(num_1, num_2)
    lcm = math.lcm(num_1, num_2)
    print("The GCF of", num_1, "and", num_2, "is", gcf)
    print("The LCM of", num_1, "and", num_2, "is", lcm)

calculate_gcf_lcm(num_1, num_2)


# In[38]:


# Ask the user to input an integer from 1 to 500. Print the multiples of that number less than or equal to 500.

user_input = int(input("Enter an integer from 1 to 500: "))

if 1 <= user_input <= 500:
    for i in range(1, 501 // user_input + 1):
        multiples = user_input * i
        print(multiples)
else:
    print("Please try again. Input an integer from 1 to 500.")


# In[39]:


# Input a number “n”. Print the first n perfect squares.
n = int(input("Enter a number: "))

for i in range(1, n+1):
    square = i ** 2
    print(square)


# In[41]:


# Print the number of factors a number n has.

n = int(input("Enter a number: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

print("The number of factors of", n, "is", count)


# In[40]:


# Create a code that prints how many prime numbers there are from 1 to a user-inputted number.

n = int(input("Enter a number: "))
count = 0

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print("The number of prime numbers from 1 to", n, "is", count)


# In[43]:


# Create a while loop that asks for the user to input integers until they input a negative integer. Afterwards, print the maximum and minimum among the numbers inputted.

numbers = []
while True:
    num = int(input("Enter an integer (or a negative integer to stop): "))
    if num < 0:
        break
    numbers.append(num)

if numbers:
    maximum = max(numbers)
    minimum = min(numbers)
    print("Maximum value: ", maximum)
    print("Minimum value: ", minimum)
else:
    print("No numbers were entered.")


# In[46]:


#  Collatz Conjecture:
# a. If the number is even, divide it by two.
# b. If odd, multiply by 3 and add 1.

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        steps += 1
    return steps

# Ask for user input
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    steps_taken = collatz_steps(number)
    print("The total number of steps taken to solve the Collatz conjecture for", number, "is", steps_taken)


# In[ ]:


# Print the prime factorization of a user-inputted number.
def prime_factorization(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

# Ask for user input
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    factorization = prime_factorization(number)
    print("Prime factorization of", number, "is:", " x ".join(map(str, factorization)))


# In[ ]:


# Create a function that converts a number in binary (base-2) to decimal (base-10). Create also a decimal to binary converter.
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        binary //= 10
        power += 1
    return decimal


def decimal_to_binary(decimal):
    if decimal == 0:
        return 0
    binary = ""
    while decimal != 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return int(binary)


# Test binary to decimal conversion
binary_input = input("Enter a binary number: ")
decimal_result = binary_to_decimal(int(binary_input))
print("Decimal conversion:", decimal_result)


# Test decimal to binary conversion
decimal_input = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_input)
print("Binary conversion:", binary_result)


# # Conditionals and Loops (Exercises)

# In[2]:


# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700.

def divisibility():
    divisible_numbers = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            divisible_numbers.append(number)
    return divisible_numbers

numbers = divisibility()
print(numbers)


# In[11]:


# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

# Ask for user input
user_input = float(input("Enter temperature here: "))
conversion = str(input("Enter C if temperature is in Celsius and F is Fahreinheit: "))

def TempConv(temp, conv):
    if conv.upper() == "C":
        celsius = (9/5 * temp) + 32
        return str(celsius) + "F"
        
    elif conv.upper() == "F":
        fahreinheit = 5/9 * (temp - 32)
        return str(fahreinheit) + "C"

    else:
        return "Invalid input."

TempConv(user_input, conversion)


# In[12]:


# Write a Python program to guess a number between 1 and 9.

import random

def guess_number():
    secret_number = random.randint(1, 9)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()


# # If Statements (Exercises from Canva)

# In[48]:


# Write a program that prompts the user to enter a number and checks if it is positive, negative, or zero. Display an appropriate message based on the input. 

n = int(input("Please input a number here... "))

if n > 0:
    print("The number is a positive integer.")
    
elif n < 0:
    print("The number is a negative integer.")
    
else:
    print("The number is zero.")


# In[ ]:


# Write a program that prompts the user to enter a numeric grade and converts it to a letter grade using the following scale:
# * 92 and above: A * 80-91: B
# * 70-79: C
# * 60-69: D
# * Below 60: F
# * Display the corresponding letter grade.

n = int(input("Please enter a numeric grade here... "))

if n >= 92:
    print ("Your grade is A.")
    
elif n >= 80 and n < 92:
    print("Your grade is B.")
    
elif n >= 70 and n < 79:
    print("Your grade is C.")
    
elif n >= 60 and n < 69:
    print("Your grade is D.")

else:
    print("Your grade is F.")


# In[ ]:


# Write a program that prompts the user to enter a year and determines whether it is a leap year or not. A leap year is divisible by 4 but not divisible by 100 unless it is also divisible by 400. Display an appropriate message based on the input.

y = int(input("Please enter a year here... "))

if y % 4 == 0 and y % 100 != 0  or y % 400 == 0:
    print("The year entered is a leap year.")
    
else:
    print("The year entered is not a leap year.")


# In[ ]:


# Miscellaneous


# In[49]:


# A government wants to provide student loans to students in their country. But in-order for a student to be eligible to get a student loan, he/she must be in age range 17 to 21, and must have a minimum of 80% score in academics. Write a program to accept the name, age, and marks of a student and display if he/she is eligible for the loan or not.

name = input("Type your name here: ")
age = int(input("Type your age here: "))
score = float(input("Type your academic score here: "))

if age >= 17 and age <=21 and score >= 80:
    print(name + " is eligible for a loan.")
else:
    print(name + " is not eligible for a loan.")


# In[50]:


# Check if the nth power of a number is even or not. (Take the number, and the power as input)

number = float(input("Type your number here: "))
power = int(input("Type the nth power here: "))

check = number**power

if check % 2 == 0:
    print("The number is an even number.")
    
else:
    print("The number is an odd number.")


# In[51]:


# Check if a triangle is a right triangle or isoceles triangle.

# Note: Right triangles: If it satisfies the Pythagorean Theorem.
# Note: Isosceles triangles: If two or more of the triangles sides are equal.

a = float(input("Type the first side of the triangle: "))
b = float(input("Type the second side of the triangle: "))
c = float(input("Type the hypotenuse of the triangle: "))

if (c==(a**2 + b**2)**(1/2)):
    print("It is a right triangle.")
    
elif a == b or a == c or b == c:
    print("It is an isoceles triangle.")
    
else:
    print("Triangle is not of known type.")


# In[57]:


# Check if the character entered by the user is an uppercase character or a lower case character.

Alphabet = ord(input("Enter the character : "))

if(Alphabet>=65 and Alphabet<=90):
    print("Uppercase letter")

elif(Alphabet>=97 and Alphabet<=122):
    print("Lowercase letter")
else:
    print("Not an Alphabet")


# # For Loops (Exercises from Canva)

# In[13]:


# Write a program that calculates and prints the sum of all numbers from 1 to 10 (inclusive) using a for loop.

sum = 0

for i in range(1,11):
    sum = sum + i
    
print(str("The sum of all numbers from 1 to 10 is ") + str(sum))


# In[ ]:


# Write a program that prompts the user to enter a number and prints the multiplication table for that number up to 10.

number = int(input("Enter a number here: "))

for i in range(1, 11):
    product = number * i
    print(product)


# In[ ]:


# Write a program that prompts the user to enter a range (start and end numbers) and prints all prime numbers within that range. Prime numbers are numbers that are only divisible by 1 and themselves.

start = int(input("Enter the start number of the range: "))
end = int(input("Enter the end number of the range: "))

print("Prime numbers in the range", start, "to", end, ":")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True

        # Check for factors from 2 to the square root of the number
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

