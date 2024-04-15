# lucky_checker.py

def is_lucky(number):
    # Check if the number is divisible by 7 or contains the digit 7
    if number % 7 == 0 or '7' in str(number):
        return True
    else:
        return False

# lucky_number_printer.py

from lucky_checker import is_lucky

for i in range(1, 101):
    if is_lucky(i):
        print("Lucky!")
    else:
        print(i)
