num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

print("\n Choose Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1-4):")

if choice == "1":
    print("Result =", num1 + num2)
elif choice == "2":
    print("Result =", num1 - num2)
elif choice == "3":
    print("Result =", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Choice")