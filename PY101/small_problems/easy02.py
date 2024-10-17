import random


def greetings(name=[], attrs={}):
    fullname = ' '.join(name)
    print(f"Nice to meet you {fullname}. Great to have a {attrs['title']} {attrs['occupation']} around.")

def greet_user():
    print("What's your name? ")
    name = input()
   
    return f"HELLO {name.upper()}! WHY ARE WE YELLING?"  if name.endswith('!') else f"Hello {name.title()}."
    

def oddities(nums):
    return [x for index, x in enumerate(nums) if index % 2 == 0]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

def teddys_age():
    age = random.randint(20, 100)
    return f"Teddy's age is {age}!"


def center_of(str):
    isOdd = len(str) % 2 == 0

    if isOdd:
        return str[len(str) // 2 - 1: (len(str) // 2) + 1]
    else:
        return str[len(str) // 2: (len(str) // 2) + 1]
    
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

def negative(num):
    # if num < 1:
    #     return num
    # else:
    #     return int('-' + str(num))
    return - abs(num)
    
# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# result1 = append_to_list(10)
# result2 = append_to_list(20)
# print(result1)
# print(result2)


def double(num):
    global int_val
    int_val *= 2

int_val = 2
double(int_val)

print(int_val)  # outputs: 2
