try:
    age = int(input("Enter age: "))
    print("Age entered:", age)
except ValueError:
    print("Invalid input. Please enter a number.")
