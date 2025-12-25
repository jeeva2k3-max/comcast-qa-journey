file = open("users.txt", "r")

for line in file:
    name, age = line.strip().split(",")
    age = int(age)

    if age < 0:
        print(name, "-> Invalid age")
    elif age >= 18:
        print(name, "-> Eligible")
    else:
        print(name, "-> Not eligible")

file.close()
