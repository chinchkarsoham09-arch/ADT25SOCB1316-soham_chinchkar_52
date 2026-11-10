# 1. read() operation

file = open("data.txt", "r")

content = file.read()
print("Content of file:")
print(content)

file.close()


# 2. readline() operation

file = open("data.txt", "r")

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()

print("\nUsing readline():")
print(line1)
print(line2)
print(line3)
print(line4)

file.close()


# 3. readlines() operation

file = open("data.txt", "r")

lines = file.readlines()

print("\nUsing readlines():")
print(lines)

file.close()
