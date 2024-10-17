# clear a list 2 ways

numbers = [1, 2, 3, 4]

def clear_numbers(nums):
    # nums = nums.copy()
    # return nums.clear()
    while numbers:
        numbers.pop()

def flintstones_rock():
    for i in range(1, 11):
        print(f"{'-' * i}The Flintstones Rock!")

def is_an_ip_number(num):
    try:
        num = int(num)
        return num >= 0 or num <= 255
    except ValueError:
        return False
    
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    n = len(dot_separated_words)

    if n != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def extend_greeting(greeting):
    greeting += " there"
    return greeting

greeting = "hi"
extend_greeting(greeting)

try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:   
    print(f"Result: {result}")
finally:    print("Exception handling complete.")