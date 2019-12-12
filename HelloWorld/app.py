print("______________________________________________________________")

print("*** Lists ****")

names = ["Serah", "Akash", "John", "Teddy"]
print(names[-2])
names[0] = "Sarah"
print(names)

"""Write a program to find the largest number in a list"""

numbers = [1, 15, 69, 56, 26, 48]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


"""print(max(numbers))"""
