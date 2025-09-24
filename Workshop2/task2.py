"""Expanding on the first task, write a decorator that prints the type of operation, the operands,
and the result of the operation. Use f-strings for the output."""

from task1 import operation

def operation_decorator(func):
    def wrapper(op, a, b):
        result = func(op, a, b)
        print(f"Operation: {op}, Operands: {a}, {b}, Result: {result}")
        return result
    return wrapper
decorated_operation = operation_decorator(operation)

print(decorated_operation("add", 10, 5))
print(decorated_operation("subtract", 10, 5))
print(decorated_operation("multiply", 10, 5))
print(decorated_operation("divide", 10, 5))





