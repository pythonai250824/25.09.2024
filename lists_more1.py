# []
# append
# insert
# len
# min max mean
# pop

# sum, remove, del, for-each, extend, comprehension, any, all

# sum the numbers between 1-50
numbers: list[int] = []
for i in range(1, 50 + 1):
    numbers.append(i)
# dont use sum as a variable
sum_list: int = sum(numbers)
avg_list: float = sum(numbers) / len(numbers)  # better mean
print('sum_list', sum_list)
print('avg_list', avg_list)

list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
print('list1[1, 2, 3] + [4, 5, 6] =', list1 + [4, 5, 6])
list1.extend(list2)  # concat
print(list1.extend([7, 8, 9]))  # None
print('after extend:', list1)

# x: int = 1
# y: int = 2
# 1 not change: x + y got feedback
# 2 change: list1.extend([4,5,6]) not got feedback , changed
# 3 len:  len(list1) feedback, not changed
# not changed, not feedback

# pop
print(list1)
print('pop -- ', list1.pop())
last_item: int = list1.pop()
item_index_2: int = list1.pop(2)
print('list1 after pop last , pop index 2: ', list1)

# remove without getting the item
# option to remove specific indexes + jump
del list1[0]
del list1[1: 3: 2]
print('after del list1[0],del list1[1: 3: 2]', list1)

# how to check if 99 is in list
list1 = [10, 20, 30, 99, 101]
print(list1)
is_99_in_list: bool = False
for number in list1:
    if number == 99:
        is_99_in_list = True
        break
print("[loop] 99 in list?", is_99_in_list)
print("[cond] 99 in list?", 99 in list1)
# >>> 'a' in 'halo'
# True
# >>> 'ab' in 'abab'
# True
# >>> 'banana' in ['apple', 'banana']
# True
# >>> 1.5 in [1, 2, 1.5]
# True
# >>> 1.5 in [1, 2, 1.51]
# False
# >>> 1.5000 in [1, 2, 1.5]
# True
# >>> [1,2] in [ [1,2], [3,4] ]

# remove the number 99 from the list
list1 = [10, 20, 30, 99, 101]
print(list1)
list1.remove(99)
print('after list1.remove(99)', list1)

# remove all 99
list1 = [10, 20, 30, 99, 101, 99, 20, -1, 99]
print(list1)
while 99 in list1:
    list1.remove(99)
print('after list1.remove all', list1)

# input names from the user and append to a list
# if the name already exist in the list then do NOT append (continue)
# if the given name was 'exit' then ==> break
list_names = []
while True:
    name: str = input('whats your name?')
    if name == 'exit':
        break
    if name in list_names:
        print(f"we already have a {name}")
        continue
    list_names.append(name)
print(list_names)

# clear
list1.clear()  # clears the specific list
list1 = []   # creates a new empty list
print('after clear', list1)

# index
list1 = [1, 20, 30, 99, -1]
if 99 in list1:
    #                                        0   1   2   3   4
    print('[1, 20, 30, 99, -1].index(99):', [1, 20, 30, 99, -1].index(99))
    print('[1, 20, 30, 99, -1].index(99):', list1.index(99))

# count
print('[1, 20, 30, 99, -1,99].count(99):', [1, 20, 30, 99, -1, 99].count(99))

# copy
"""
>>> l1 = [1,2,3]
>>> save_list = l1  # did NOT really save the original
>>> l1.extend([4,5,6])
>>> save_list
[1, 2, 3, 4, 5, 6]     # save_list is the same as l1, alias

>>> l1 = [1,2,3]
>>> save_list = l1.copy()     # save_list is a new independent list
>>> l1.extend([4,5,6])
>>> l1
[1, 2, 3, 4, 5, 6]
>>> save_list
[1, 2, 3]

>>> x = 1
>>> y = x  # copy a new value 
>>> x += 1
>>> x
2
>>> y
1
"""

list1 = [1, 5, -2, 100, -30, 11, 0]
print('before sort', list1)
save_list1 = list1.copy()
list1.sort()
print('after sort', list1)
print('after sort, save list1', save_list1)
# sort reverse
list1.sort(reverse=True) # sort from big to small, in reverse order
print('list1.sort(reverse=True)', list1)

#        d        m        z       a
list1= ['danny', 'moshe', 'zina', 'avi']
print(list1)
list1.sort()
print('list1.sort() by abc', list1)


