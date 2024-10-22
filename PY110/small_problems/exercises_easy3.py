"""
PROBLEM: 
  Explicit:
    - 24 hrs
    - 1440 minutes
    - 86400 seconds
    - Input(s): int is in minutes
  Implicit:
EXAMPLES:


DATA:
  Input(s):
  Output:
ALGORITHM:
    return if num == 0

    _, mins = divmod(num, 1440)
    

CODE:
"""

def time_of_day(minutes):
    _, minutes = divmod(minutes, (24 * 60))
    hrs, mns = divmod(minutes, 60)

    return f"{hrs:02d}:{mns:02d}"

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

def after_midnight(time):
    hrs, mins = time.split(':')

    return (int(hrs) % 24) * 60 + int(mins)

def before_midnight(time):
    hrs, mins = time.split(':')

    return (int(hrs) % 24) * 60 - (int(mins) % 60)

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

def repeater(string):
    result = ''

    for char in string:
        result += char * 2
    
    return result

def repeater_ls(string):
    return ''.join([char * 2 for char in string])

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

def double_consonants(string):
    result = ''

    for char in string:
        result += char * 2 if not char.lower() in 'aeiou' and char.isalpha() else char
    
    return result

# All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

def reverse_number(number):
    digits = list(str(number))[::-1]
    digits = ''.join(digits)

    return int(digits)

def reverse_number_ls(number):
    return int(str(number)[::-1])

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

def sequence(num):
    return [n for n in range(1, num + 1)]

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

def swap_name(name):
    first, last = name.split(' ')

    return f"{last}, {first}"

def swap_name_ls(name):
    return ', '.join(name.split()[::-1])

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

def sequence(count, step):
    result = []

    for idx, element in enumerate(range(count)):
        result.append(step * (idx + 1))

    return result

def sequence_ls(count, start_num):
    return [start_num * num for num in range(1, count + 1)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
      lst[end], lst[start] = lst[start], lst[end]
      
      start += 1
      end -= 1
    
    return lst

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

def is_balanced(string):
    total = 0

    for char in string:
        if char == '(':
            total += 1
        if char == ')':
            total -= 1
        if total < 0:
            return False

    return total == 0

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True