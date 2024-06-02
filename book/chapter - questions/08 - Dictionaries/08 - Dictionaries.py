# Question 1: Create a dictionary with keys "name", "age", and "city", and print it.
person = {"name": "Alice", "age": 10, "city": "Wonderland"}
print(person)

# Question 2: Add a new key-value pair "favorite_color" with value "blue" to the dictionary and print it.
person["favorite_color"] = "blue"
print(person)

# Question 3: Change the value of "age" to 11 and print the updated dictionary.
person["age"] = 11
print(person)

# Question 4: Remove the key "city" from the dictionary and print the updated dictionary.
del person["city"]
print(person)

# Question 5: Print all the keys in the dictionary.
print(person.keys())

# Question 6: Print all the values in the dictionary.
print(person.values())

# Question 7: Print the value associated with the key "name".
print(person["name"])

# Question 8: Check if the key "favorite_food" is in the dictionary and print the result.
print("favorite_food" in person)

# Question 9: Use a for loop to print all the key-value pairs in the dictionary.
for key, value in person.items():
    print(key, ":", value)

# Question 10: Create a dictionary of three friends with their ages and print it.
friends_ages = {"Bob": 10, "Charlie": 11, "Daisy": 10}
print(friends_ages)



group = {
    "first_name": "Tommy",
    "last_name": "Tutone",
    "age": None,
    "top_song": [867, 5309, "Jenny-Jenny"]
}

artist = {
    "first_name": "Rick",
    "last_name": "Astley",
    "age": 58,
    "top_song": {
        1: "Never Gonna Give You Up",
    }
}


# Create a dictionary called phone_book
# It should have three keys called "first_name", "last_name" and "mobile"


# Create a dictionary called to_do_list
# It should have two list which are assigned to a key called "incomplete" and "complete"