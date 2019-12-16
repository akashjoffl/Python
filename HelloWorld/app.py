print("*** Exercise: List Method ****")

numbers = [3, 3, 5, 6, 7, 7, 8, 6, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
