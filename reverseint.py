# reversing integer
number = int(input("Input the number you want to reverse: "))
reverse = 0
if number < 0:
    number = abs(number)
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    print(reverse * -1)
else:
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    print(reverse)
