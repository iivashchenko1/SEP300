"""Write a function that takes three arguments: a string specifying an operation (such as 'add',
'subtract', 'multiply', or 'divide'), and two numeric operands. The function should return the
result of applying the specified operation to the operands."""

def operation(op, a, b):
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation specified."

print(operation("add", 10, 5))
print(operation("subtract", 10, 5))
print(operation("multiply", 10, 5))
print(operation("divide", 10, 5))