"""

print("Akash Jeganath")
print("o----")
print(" ||||")
print("*" * 10)


price = 10
rating = 4.9
name = "Akash"
is_published = False

print(price)
print(is_published)


print("______________________________________________________________")

name = input("What is your first name? ")
print("Hi " + name)

print("______________________________________________________________")

name = input("What is your first name? ")
color = input("What is your favourite color? ")

print(name + " likes " + color)

print("______________________________________________________________")


birth_year = input("Birth year: ")
age = 2019 - int(birth_year)

print(age)

print("______________________________________________________________")

birth_year = input("Birth year: ")
age = 2019 - int(birth_year)

print(type(age))

print("______________________________________________________________")


weight_pounds = input("Weight: ")

weight_kg = int(weight_pounds) * 0.45

print(weight_kg)

print("______________________________________________________________")
"""
"""
new = "I am Akash"
print(new[0:-3])

all = new[:]
print(all)

name = "Jennifer"
print(name[1:-1])

print("______________________________________________________________")
"""
""" ***Formatted String****"""
"""
first = "Akash"
last = "Jeganath"

message = first + " [" + last + "] is a coder"
formattedMsg = f"{first} [{last}] is a coder"

print(message)
print(formattedMsg)
"""

"""/// To define formatted strings, pre fix your string with 'f' and use curly braces '{} to dinamically insert 
values """

"""
print("______________________________________________________________")

print("***String Methods****")

course = "Python for Beginners"

print(len(course));  // to count the number of characters in string
print(course)
print(course.upper())
print(course.lower())
print(course.find("o"))
print(course.replace("Beginners", "Absolute Beginners"))

print("Python" in course)
print("python" in course)


print("______________________________________________________________")

print("***Arithmetic Operations****")

print(10 / 2)
print(10 // 2)
print(10 ** 2)

x = 10
x = x + 3
x += 3
x -= 2
print(x)

"""
"""
print("______________________________________________________________")

print("***Operator Precedence (BODMAS) ****")

x = 10 + 3 * 2
print(x)
"parenthesis
exponentiation 2**3
multiplication or division
addition or subtraction"

y = (10 + 3) * 2 ** 2
print(y)

z = (2 + 3) * 10 - 3
print(z)

print("______________________________________________________________")
"""
"""
print("*** Math Functions ****")

x = 6.9
print(round(x))
print(abs(-6.9))

import math

print(math.floor(6.9))
print(math.ceil(6.9))



print("______________________________________________________________")

print("*** If Statements ****")

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

elif is_cold:
    print("It's a cold day")
    print("Wear warm cloth")
else:
    print("It's a lovely day")

print("Enjoy your day")

"____Exercise____"

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print (f"Down Payment: ${down_payment}")


print("______________________________________________________________")

print("*** Logical Operators ****")

has_high_income = False
has_good_credit = False

if has_good_credit or has_high_income:
    print("Eligible for Loan")
else:
    print("Sorry you are not Eligible for Loan")


print("______________________________________________________________")

print("*** Comparison Operators ****")

temperature = 29

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

"____Exercise____"

name = "Akash Jeganath"

if len(name) < 3:
    print("Name must be at least 3 characters")

elif len(name) > 50:
    print("Name can be maximum of 50 characters")

else:
    print("Name looks good!")


print("______________________________________________________________")

print("*** While Loops ****")

i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")


print("______________________________________________________________")

print("*** Guessing Game ****")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("Sorry, you failed!")
 


print("______________________________________________________________")

print("*** Car Game ****")

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Yob WTF Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print
start - to start the car
stop - to stop the car
quit - to quit'
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")



print("______________________________________________________________")

print("*** For Loops ****")

prices = [10, 20, 30, 9]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")



print("______________________________________________________________")

print("*** Nested Loops ****")

for x in range (4):
    for y in range (3):
        print(f"({x},{y})")
        
"""

print("______________________________________________________________")

print("*** Lists ****")

names = ["Serah", "Akash", "John", "Teddy"]
print(names[-2])
names[0] = "Sarah"
print(names)

"""Write a program to find the largest number in a list"""
    