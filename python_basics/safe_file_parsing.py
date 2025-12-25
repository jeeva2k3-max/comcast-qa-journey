with open("users.txt", "r") as file:
    for line in file:
        try:
            name, age = line.strip().split(",")
            age = int(age)

            if age < 0:
                result = "Invalid age"
            elif age >= 18:
                result = "Eligible"
            else:
                result = "Not eligible"

        except ValueError:
            result = "Bad data format"

        print(name, "->", result)
