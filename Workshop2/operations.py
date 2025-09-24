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

num_list = list(map(int, input("Enter integers separated by spaces: ").split()))

def sum_numbers(num_list):
    total = sum(num_list)
    print(f"The total sum is: {total}")

sum_numbers(num_list)