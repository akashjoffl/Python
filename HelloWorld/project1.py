print("______________________________________________________________")

print("*** Project: Weight Converter ****")

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")

elif unit.upper() == "K":
    converted = weight // 0.45
    print(f"You are {converted} lbs")

else:
    print("Input valid unit")
