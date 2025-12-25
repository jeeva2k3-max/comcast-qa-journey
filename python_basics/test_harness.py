def check_pass(mark):
    if mark < 0 or mark > 100:
        return "Invalid"
    elif mark >= 60:
        return "Pass"
    else:
        return "Fail"

test_cases = [100, 75, 60, 59, 0, -1, 101]

for case in test_cases:
    result = check_pass(case)
    print("Input:", case, "| Result:", result)
