def check_pass(mark):
    if mark < 0 or mark > 100:
        return "Invalid"
    elif mark >= 60:
        return "Pass"
    else:
        return "Fail"

test_values = [95, 60, 59, -5, 120]

for value in test_values:
    print(value, "->", check_pass(value))
