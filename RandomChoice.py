
# open new_file
# read new_file
# extract the words from new_file
# create a list
# save each word from new_file into that list
# choose a random word
# show the length of the chosen word
#close new_file

from word_preprocessing import read_words
from word_preprocessing import filtered_words
from word_preprocessing import combined_file


import random
# new_file = open('new_file.txt', "r")
# file_contents = new_file.read()
# random_lst = file_contents.split()
word_lst = read_words('new_file.txt')
selected_word = random.choice(word_lst)
print(selected_word)
print(len(selected_word))

print('The word has', len(selected_word), 'letters')
guess = input("Please enter your word guess: ")


while len(guess) != len(selected_word):
    print('Try again, wrong length')
    guess = input("Please enter your word guess: ")

# while guess not in word_lst:
#     print('Try again, not an actual word')
#     guess = input("Please enter your word guess: ")

from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# while guess in word_lst:
#     if letter in
#     print(Back.GREEN + 'and with a green background')
#
# while guess not in word_lst:
#     print(Fore.RED + 'some red text')
#
# correct_letters = []
# wrong_letters = []
# for letter in guess:
#     if letter in guess and letter in selected_word:
#         print(Back.GREEN + letter + Style.RESET_ALL, end=' ')
#         correct_letters.append(letter)
#     else:
#         print(Fore.RED + letter + Style.RESET_ALL, end=' ')
#         wrong_letters.append(letter)
#
# print("Correct Letters", correct_letters)
# print("Wrong Letters", wrong_letters)

# If the position of the letter in guess == the position of the letter in selected word then it is a match
# if the position of the letter in guess is not equal to the position of the letter in selected word, then it is not a match

# print the correct letters in green using the imported functions
# print the wrong letters with no style


for i in range(len(guess)):
    letter = guess[i]
    if guess[i] == selected_word[i]:
        print(Back.GREEN + letter + Style.RESET_ALL, end=' ')
    else:
        print(Fore.RED + letter + Style.RESET_ALL, end=' ')



# selected word = help
# guess = hope   + - % %
# + is when the guess letter is in the same position as the selected word
# - is when the guess letter is not present at all in the selected word
# % is when the guess letter is present but in the wrong position as the selected word letter
# if you match the letter in selected word, that is no longer enabled to be matched with
# the matched letters in selected words are removed from the pool of allowable items to be matched
# selected_words

# selected word = private
# guess = approve
# output = % % - % - % +

# Subtract 123 from the value
# my_dict['key1'] = my_dict['key1']
# my_dict['key1'] -= 123
#
# word_dict = {}

def get_letters_count(word):
    word_dict = {}
    for letter in word:
        word_dict['letter'] = 1
    return word_dict

print(get_letters_count('apple'))

# apple
# {'a': 1, 'p': 2, 'l': 1, 'e': 1 }













