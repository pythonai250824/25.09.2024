
import random
import statistics

# for-each

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

# print each letter in a word
print(f"for-each letter in 'Hello' --> ", end="")
for letter in "Hello":  # str ['H', 'e', 'l', 'l', 'o']
    print(letter, end="  ")
print()

# create a list of 20 random numbers between -50 and +50
# print the list
# print all positive numbers using for-each
random_list: list[int] = []
for _ in range(20):
    random_number: int = random.randint(-50, +50)
    random_list.append(random_number)

print(random_list)

print(f"for-each positive numbers: ", end="")
for number in random_list:
    if number > 0:
        print(number, end =" ")
print()

# input str from the user i.e. chocolate
# input a letter str i.e. c
# count how many times the letter appears in the word?
word: str = input('enter a word: ')
char: str = input('enter a character: ')
char_counter: int = 0
for letter in word:
    if letter == char:
        char_counter += 1
print(f"in '{word}' the character '{char}' repeats {char_counter} times.")
