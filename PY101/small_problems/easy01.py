def is_odd(number):
    return abs(number) % 2 != 0

def print_odds():
    for num in range(1, 100):
        if num % 2 != 0:
            print(num)

def print_evens():
    for n in range(2, 100, 2):
        print(n)

def calc_sq_measurements(length, width):
    sq_meters = length * width
    return (sq_meters, sq_meters * 10.7639)

def get_measurements():
    length = float(input("Enter the length of the room in meters: "))
    width = float(input("Enter the width of the room in meters: "))

    sq_meters, sq_feet = calc_sq_measurements(length, width)

    print(f"The area of the room is {sq_meters:.2f} "
          f"square meters ({sq_feet:.2f} square feet).")
    
def get_amounts():
    bill = float(input('Enter the total bill amount: '))
    tip_percentage = int(input('Enter the tip percentage as an integer: '))

    tip = bill * (tip_percentage / 100)
    total = bill + tip

    print(f"The tip is ${tip:.2f}")
    print(f"The total amount due is ${(total):.2f}")

def sum_product():
    def invalid_num(num):
        try:
            int(num)
        except ValueError:
            return True
        return False
    
    target = input("Please enter an integer greater than 0: ")

    while invalid_num(target):
       print("An invalid number was entered. Try again: ")
       target = int(input("Please enter an integer greater than 0: ")) 

    operation = input('Enter "s" to compute the sum, or "p" to compute the product. ').lower()

    while operation not in ['s', 'p']:
        operation = input('Enter "s" to compute the sum, or "p" to compute the product. ').lower() 

    total = 1 if operation == 'p' else 0

    for num in range(1, int(target) + 1):
        if operation == 's':
            total += num
        else:
            total *= num


    print(f"The {'sum' if operation == 's' else 'product'} of the integers between 1 and {target} is {total}") 

def short_long_short(str1, str2):
    return str2 + str1 + str2 if len(str1) > len(str2) else str1 + str2 + str1


def is_leap_year(year):
    if year > 1751:
      if year % 400 == 0:
          return True
      elif year % 100 == 0:
          return False

    return year % 4 == 0 
    

def multisum(target):
    total = 0

    for num in range(1, target + 1):
        if num % 3 == 0 or num % 5 == 0:
            total += num

    return total

def utf16_value(str_value):
    total = 0

    for char in str_value:
        total += ord(char)

    return total
