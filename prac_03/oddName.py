"""Alex Woffenden"""


def main():

    name = get_name()
    frequency = int(input("Enter frequency:"))
    print_name(name,frequency)


def get_name():
    name = input("Enter name:")
    while name == "":
        print("Name cannot be blank")
        name = input("Enter name:")
    return name


def print_name(name,frequency):
    print(name[::frequency])

main()
