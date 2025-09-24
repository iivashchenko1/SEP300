from operations import operation, sum_numbers

result1 = operation("add", 10, 5)
print(f"Result of Task 1: {result1}")
result2 = operation("subtract", 10, 5)
print(f"Result of Task 1: {result2}")
result3 = operation("multiply", 10, 5)
print(f"Result of Task 1: {result3}")
result4 = operation("divide", 10, 5)
print(f"Result of Task 1: {result4}")   

num_list = list(map(int, input("Enter integers separated by spaces: ").split()))
sum_numbers(num_list)