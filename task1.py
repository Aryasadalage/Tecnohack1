def f1(x, y):
    z=x+y
    print("Addition is:",z)

def f2(x, y):
    z=x - y
    print("Subtraction is:",z)

def f3(x, y):
    z= x * y
    print("Multiplication is:",z)

def f4(x, y):
    if y != 0:
        z=x / y
        print("Division is:",z)
    else:
        print("Error!!!!!")

print("*******************Simple calculator************************")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            f1(num1, num2)
        elif choice == '2':
            f2(num1, num2)
        elif choice == '3':
            f3(num1, num2)
        elif choice == '4':
             f4(num1, num2)

        break
    else:
        print("Error!!!!!. Please enter a valid choice.")

