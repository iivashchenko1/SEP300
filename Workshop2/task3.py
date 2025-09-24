"""Write a function that accepts any number of integer arguments and prints their total sum."""

num_list = list(map(int, input("Enter integers separated by spaces: ").split()))

def sum_numbers(num_list):
    total = sum(num_list)
    print(f"The total sum is: {total}")

sum_numbers(num_list)