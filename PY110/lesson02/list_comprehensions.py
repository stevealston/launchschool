import random
# List comprehensions
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Computer the total age of family male members in a loop and in a list comprehension
totalAge = 0

for _, info in munsters.items():
    if info['gender'] == 'male':
        totalAge += info['age']

# print(totalAge)

# print(sum([info['age'] for _, info in munsters.items()
#               if info['gender'] == 'male']))

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
new_lst = [sorted(item) for item in lst]
# print(new_lst)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
new_lst = [sorted(item, key=str) for item in lst]
# print(new_lst)

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {item[0]: item[1] for item in lst}
# print(new_dict)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# sort the lists based on the sum of odd nums the contain
result = []
for sublist in lst:
    total = 0
    for num in sublist:
        if num % 2 != 0:
            total += num
    result.append(total)

def sum_of_odds(sublist):
    odds = [num for num in sublist if num % 2 != 0]
    return sum(odds)

# print(sorted(lst, key=sum_of_odds))

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

new_list = [increment_values(value) for value in lst]

# print(new_list, lst, sep='\n')

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def multiples(sublist):
    return [num for num in sublist if num % 3 == 0]

# print([multiples(sublist) for sublist in lst])

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(dictionary):
  
    if dictionary['type'] == 'fruit':
        return [color.capitalize() for color in dictionary['colors']]
    else:
        return dictionary['size'].upper()

# print([transform_item(item) for item in dict1.values()])

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

"""
PROBLEM: 
  - include dictionary in output only if all list values contain only even numbers
EXAMPLES
  - output[{e: [8], f: [6, 10]}]
DATA:
  INPUT(s): { [key: string]: int[] }[]
  OUTPUT: { [key: string]: int[] }[]
ALGORITHM:
  check all evens 
  
"""
def extract_evens(dictionary):
    if all(all(elem % 2 == 0 for elem in lst) for lst in dictionary.values()):
        return dictionary
    return None
              
              

filtered_list = [d for d in (extract_evens(dictionary) for dictionary in lst) if d]

# print(filtered_list)

# UUID
def generate_uuid():
    uuid_chars = 'abcdef0123456789'

    eight = [random.choice(uuid_chars) for _ in range(0, 8)]
    four1 = [random.choice(uuid_chars) for _ in range(0, 4)]
    four2 = [random.choice(uuid_chars) for _ in range(0, 4)]
    four3 = [random.choice(uuid_chars) for _ in range(0, 4)]
    twelve = [random.choice(uuid_chars) for _ in range(0, 12)]

    uuid = eight + ['-'] + four1 + ['-'] + four2 + ['-']  + four3 + ['-']  + twelve

    return ''.join(uuid)

def ls_generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)
    
# print(generate_uuid())

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here
vowels = 'aeiou'

list_of_vowels = [char for lst in dict1.values()
                        for word in lst
                        for char in word if char in vowels]

# print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
todo_lists = [
    {
        "id": 1,
        "list_name": 'Groceries',
        "todos": [
            {"id": 1, "name": 'Bread', "completed": False},
            {"id": 2, "name": 'Milk', "completed": False},
            {"id": 3, "name": 'Apple Juice', "completed": False}
        ]
    }
]

todo_lists[0]["todos"][2].update({"name": 'Orange Juice'})

print(todo_lists)

lst = [1, 0, 1, 0, 1, 0, 0]

def iteration_performed(item):
    return f"iteration {item}"

print([iteration_performed(item) for item in lst if lst.pop(0)])