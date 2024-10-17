import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number):
    try:
        int(number)
    except ValueError:
        return True

    return False

def translate(key, lang='en'):
    return messages.get(lang, {}).get(key, key)

with open("msgs.json", "r") as f:
    messages = json.load(f)

print("Language: (en) English, (es) Español, (fr) Français")
language = input().lower()

while language not in ['en', 'es', 'fr']:
    prompt('options: en, es, fr')
    language.input().lower()

prompt(translate('welcome', language))

while True:
  # ask user for first number
  prompt(translate('num1', language))
  number1 = input()

  while invalid_number(number1):
      prompt(translate('invalid', language))
      number1 = int(input())

  # ask user for second number
  prompt(translate('num2', language))
  number2 = input()

  while invalid_number(number2):
      prompt(translate('invalid', language))
      number2 = int(input())

  # get the operation
  prompt(translate('calc', language))

  operation = input()

  while operation not in ["1", "2", "3", "4"]:
      prompt('You must choose 1, 2, 3, or 4')
      operation = input()

  match operation:
      case '1':   # '1' represents addition
          output = int(number1) + int(number2)
      case '2': # '2' represents subtraction
          output = int(number1) - int(number2)
      case '3': # '3' represents multiplication
          output = int(number1) * int(number2)
      case '4': # '4' represents division
          output = int(number1) / int(number2)

  print(f"The result is: {output}")
  prompt(translate('again', language))
  another_calculation = input().lower()

  if not another_calculation.startswith('y'):
      break
      
