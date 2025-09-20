def my_function():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("gray")
    print("Hello")

sky = input("Is the sky clear or cloudy today?\n").lower()

while sky not in ["clear", "cloudy"]:
    sky = input("Incorrect selection, please pick clear or cloudy:\n").lower()

my_function()
