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

first = "Akash"
last = "Jeganath"

message = first + " [" + last + "] is a coder"
formattedMsg = f"{first} [{last}] is a coder"

print(message)
print(formattedMsg)

"""/// To define formatted strings, pre fix your string with 'f' and use curly braces '{} to dinamically insert 
values """

