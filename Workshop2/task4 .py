"""Using the function from Task 3, write a decorator that prints the names of all the arguments
passed to the function. 

"""


def print_args(func):
    def wrapper(*args, **kwargs):
        print("Provided arguments:")
        for arg in args:
            print(arg, end=" ")
        print()  
        return func(*args, **kwargs)
    return wrapper

@print_args
def sum_numbers(*args):
    total = sum(args)
    print(f"The sum is: {total}")

# Example run
nums = list(map(int, input("Enter integers separated by spaces: ").split()))
sum_numbers(*nums)






    
