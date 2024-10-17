from loan_msgs import msgs

def prompt(msg):
    print(f"==> {msg}")

def invalid_number(num):
    try:
        float(num)
    except ValueError:
        return True
    
    return False

def calculate_payment(amt, apr, dur):
    try:
        rate = apr / 12
        dur = float(dur)
        payment = float(amt) * (rate / (1 - (1 + rate) ** (-dur)))

        return rate, payment
    except ValueError:
        pass

def calculate_apr(apr):
    if '%' in apr:
        return float(apr.split('%')[0]) / 100 

    if '.' in str(apr):
        print(apr.split('.'))
        if apr.split('.')[0]:
            return float(apr) / 100
    
    if apr.isdigit():
        return float(apr) / 100
    
    return apr

print("========LOAN CALCULATOR========\n")
prompt(msgs['loan_amt'])
amt = input()

while invalid_number(amt):
    prompt(msgs['invalid_number'])
    amt = input()

prompt(msgs['loan_apr'])
apr = input()

while invalid_number(apr):
    prompt (msgs['invalid_number'])
    apr = input()

apr = float(calculate_apr(apr))

prompt(msgs['loan_dur'])
dur = input()

while invalid_number(dur):
    prompt (msgs['invalid_number'])
    dur = input()

_, payment = calculate_payment(amt, apr, dur)

print(f"Your monthly payment is: ${payment:.2f}")
