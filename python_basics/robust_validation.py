def validate_user(user):
    try:
        age = int(user["age"])
    except (KeyError, ValueError, TypeError):
        return "Invalid data"

    if age < 0:
        return "Invalid age"
    elif age >= 18:
        return "Eligible"
    else:
        return "Not eligible"


test_users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": "x"},
    {"name": "C"},
    {"name": "D", "age": -5}
]

for user in test_users:
    print(user.get("name", "Unknown"), "->", validate_user(user))
