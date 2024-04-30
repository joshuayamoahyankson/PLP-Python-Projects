"""Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.
Create a GitHub repository for your assignment and submit the link.
"""

class Person:
    """This function initialises the person class"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """A method that returns a person's information"""
        return ("My name is {} and I am {} years of age. By gender, I am a {}".format(self.name, self.age, self.gender))

person = Person("Joshua Yamoah Yankson", 29, "Male")
print(person.introduce())
