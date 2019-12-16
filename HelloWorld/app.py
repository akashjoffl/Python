print("*** Dictionaries ****")

customer = {
    "name": "Akash Jeganath",
    "age": 30,
    "is_verified": True
}
customer["age"] = 20
print(customer.get("dob", "4th of June 1999"))
print(customer["age"])