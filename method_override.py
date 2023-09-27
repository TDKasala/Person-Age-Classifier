
# Creating Adult class with 4 attributes
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):

        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # Creating a method called can_drive that will print a message
    def can_drive(self):
        print(self.name, "is old enough to drive.")

# Creating subclass of adult class called 'Child' that has the asme attributes
class Child(Adult):

    # Initialising the same attributes and using the super()
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    # Override can_drive method to print out something different
    def can_drive(self):
        print(f"{self.name} is too young to drive")


# Requesting input from user
name = input("\nPlease enter your name: ")
age = int(input("Please enter your age: "))
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eyes colour: ")

# Checking user's age and creating an object with same attributes
if age >= 18:
    person_1 = Adult(name, age, hair_colour, eye_colour)

else:
    person_1 = Child(name, age, hair_colour, eye_colour)

person_1.can_drive()
