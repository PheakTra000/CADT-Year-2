import random

def is_too_short(pswd):  # worked
    return len(pswd) < 8

def has_upper_case(pswd): # worked
    for i in range(len(pswd)):
        if pswd[i].isalpha():
            if pswd[i] == pswd[i].upper(): return True
    return False

def has_digit(pswd): # worked
    for i in range(len(pswd)):
        if pswd[i] in {'1','2','3','4','5','6','7','8','9','0'}: return True
    return False

def has_special(pswd): # worked 
    for i in range(len(pswd)):
        if pswd[i] in {'!','@','#','$','%','^','&','*','(',')'}: return True
    return False

def ultimate_password(pswd):
    if is_too_short(pswd):
        print('Password too short. Must be at least 8 characters.')
    elif not has_upper_case(pswd):
        print('Password must contain at least one uppercase letter.')
    elif not has_digit(pswd):
        print('Password must contain at least one digit.')
    elif not has_special(pswd):
        print('Password must contain at least one special character.')
    else:
        return True

def get_passkey():
    return random.randrange(10000000, 99999999)


def menu():
    print('--------------------------------------------------')
    print('Default Menu:\n')
    print('1. Register')
    print('2. Login')
    print('3. Forgot Password')
    print('4. Exit')
    print('--------------------------------------------------')

def user_menu():
    print('--------------------------------------------------')
    print('User Menu:\n')
    print('1. Show detail')
    print('2. Exit')
    print('--------------------------------------------------')

def forget_password_choice():
    print('--------------------------------------------------')
    print('Forget password:\n')
    print('1. using passkey')
    print('2. using email')
    print('3. exit')
    print('--------------------------------------------------')

