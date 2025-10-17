# Exercise 1

# reverse

# def reverse(num_list, size):
#     half_size = int(size / 2)
#     for i in range(half_size):
#         temp = num_list[i]
#         num_list[i] = num_list[size - i - 1]
#         num_list[size - i - 1] = temp
#     return num_list

# size = int(input("Enter the size of your list: "))
# num_list = []

# for i in range(size):
#     num_list.insert(i, int(input(f"Index {i}: ")))
 
# print("Normal: ", num_list)

# print("Reversed: ", reverse(num_list, size))


# Exercise 2

# max_num = int(input("Enter max number: "))
# num_list = []

# for i in range(1, max_num):
#     if i % 2 == 0:
#         num_list.append(i)

# print('Before: ',num_list)

# for i in range(len(num_list)):
#     num_list[i] = num_list[i] ** 2

# print('After: ',num_list) 


# Exercise 3

# def merge(list1, list2):
#     merge_list = list1 + list2
#     union_list = []
#     for i in range(int(len(merge_list))):
#         if merge_list[i] not in union_list:
#             union_list.append(merge_list[i])
#     return union_list

# def assign_item(size):
#     num_list = []
#     for i in range(size):
#         num_list.append(input(f'Enter element for index {i}: '))
#     return num_list

# list1_size = int(input('Enter the size of list 1: '))
# list2_size = int(input('Enter the size of list 2: '))

# list1 = assign_item(list1_size)
# list2 = assign_item(list2_size)

# print(list1, list2)

# print(merge(list1, list2))


# Exercise 4

# def get_min(tuple_num):
#     min = tuple_num[0]
#     for i in range(len(tuple_num)):
#         if tuple_num[i] < min:
#             min = tuple_num[i]
#     return min

# def get_max(tuple_num):
#     max = tuple_num[0]
#     for i in range(len(tuple_num)):
#         if tuple_num[i] > max:
#             max = tuple_num[i]
#     return max

# def min_max(tuple_num):
#     return (get_min(tuple_num), get_max(tuple_num))

# tuple_num = (8,7,6,5,4,3,2,1)

# print(min_max(tuple_num))    


# Exercise 5:

# GPS = (('Phnom Penh', 11.5564, 104.9282),
#         ('Siem Reap', 13.3622, 103.8597), 
#         ('Battambang', 13.0957, 103.2022))


# for slot in range(len(GPS)):
#     i = 0
#     print(f'City: {GPS[slot][i]}, Latitude: {GPS[slot][i + 1]}, Longitude: {GPS[slot][i + 2]}')


# Exercise 6:

dic = {1: 10, 2: 20, 3: 30, 4: 40}

squ = lambda x:x*2
dic ={k:squ(v) for k , v in dic.items()}
print("The lambda of dic is",dic)

