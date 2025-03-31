
def read_words(filename):
    my_file = open(filename, "r") #1 if you want to change input file
    words = my_file.read() #1
    word_lst = words.split() #1
    my_file.close() #1
    return word_lst

def filtered_words(word_lst):
    new_lst = [] #2
    for item in word_lst: #2
        if len(item) >= 4 and len(item) <= 6 and item.isalpha(): #2 #if you want to change the range of the word length
            new_lst.append(item) #2
    return new_lst #2

def combined_file(new_lst):
    new_file = open("new_file.txt", "w") #3 Change here if you want to change the output file
    combined_lst = '\n'.join(new_lst) #3
    new_file.write(combined_lst) #3
    new_file.close() #3


def main():
# Create a list of words from word.txt
#     my_file = open("worddle.txt", "r") #1 if you want to change input file
#     words = my_file.read() #1
#     word_lst = words.split() #1
#     my_file.close() #1
    word_lst = read_words('worddle.txt')

#     if each item of the word_lst has 4,5 or 6 length then save to new list
#
# Create a new list of 4,5 and 6 length words from the list you created in part 1
#     new_lst = [] #2
#     for item in word_lst: #2
#         if len(item) >= 4 and len(item) <= 6 and item.isalpha(): #2 #if you want to change the range of the word length
#             new_lst.append(item) #2
#     print(new_lst) #2

    filtered_lst = filtered_words(word_lst)


# Write contents from refined list into a new file called new_file.txt
#     new_file = open("new_file.txt", "w") #3 Change here if you want to change the output file
#     combined_lst = '\n'.join(new_lst) #3
#     new_file.write(combined_lst) #3
#     new_file.close() #3

    combined_file(filtered_lst)

if __name__ == "__main__":
    main()
    #what steps are present and what are missing in order to replicate the worddle app - what do we need to do next?