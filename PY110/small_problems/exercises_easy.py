def searching_101():
    first = input('Enter the 1st number: ')
    second = input('Enter the 2nd number: ')
    third = input('Enter the 3rd number: ')
    fourth = input('Enter the 4th number: ')
    fifth = input('Enter the 5th number: ')
    sixth = input('Enter the 6th number: ')

    numbers = [first, second, third, fourth, fifth]

    return f"{sixth} is in {', '.join(numbers)}" if sixth in numbers else f"{sixth} isn't in {', '.join(numbers)}"

# print(searching_101())

"""
PROBLEM: 
  Explicit:
    - string read the same forwards and backwards
  Implicit:
    - if length is odd don't worry about middle letter
EXAMPLES:
  print(is_palindrome('madam') == True)
  print(is_palindrome('356653') == True)
  print(is_palindrome('356635') == False)

  # case matters
  print(is_palindrome('Madam') == False)

  # all characters matter
  print(is_palindrome("madam i'm adam") == False)

DATA:
  Input(s): str
  Output: bool
ALGORITHM:
  find midpoint of string
  get first half of string
  get second half of string
  return first == second
"""
def is_palindrome(string):
    mid = len(string) // 2
    first = string[:mid]
    second = string[-1:(mid - 1):-1] if len(string) % 2 == 0 else string[-1:mid:-1]

    return first == second

def ls_is_palindrome(s):
    return s == s[::-1]

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)
# print(is_palindrome('Madam') == False)
# all characters matter
# print(is_palindrome("madam i'm adam") == False)


def is_real_palindrome(s):
    result = ''
    for char in s:
        if char.isalnum() and char.isascii():
            result += char

    return result.casefold() == result[::-1].casefold()

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

def running_total(numbers):
    sum = 0
    result = []

    for num in numbers:
        sum += num
        result.append(sum)
    
    return result

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

def word_sizes(s):
    clean_str = ''

    for char in s:
        if char == ' ' or char.isalpha():
            clean_str += char

    split = clean_str.split(' ')
    sizes = {}

    if not s:
        return sizes
    
    for word in split:
        sizes[len(word)] = sizes.get(len(word), 0) + 1
    
    return sizes

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

def swap(s):
    if not s or len(s) < 2:
        return s
    
    split_str = s.split(' ')
    result = []

    for word in split_str:
        first, last = word[0], word[-1]

        if len(word) < 2:
            result.append(word)
        else:
            result.append(last + word[1:len(word) - 1] + first)

    return ' '.join(result)

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

DIGITS = {
    0: '0',
    1: '1', 
    2: '2', 
    3: '3', 
    4: '4', 
    5: '5', 
    6: '6', 
    7: '7', 
    8: '8', 
    9: '9', 
}
def str_to_int(s):
    result = 0

    for idx, char in enumerate(s[::-1]):
         result += (DIGITS[char] * (10 ** idx))

    return result

# print(str_to_int("4321") == 4321)  # True
# print(str_to_int("570") == 570)    # True

def string_to_signed_integer(s):
    is_negative = False

    if s.startswith('-'):
        is_negative = True
        s = s.replace('-', '')
    elif s.startswith('+'):
        s = s.replace('+', '')

        
        
    result = str_to_int(s)

    if is_negative:
        result *= -1
    
    return result

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

"""
x = 109
"""
def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True


def signed_integer_to_string(integer):
    if integer > 0:
        return f"+{integer_to_string(integer)}"
    elif integer < 0:
        integer = integer * -1
        return f"-{integer_to_string(integer)}"
    else:
        return integer_to_string(integer)
    
# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True