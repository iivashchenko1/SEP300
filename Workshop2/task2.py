"""Expanding on the first task, write a decorator that prints the type of operation, the operands,
and the result of the operation. Use f-strings for the output."""

def operation_decorator(func):
    def wrapper(op, a, b):
        result = func(op, a, b)
        print(f"Operation: {op}\nOperands: {a}, {b}\nResult: {result}")
        return result
    return wrapper

@operation_decorator
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

# User picks an operation
op = input("Enter operation (add/subtract/multiply/divide): ")
a = float(input("Enter first operand: "))
b = float(input("Enter second operand: "))

result = operation(op, a, b)
print(result)




