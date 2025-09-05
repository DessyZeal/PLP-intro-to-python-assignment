num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operator = input("Enter the operation (+, -, *, /):")
if operator == "+":
    result = int(num1) + int(num2)
elif operator == "-":
    result = int(num1) - int(num2)
elif operator == "*":
    result = int(num1) * int(num2)
elif operator == "/":
    if int(num2) != 0:
        result = int(num1) / int(num2)
print("The result is:", result)
