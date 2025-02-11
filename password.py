## at least on numeric value and has 5 charecter and captalize
'''while True: 
    password = input('Enter new password: ')
    if password.isalnum() and len(password)>5 : 
        break
    else: 
        print('Weak Password')
print('Strong Password')'''


### 
while True:

    result = []
    password = input('Enter new password: ')

    if len(password)>=8:
        result.append(True)


    digit = False
    for i in password: 
        if i.isdigit():
            digit = True

    result.append(digit)

    upperCase = False

    for i in password:
        if i.isupper(): 
            upperCase = True

    result.append(upperCase)

    if all(result): 
        print('Strong Password')
    else:
        print('Weak Password')


def strength(password):

    if len(password)>= 8: 
        result = []
        upper = False
        for c in password: 
            if c.isupper():
                upper = True
        result.append(upper)
        digit = False
        for c in password:
            if c.isdigit():
                digit = True
        result.append(digit)
        if all(result): 
            return 'Strong Password'
        else: 
            return 'Weak Password'
        
        
    else: 
        return 'weak password'
        
password = 'a2225678'
strength(password)

help(len)