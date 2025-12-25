def validate_user(user):
    if user["age"] < 0:
        return "Invalid age"
    elif user["age"] >= 18:
        return "Eligible"
    else:
        return "Not eligible"

test_users = [
    {"name": "A", "age": 17},
    {"name": "B", "age": 18},
    {"name": "C", "age": 30},
    {"name": "D", "age": -5}
]

for user in test_users:
    result = validate_user(user)
    print(user["name"], "->", result)
