"""
  This module prepares words for wordle game.
"""

ALL_WORDS_FILE = "all_words.txt"
GAME_WORDS_FILE = "game_words.txt"


def read_words_from_file(filename):
    """
    This function reads a file and returns list of words present inside the file.

    :param filename: the name of the file to be read
    :return: list of found words
    """
    in_file = open(filename, "r")
    words_str = in_file.read()
    words = words_str.split()
    in_file.close()
    return words


def filter_words(words, min_length, max_length):
    result = []
    for item in words:
        if min_length <= len(item) <= max_length and item.isalpha():
            result.append(item)
    return result


def write_words_in_file(words, filename):
    """
    This function gets a list of strings (words) and writes each word at a line in th file.

    :param words: list of words that should be written in a file
    :param filename: the name of the file that words are going to be written inside of it
    """

    out_file = open(filename, "w")
    words_str = '\n'.join(words)
    out_file.write(words_str)
    out_file.close()


def main():
    words = read_words_from_file(ALL_WORDS_FILE)

    filtered_words = filter_words(words, 4, 6)

    write_words_in_file(filtered_words, GAME_WORDS_FILE)


if __name__ == "__main__":
    main()
