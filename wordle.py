import random
from word_preprocessing import read_words_from_file, GAME_WORDS_FILE
from colorama import Fore, Back, Style

MAX_TRIES = 6


def get_user_guess(length):
    """
    This function reads a word from keyboard input and validates it to be
    alphabetic (no non-letter character) and have the same size as the length parameter
    it should keep asking until the user enters a valid guess.

    :param length: number of expected letter inside the gues
    :return: the lowercase valid input guess of the user
    """
    guess = input("Enter your guess: ")
    while len(guess) != length or not guess.isalpha():
        print('Incorrect length or characters. Please try again.')
        guess = input("Enter your guess: ")
    return guess.lower()


def get_feedback(selected_word: str, guess: str) -> list:
    """
    This function generates the feedback pattern of the guess against the selected word.
    The feedback is a python list which its values are as follows.
    All the correct letters in the correct positions are going to have green values
    All the remaining correct letters in incorrect positions are going to have yellow values
    The remaining indexes are going to have gray values
    :param selected_word: the word that should be used as the answer
    :param guess: the user guess that should be checked
    :return: a list of the feedback pattern
    """

    length = len(guess)
    feedback = ['GRAY'] * length
    letters_count = {}

    for letter in selected_word:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

    for i in range(length):
        letter = guess[i]
        if guess[i] == selected_word[i]:
            feedback[i] = "GREEN"
            letters_count[letter] -= 1

    for i in range(length):
        letter = guess[i]
        if feedback[i] == 'GRAY':
            if letter in letters_count and letters_count[letter] > 0:
                feedback[i] = "YELLOW"
                letters_count[letter] -= 1

    return feedback


def main():
    game_words = read_words_from_file(GAME_WORDS_FILE)
    selected_word = random.choice(game_words).lower()

    print(f"You should guess a word with {len(selected_word)} letters.")

    i = 0
    guess = ""
    while guess.lower() != selected_word and i < MAX_TRIES:
        guess = get_user_guess(len(selected_word))
        feedback_pattern = get_feedback(selected_word, guess)
        print(feedback_pattern)

        i += 1

    # while guess not in word_lst:
    #     print('Try again, not an actual word')
    #     guess = input("Please enter your word guess: ")

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

    # for i in range(len(guess)):
    #     letter = guess[i]
    #     if guess[i] == selected_word[i]:
    #         print(Back.GREEN + letter + Style.RESET_ALL, end=' ')
    #     else:
    #         print(Fore.RED + letter + Style.RESET_ALL, end=' ')

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

    # def get_letters_count(word):
    #     word_dict = {}
    #     for letter in word:
    #         word_dict['letter'] = 1
    #     return word_dict
    #
    # print(get_letters_count('apple'))

    # apple
    # {'a': 1, 'p': 2, 'l': 1, 'e': 1 }


if __name__ == "__main__":
    main()













