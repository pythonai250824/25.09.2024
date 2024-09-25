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

# input names from the user and append to the list
# if a name was entered twice then continue
# if the given name was 'exit' then ==> break







