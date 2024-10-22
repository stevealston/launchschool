"""
PROBLEM: 
  Explicit:
    - argument represents an angle
    - 60 minutes in a degree
    - 60 seconds in a minute
    - Input(s): float
    - output str representing "degrees°minutes'seconds"
  Implicit:
    - take the numbers after the decimal point and divide 60 by that value
      -(eg 60 * .78 = 43.8 take the .8 from 43 and divide 60 by .8)
EXAMPLES:
  # All of these examples should print True
  print(dms(30) == "30°00'00\"")
  print(dms(76.73) == "76°43'48\"")
  print(dms(254.6) == "254°35'59\"")
  print(dms(93.034773) == "93°02'05\"")
  print(dms(0) == "0°00'00\"")
  print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

DATA:
  list
ALGORITHM:


CODE:
"""
import math

DEGREE = "\u00B0"

def dms(num):
    if isinstance(num, int):
        return f"{str(num) + DEGREE}00'00\""
   
    split_num = str(num).split(".")
    degree = math.floor(num)
    minutes = 60 * (int(split_num[1]) / 100)
    minutes, seconds = f"{minutes:.2f}".split('.')
    seconds = math.floor(60 * (int(seconds) / 100))

    return f"{str(degree) + DEGREE}{minutes}'{seconds}\""

# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

def union(list1, list2):
    return { item for item in (list1 + list2) }

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

def halvsies(lst):
    if len(lst) == 1:
        return [lst, []]
    
    mid = math.ceil(len(lst) / 2)
    # mid = (len(lst) + 1) // 2

    return [lst[:mid], lst[mid:]]

# All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

def find_dup(lst):
    dup_map = {}

    for item in lst:
        value = dup_map.get(item, 0)
        dup_map[item] = value + 1
        if dup_map[item] == 2:
            return item

def find_dup_ls1(lst):
    dups = [element for element in lst if lst.count(element) == 2]
    return dups[0]

def find_dup_ls2(lst):
    seen = set()

    for element in lst:
        if element in seen:
            return element

        seen.add(element)

"""
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
"""

def interleave(list1, list2):
    result = []

    for i, val in enumerate(list1):
        result.append(val)
        result.append(list2[i])
    
    return result

def interleave_ls(list1, list2):
    new_list = []
    for idx in range(len(list1)):
        new_list.extend([list1[idx], list2[idx]])

    return new_list

def interleave_zip(list1, list2):
    result = []

    for item1, item2 in zip(list1, list2):
        result.extend([item1, item2])
    
    return result

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave_zip(list1, list2) == expected)      # True
from functools import reduce

def multiplicative_average(lst):
    average = round(reduce(lambda x, y: x * y, lst) / len(lst), 3)
    return f"{average:.3f}"

# All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

def multiply_list(list1, list2):
    result = []
    for idx, val in enumerate(list1):
        result.append(val * list2[idx])
    
    return result

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

def digit_list(num):
    return [int(digit) for digit in list(str(num))]

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        value = occurrences.get(item, 0)
        occurrences[item] = value + 1
    
    for key, value in occurrences.items():
        print(f"{key} => {value}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

def average(lst):
    return math.floor(reduce(lambda x, y: x + y, lst) / len(lst))

# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True