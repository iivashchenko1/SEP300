# Task 1

"""Create a Python script that generates a list 
with all numbers between 0 and 20. Then, your
script should print all the even numbers in this list."""

list = list(range(0,21,2))
print(list)

#Task 2
#Create a Python script that starts by storing the dictionary below.

"""Your script should then:
1. Ask the user to enter the name of a person whose number they want to get.
2. If the entered name exists as a key in the dictionary, display the corresponding
number (value).
3. If the entered name does not exist, display an error message alerting the user that
the person is not in the dictionary."""

phone_book = {
"Alice": "416-555-1234",
"Bob": "647-555-5678",
"Charlie": "905-555-2468",
"Diana": "289-555-1357",
"Ethan": "613-555-9876"
}

name = str(input("Enter a name of the person that you would like to reach: "))

if name in phone_book:
    print(phone_book[name])
else:
    print("Error has occured. Try another name")

#Task 3 
"""Write a Python script that prints the first N numbers of the Fibonacci sequence. The
sequence starts with 0 and 1, and each new number in the sequence is the sum of the two
numbers before it. For example, a Fibonacci sequence with 7 numbers is: [0, 1, 1, 2, 3, 5, 8]"""

N = int(input("Enter the number of Fibonacci numbers to generate:"))

if N <= 0:
    print("Error: Please enter the right number")
elif N == 1:
    print(0)
else:
    fib_sequence =[0,1]
    for i in range (2,N):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    print(fib_sequence)


#Task 4
"""Write a Python program that:
1. Starts with a set containing the words “apple” and “banana”.
2. Then, it starts a loop that asks the user what to do: add more fruits to the set,
remove fruits from the set, check if a fruit has been added to the set, or quit.
3. After the user has picked a choice, the loop should ask for more info (if required)
and output what is needed"""


fruits = {"apple", "banana"}

while True:
    print("Current fruits:", fruits)
    action = input("What do you want to do? (add/remove/check/quit): ").lower()
    if action == "add":
        new_fruit = input("Enter the fruit you want to add: ")
        if new_fruit:
            fruits.add(new_fruit)
            print("Added", new_fruit, ". Fruits are now:", fruits)
        else:
            print("No fruit entered.")
    elif action == "remove":
        rem_fruit = input("Enter the fruit you want to remove: ")
        if rem_fruit in fruits:
            fruits.remove(rem_fruit)
            print("Removed", rem_fruit, ". Fruits are now:", fruits)
        else:
            print(rem_fruit, "is not in the set.")
    elif action == "check":
        check_fruit = input("Enter the fruit to check: ")
        if check_fruit in fruits:
            print(check_fruit, "is in the set.")
        else:
            print(check_fruit, "is NOT in the set.")
    elif action == "quit":
        print("Quitting. Final fruits:", fruits)
        break
    else:
        print("Invalid action. Please choose add, remove, check, or quit.")
    

