# Question 1: Create a class named Dog and print "This is a Dog class" inside it.
class Dog:
    def __init__(self):
        print("This is a Dog class")


# Create an instance of the Dog class
dog1 = Dog()


# Question 2: Add an attribute name to the Dog class and set it using the __init__ method.
class Dog:
    def __init__(self, name):
        self.name = name


# Create an instance of the Dog class with the name "Buddy"
dog2 = Dog("Buddy")
print(dog2.name)


# Question 3: Add a method bark to the Dog class that prints "Woof!".
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")


# Create an instance of the Dog class and call the bark method
dog3 = Dog("Buddy")
dog3.bark()


# Question 4: Create a class named Cat with a method meow that prints "Meow!".
class Cat:
    def meow(self):
        print("Meow!")


# Create an instance of the Cat class and call the meow method
cat1 = Cat()
cat1.meow()


# Question 5: Create a class named Person with attributes name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an instance of the Person class and print the attributes
person1 = Person("Alice", 10)
print(person1.name, person1.age)


# Question 6: Add a method greet to the Person class that prints "Hello, my name is name".
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")


# Create an instance of the Person class and call the greet method
person2 = Person("Alice", 10)
person2.greet()


# Question 7: Create a class named Car with attributes brand and model.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Create an instance of the Car class and print the attributes
car1 = Car("Toyota", "Corolla")
print(car1.brand, car1.model)


# Question 8: Add a method honk to the Car class that prints "Beep beep!".
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def honk(self):
        print("Beep beep!")


# Create an instance of the Car class and call the honk method
car2 = Car("Toyota", "Corolla")
car2.honk()


# Question 9: Create a class named Book with attributes title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Create an instance of the Book class and print the attributes
book1 = Book("Harry Potter", "J.K. Rowling")
print(book1.title, book1.author)


# Question 10: Add a method describe to the Book class that prints "The book title is written by author".
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"The book {self.title} is written by {self.author}")


# Create an instance of the Book class and call the describe method
book2 = Book("Harry Potter", "J.K. Rowling")
book2.describe()


class Human:
    def __init__(self, name, age, gender, adjective):
        self.name = name
        self.age = age
        self.gender = gender
        self.adjective = adjective

    def describe(self):
        return [
            f"My name is {self.name}",
            f"I'm {self.age} years old",
            f"{self.adjective}, and I'm {self.gender}.",
        ]


alice = Human("Alice", 10, "female", "brave")
print(alice.describe())
