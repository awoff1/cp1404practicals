"""Alex Woffenden"""

name = input("Enter name:")
while name == "" :
    print("Name cannot be blank")
    name = input("Enter name:")

print(name[::2])
