
out_file = open("name.txt", 'w')
name = input("Enter name:")
out_file.write(name)
out_file.close()

in_file = open("name.txt", 'r')
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
total = number1 + number2
print(total)
