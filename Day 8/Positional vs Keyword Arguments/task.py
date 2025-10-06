# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


#Functions w/ more than 1 input

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"It's so cool that you're from {location}!!")
    print(f"How is the weather in {location}?")

#greet_with("Bob Dole", "Argentina")
greet_with(name="Bob Dole", location="London")

def add(a, b):
    return a + b
x = add(3, 4)
print(x)