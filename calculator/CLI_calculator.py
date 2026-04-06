def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = input("Choose: ")

    if choice == '5':
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", sub(x, y))
    elif choice == '3':
        print("Result:", mul(x, y))
    elif choice == '4':
        print("Result:", div(x, y))
    else:
        print("Invalid choice")
