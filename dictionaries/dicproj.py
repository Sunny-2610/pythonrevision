# going to develop a project related to dictionaries

contacts = {}

while True:
    name = input("Name:")

    if name == "quit":
        break

    phone = input("Phone:")

    contacts[name] = phone

print(contacts)   