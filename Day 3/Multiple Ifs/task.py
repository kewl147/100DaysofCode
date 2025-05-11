print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.00.")
    elif age <= 18:
        bill = 7
        print("Teenager tickets are $7.00.")
    else:
        bill = 12
        print("Adult tickets are $12.00.")

    wantsPhoto = input("Do you want to have a photo taken? Type Y for Yes and N for No.\n")
    if wantsPhoto.upper() == "Y":
        bill += 3
        print(f"Your bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
