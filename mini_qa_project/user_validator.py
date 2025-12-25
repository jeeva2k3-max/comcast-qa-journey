def validate_user(name, age):
    try:
        age = int(age)
    except (ValueError, TypeError):
        return "Invalid data"

    if age < 0:
        return "Invalid age"
    elif age >= 18:
        return "Eligible"
    else:
        return "Not eligible"


with open("users_data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")

        if len(parts) != 2:
            print("Invalid record format")
            continue

        name, age = parts
        result = validate_user(name, age)
        print(name, "->", result)
