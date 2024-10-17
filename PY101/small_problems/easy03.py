def repeat(string, num):
    for _ in range(num):
        print(string)

# repeat('Hello', 3)

def crunch(string):
    n = len(string)
    if n < 2:
        return string
    
    i, j = 0, 1
    result = ''

    while i < n:
        while j < n and string[j] == string[i]:
            j += 1

        result += string[i]
        i = j
        j + 1

    return result  

# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')    
    
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

friends1 = ['Rachel', 'Phoebe', 'Joey', 'Monica', 'Ross', 'Chandler']
friends2 = friends1

friends1.reverse()

# print(friends2[0]) # ?

everest = "Everest"
kilimanjaro = "Kilimanjaro"
fuji = "Fuji"

mountain_list = [everest, kilimanjaro, fuji]

for idx in range(len(mountain_list)):
    mountain_list[idx] += " " + str(len(mountain_list[idx]))

mountain_list  # ['Everest 7', 'Kilimanjaro 11', 'Fuji 4']

# print(range(len(mountain_list)))

bar = 0
foo = []
baz = 3

try:
    qux = (bar or foo) and (baz / bar)
except ZeroDivisionError:
    qux = 0

if qux:
    print("Operation succeeded")
else:
    pass


greeting = "Hello"

people = { 1: "Ike", 2: "Jesse", 3: "Robin" }

def greet(item):
    greeting, name = item

    if name == 'Ike':
        print(f"{greeting}, {name}")
    elif name == 'Jesse':
        print(f"{greeting}, {name}")
    else:
        print(f"Hi, {name}")

# for p in people.items():
#     greet(p)

MONTHS = {
    1: 'JaNuArY',
    2: 'february',
    3: 'MaRch',
    4: 'ApriL',
    5: 'mAY',
    6: 'jUne',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'oCTOber',
    11: 'november',
    12: 'deCember'
}

month_names = MONTHS.values()

def cap_values(d):
    for key, value in d.items():
        d[key] = value.capitalize()

    return d

# capitalized_months = cap_values(MONTHS)
# print(list(month_names))
# print(month_names)
# print(MONTHS)
# ['January', 'February', 'March', 'April',
#   'May', 'June', 'July', 'August', 'September',
#   'October', 'November', 'December']

def mutating_delete(lst):
    return lst[:-1]

lst = [1, 2, 3]

# print(mutating_delete(lst) == [1, 2]) #=> True
# print(lst == [1, 2, 3]) #=> True

# num = 1

# def modify():
#     num += 1
#     print(num)

# modify()

a = 3

def foo():
    b = 2
    while a > b:
        c = 3
        b += 1

foo()

greeting = "Hello"

people = { 1: "Ike", 2: "Jesse", 3: "Robin" }

def greet(item):
    greeting, name = item

    if name == 'Ike':
        print(f"{greeting}, {name}")
    elif name == 'Jesse':
        print(f"{greeting}, {name}")
    else:
        print(f"Hi, {name}")

# for p in people.items():
#     greet(p)


def print_in_box(string):
    n = len(string)

    print(f"+-{'-' * n}-+")
    print(f"| {' ' * n} |")
    print(f"| {string} |")
    print(f"| {' ' * n} |")
    print(f"+-{'-' * n}-+")

# print_in_box('To boldly go where no one has gone before.')

def stringy(n):
    result = ''

    for idx in range(n):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result

# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

def triangle(steps):

    for i in range(steps):
        result = ''
        for j in range(i + 1, steps):
            result += ' ' 
        
        result += '*' * (i + 1)
        print(result)
    

# triangle(5)

def find_double(num):
    split = list(str(num))
    mid = len(split) // 2
    first_half = split[:mid]
    second_half = split[mid:]

    return first_half == second_half

def twice(num):
    return num if find_double(num) else num * 2

# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

def get_grade(*scores):
    sum = 0

    for grade in scores:
        sum += grade
    
    average = sum / 3

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

def clean_up(string):
    # replace non alpha chars with a single space
    result = ''

    for idx, char in enumerate(string):
        if char.isalpha():
            result += char
        elif idx == 0 or result[-1] != ' ':
            result += ' '

    return result      
        
    pass
        
print(clean_up("---what's my +*& line?") == " what s my line ")
# True