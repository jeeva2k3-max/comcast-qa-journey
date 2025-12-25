with open("users.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(",")
        age = int(age)

        if age < 0:
            result = "Invalid age"
        elif age >= 18:
            result = "Eligible"
        else:
            result = "Not eligible"

        print(name, "->", result)
