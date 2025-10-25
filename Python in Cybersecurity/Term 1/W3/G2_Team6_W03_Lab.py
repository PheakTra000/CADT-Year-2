# Exercise 1

print('Exercise 1')
numbers = [1,2,3,4,5]

for i in numbers:
    print(i)

i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

i = 1
while i <= 10:
    if i == 4:
        i += 1
        continue
    print(i)
    i += 1
print()

# Exercise 2
print('Exercise 2')

fruits = ['apple', 'banana', 'coconut']
print('List: ',fruits)

fruits.append('mango')
print('update list:', fruits)

fruits.remove('mango')
print('removed item list: ', fruits)

fruits.sort()
print('Sorted list base on alphabet: ', fruits)
print()


# exercise3
# 1
print('Exercise 3')

number = (1, 2, 3, 4, 5)
print(number)

#2
number = (1, 2, 3, 4, 5)
# number[0]=10
"""  """
# 3
number_tuple=(1, 2, 3, 4, 5)
number_list = list(number_tuple)
print(number_list)
print()


# # Exercise 4
print('Exercise 4')

dicts =  {"Alice": 30, "Bob": 25, "Charlie": 35}
print('dicts: ', dicts)

dicts['Tra'] = '18'
print('dicts updated: ', dicts)

dicts.pop('Bob')
print('dicts removed item: ', dicts)

for k, v in dicts.items():
    print(f'Key: {k} -> value: {v}')
print()


# Exercise 5
print('Exercise 5')

def add(num1, num2):
    return num1 + num2
print('total of sum: ', add(5, 2))

def greet():
    print("Hello, World!")
greet()

sqrt = lambda x : x ** 2
print(sqrt(5))
print()




#bonus
print('Bonus')

from function import * # use * to import all function

database = {}

def register():
    user_id = len(database) + 1

    # get email and password
    user_email = input('Please enter your email: ')
    email_password = input('Please enter your email password: ')

    # get username from database
    username_list = []
    for uid in database:
        username_list.append(database[uid]['username'])
   
    # apply and validate username 
    while True:
        username = input('Enter your username: ')
        if username not in username_list:
            break
        else:
            print('Username is already taken!')
        
    # apply and validate password
    while True:    
        user_password = input('Please enter your password: ')
        if ultimate_password(user_password):
            print('Registration successful with a strong password!')
            break
            
    # get pass key for account recovery 
    pass_key = get_passkey()
    print(f'Please save your passkey: [{pass_key}]')

    # apply user info to database
    database[user_id] = {
        'username': username,
        'user_password': user_password,
        'user_email': user_email,
        'email_password': email_password,   
        'pass_key': pass_key
    }

def login():
    attempt = 3
    while attempt > 0:
        username = input('Please enter your username: ')
        user_password = input('Please enter your password: ')
        attempt -= 1
        for uid in database:
            if username == database[uid]['username'] and user_password == database[uid]['user_password']:
                print(f'Login successful! Welcome, {database[uid]['username']}.')
                user_process(uid)
                return
        print(f'Invalid credentials. You have {attempt} attempts left.')

    print('Too many failed attempts. Access blocked.')
    return 'blocked'

def forget_password():

    while True:
        username = input('Enter your username: ')
        
        username_list = []
        for uid in database:
            username_list.append(database[uid]['username'])

        if username not in username_list:
            print('Username not found!')
            break
        else:      
            forget_password_choice()
            option = int(input('Enter your choice (1-3): '))
            match option:
                # case using passkey to recover the account
                case 1:
                    for uid in database:
                            pass_key = int(input('Enter your passkey to recover your account: '))

                            # if passkey is correct, it will let user to change their password
                            if pass_key == database[uid]['pass_key']:
                                while True:    
                                    new_password = input('Please enter your new password: ')
                                    if ultimate_password(new_password):
                                        print('You have successfully recovered your account!')
                                        break
                                database[uid]['user_password'] = new_password
                                break
                            else:
                                print('Incorrect passkey')
                    break
                
                # case using email to recover the account
                case 2:
                    for uid in database:
                            user_email = input('Please enter your email: ')
                            email_password = input('Please enter your email password: ')    

                            # if email and password is correct, it will also let user to change the password too
                            if user_email == database[uid]['user_email'] and email_password == database[uid]['email_password']:
                                while True:
                                    new_password = input('Please enter your new password: ')
                                    if ultimate_password(new_password):
                                        print('You have successfully recovered your account!')
                                        break
                                database[uid]['user_password'] = new_password
                                break
                            else:
                                print('Incorrect email or password!')
                    break

def user_process(user_id):
    while True:
        user_menu()
        option = int(input('Choose an option(1-2): '))
        match option:
            case 1:
                print('--------------------------------------------------')
                print('User detail:\n')
                print(f'User id: {user_id}')
                for key, value in database[user_id].items():
                    print(f'{key}: {value}')
                print('--------------------------------------------------')
            case 2:
                break

while True:
    menu()
    option = int(input('Choose an option(1-4): '))
    match option:
        case 1:
            register()
        case 2:
            status = login()
            if status == 'blocked':
                break
        case 3:
            forget_password()
        case 4:
            print('Exiting the program. Goodbye!')
            break
