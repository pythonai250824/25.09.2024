# []
# append
# insert
# len
# min max mean
# pop
import statistics

# sum, for-each, remove, del, for-each, extend, comprehension, any, all

# sum the numbers between 1-50
numbers: list[int] = []
for i in range(1, 50 + 1):
    numbers.append(i)
# dont use sum as a variable
sum_list: int = sum(numbers)
avg_list: float = sum(numbers) / len(numbers)  # better mean
print('sum_list', sum_list)
print('avg_list', avg_list)

# print every height above avg
height_list: list[float] = [1.90, 2.25, 2.1, 1.8, 1.55, 1.99, 2.3]
print('height_list', height_list)
avg_heights: float = statistics.mean(height_list)
print(f"for-i    above avg[{avg_heights:.2f}]: ", end="")
#                                      0     1    2    3     4     5    6
for i in range(len(height_list)): # [1.9, 2.25, 2.1, 1.8, 1.55, 1.99, 2.3]
    height: float = height_list[i]
    if height > avg_heights:
        print(f"{height}", end=" ")
print()
print(f"for-each above avg[{avg_heights:.2f}]: ", end="")
for height in height_list:  # [1.9, 2.25, 2.1, 1.8, 1.55, 1.99, 2.3]
    if height > avg_heights:
        print(f"{height}", end=" ")
print()
print(f"for-each letter in 'Hello' --> ", end="")
for letter in "Hello":  # str ['H', 'e', 'l', 'l', 'o']
    print(letter, end="  ")
print()

# create a list of 20 random numbers between -50 and +50
# print the list
# print all positive numbers using for-each
# input str from the user i.e. chocolate
# input a letter str i.e. c
# count how many times the letter appears in the word?

