# Problem 1:
# Write a Python program that checks if a number is positive. If it is, print "The number is positive."
number = 5
if number > 0:
    print("The number is positive.")  # Expected output: The number is positive.

# Problem 2:
# Write a Python program that checks if a number is negative. If it is, print "The number is negative."
number = -3
if number < 0:
    print("The number is negative.")  # Expected output: The number is negative.

# Problem 3:
# Write a Python program that checks if a number is zero. If it is, print "The number is zero."
number = 0
if number == 0:
    print("The number is zero.")  # Expected output: The number is zero.

# Problem 4:
# Write a Python program that checks if the age is greater than or equal to 18. If it is, print "You are an adult."
age = 20
if age >= 18:
    print("You are an adult.")  # Expected output: You are an adult.

# 5. Write a Python program that checks if a person is a teenager (age between 13 and 19). If they are, print "You are a teenager."
age = 15
if 13 <= age <= 19:
    print("You are a teenager.")  # Expected output: You are a teenager.

# 6. Write a Python program that checks if a number is even. If it is, print "The number is even."
number = 4
if number % 2 == 0:
    print("The number is even.")  # Expected output: The number is even.

# 7. Write a Python program that checks if a number is odd. If it is, print "The number is odd."
number = 7
if number % 2 != 0:
    print("The number is odd.")  # Expected output: The number is odd.

# 8. Write a Python program that checks if a score is an A (90 or above). If it is, print "You got an A!"
score = 92
if score >= 90:
    print("You got an A!")  # Expected output: You got an A!

# 9. Write a Python program that checks if the temperature is below freezing (32 degrees Fahrenheit). If it is, print "It's freezing!"
temperature = 30
if temperature < 32:
    print("It's freezing!")  # Expected output: It's freezing!

# 10. Write a Python program that checks if a number is both greater than 10 and less than 20. If it is, print "The number is between 10 and 20."
number = 15
if 10 < number < 20:
    print("The number is between 10 and 20.")  # Expected output: The number is between 10 and 20.







# 2. What's your age? If it's greater than 10, print "You are growing up!"
age = int(input("What's your age? "))

if age == 10:
    print("You're 10, me too!")
elif age < 10:
    print("You're very young.")
else:
    print("You're older than me")

# 3. Is today sunny? If yes, print "Let's go outside!"
weather = input("Is today sunny? (yes/no): ")
if weather == "yes":
    print("Let's go outside!")

# 4. Did you finish your homework? If no, print "Finish it now!"
homework_done = input("Did you finish your homework? (yes/no): ")
if homework_done == "no":
    print("Finish it now!")

# 5. Do you like ice cream? If yes, print "Let's have some!"
ice_cream = input("Do you like ice cream? (yes/no): ")
if ice_cream == "yes":
    print("Let's have some!")

# 6. Is your room tidy? If no, print "Clean it up!"
room_tidy = input("Is your room tidy? (yes/no): ")
if room_tidy == "no":
    print("Clean it up!")

# 7. Have you brushed your teeth? If no, print "Go brush them!"
teeth_brushed = input("Have you brushed your teeth? (yes/no): ")
if teeth_brushed == "no":
    print("Go brush them!")

# 8. Did you drink water today? If no, print "Stay hydrated!"
water_drunk = input("Did you drink water today? (yes/no): ")
if water_drunk == "no":
    print("Stay hydrated!")

# 9. Do you have any siblings? If yes, print "Say hi to them!"
siblings = input("Do you have any siblings? (yes/no): ")
if siblings == "yes":
    print("Say hi to them!")

# 10. Did you make your bed? If no, print "Make it now!"
bed_made = input("Did you make your bed? (yes/no): ")
if bed_made == "no":
    print("Make it now!")