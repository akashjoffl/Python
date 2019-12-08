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
print("*** Math Functions ****")

x = 6.9
print(round(x))
print(abs(-6.9))

import math

print(math.floor(6.9))
print(math.ceil(6.9))

