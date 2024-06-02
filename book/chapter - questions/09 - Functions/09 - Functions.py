# Question 1: Write a function that prints "Hello, World!" and call it.
def greet():
    print("Hello, World!")


greet()


# Question 2: Write a function that takes a name as an argument and prints "Hello, name!".
def greet_name(name):
    print(f"Hello, {name}!")


greet_name("Alice")


# Question 3: Write a function that takes two numbers as arguments and returns their sum.
def add(a, b):
    return a + b


print(add(3, 4))


# Question 4: Write a function that takes a list of numbers and returns the largest number.
def find_max(numbers):
    return max(numbers)


print(find_max([1, 2, 3, 4, 5]))


# Question 5: Write a function that takes a number and returns True if the number is even, else False.
def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))


# Question 6: Write a function that takes a list of words and prints each word on a new line.
def print_words(words):
    for word in words:
        print(word)


print_words(["apple", "banana", "cherry"])


# Question 7: Write a function that returns the length of a string.
def string_length(s):
    return len(s)


print(string_length("hello"))


# Question 8: Write a function that takes a number and prints its multiplication table up to 10.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


multiplication_table(3)


# Question 9: Write a function that takes a list of numbers and returns the average.
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(calculate_average([1, 2, 3, 4, 5]))


# Question 10: Write a function that takes a string and returns the string in reverse.
def reverse_string(s):
    return s[::-1]


print(reverse_string("hello"))


print("1. Get two slices of bread.")
print("2. Put some cheese and ham on one slice.")
print("3. Place the other slice of bread on top.")
print("4. Enjoy your sandwich!")


def make_sandwich():
    return (
        "1. Get two slices of bread.",
        "2. Put some cheese and ham on one slice.",
        "3. Place the other slice of bread on top.",
        "4. Enjoy your sandwich!",
    )


print(make_sandwich())


# Create a function called "bake_cake" and return the steps of baking a cake


# Create a function called "friends" and return a list of friends
