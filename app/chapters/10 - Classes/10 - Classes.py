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
          f"{self.adjective}, and I'm {self.gender}."]

alice = Human("Alice", 10, "female", "brave")
print(alice.describe())