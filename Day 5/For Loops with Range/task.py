#Range Function with For Loop
total = 0
for number in range(1, 101):
    total += number

print(total)

for number in range(1, 101):  # goes from 1 up to 100 inclusive
    if number % 3 == 0 and number % 5 == 0:  # divisible by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # divisible by 5
        print("Buzz")
    else:
        print(number)  # not divisible by 3 or 5, just print the number
