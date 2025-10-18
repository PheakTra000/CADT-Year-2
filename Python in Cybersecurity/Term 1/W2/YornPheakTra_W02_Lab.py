# Exercise 1
print('Exercise 1')
def reverse(num_list):
    size = len(num_list)
    half_size = int(size / 2)
    for i in range(half_size):
        temp = num_list[i]
        num_list[i] = num_list[size - i - 1]
        num_list[size - i - 1] = temp
    return num_list

num_list = [1,2,3,4,5]
print("Reversed: ", reverse(num_list))
print()

# Exercise 2
print('Exercise 2')
num_list = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(num_list)
print()

# Exercise 3
print('Exercise 3')
def merge(list1, list2):
    merge_list = list1 + list2
    union_list = []
    for i in range(int(len(merge_list))):
        if merge_list[i] not in union_list:
            union_list.append(merge_list[i])
    return union_list

list1 = [1,2,3]
list2 = [2,3,4,5]

print(merge(list1, list2))
print()


# Exercise 4
print('Exercise 4')
def get_min(tuple_num):
    min = tuple_num[0]
    for i in range(len(tuple_num)):
        if tuple_num[i] < min:
            min = tuple_num[i]
    return min

def get_max(tuple_num):
    max = tuple_num[0]
    for i in range(len(tuple_num)):
        if tuple_num[i] > max:
            max = tuple_num[i]
    return max

def min_max(tuple_num):
    return (get_min(tuple_num), get_max(tuple_num))

tuple_num = (10,5,8,12,3)

print(min_max(tuple_num))    
print()


# Exercise 5:
print('Exercise 5')
GPS = (('Phnom Penh', 11.5564, 104.9282),
        ('Siem Reap', 13.3622, 103.8597), 
        ('Battambang', 13.0957, 103.2022))


for slot in range(len(GPS)):
    i = 0
    print(f'City: {GPS[slot][i]}, Latitude: {GPS[slot][i + 1]}, Longitude: {GPS[slot][i + 2]}')
print()


# Exercise 6:
print('Exercise 6')
dicts = {1: 10, 2: 20, 3: 30, 4: 40}

value_list = list(dicts.values())
double_value = lambda x : x * 2

for i in range(len(value_list)):
    dicts.update({i + 1 : double_value(value_list[i])})

print(dicts)
print()


# Exercise 7
print('Exercise 7')
def frequency(string):
    char_list = []
    for i in range(len(string)):
        char_list.append(string[i])

    dicts = {}
    for i in char_list:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    return dicts

string = 'hello'
print(frequency(string))
print()


# Exercise 8
print('Exercise 8')
def merge_dicts(dicts_1, dicts_2):
    new_dicts = {}
    new_dicts.update(dicts_1)
    new_dicts.update(dicts_2)
    
    common = dicts_1.keys() & dicts_2.keys()

    if len(common) > 0:
        for i in common:
            new_dicts[i] = dicts_1[i] + dicts_2[i]

    return new_dicts

dicts_1 = {'a': 1, 'b': 2}
dicts_2 = {'b': 3, 'c': 4}

print(merge_dicts(dicts_1, dicts_2))
print()


#bonus 
'''
                                Data Management
'''
print('Bonus')
def add_user(users, username, email, status):
    duplicate = False
    for i in range(len(users)):
        if username == users[i]['username']:
            duplicate = True

    if not duplicate: users.append({"username": username, "email": email, "status": status})
    else: print('This username is already taken. Please use different username')

def remove_user(users, username):
    for i in range(len(users)):
        if username == users[i]['username']:
            del users[i]
            break
        
def update_user_status(users, username, new_status):
    for i in range(len(users)):
        if username == users[i]['username']:
            users[i]['status'] = new_status

def display_users(users):
    for i in range(len(users)):
        print(users[i])

def count_active_users(users):
    count = 0
    for i in range(len(users)):
        if 'active' == users[i]['status']:
            count += 1
    print(count)

users = [
{"username": "alice", "email": "alice@example.com", "status": "active"},
{"username": "bob", "email": "bob@example.com", "status": "suspended"},
{"username": "charlie", "email": "charlie@example.com", "status": "active"}
]

display_users(users)
print()
add_user(users, 'tra', 'tra@gmail.com', 'active')
remove_user(users, 'bob')
add_user(users, 'tra', 'tra@gmail.com', 'active') # handle duplicate
update_user_status(users, 'charlie', 'suspended')
display_users(users)