test_users = [
    {"name": "A", "age": 17},
    {"name": "B", "age": 18},
    {"name": "C", "age": 25},
    {"name": "D", "age": -1}
]

for user in test_users:
    if user["age"] >= 18:
        print(user["name"], "-> Eligible")
    else:
        print(user["name"], "-> Not Eligible")
