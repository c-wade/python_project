"""
File: boggle.py
Name:
----------------------------------------
test input:
f y c l
i o m g
o r i l
h j h u
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROWS = 4
COLS = 4
ANS_LEN = 4
dictionary = []
boggle_letters = []


def main():
    read_dictionary(FILE)
    complete = set_boggle_letters()
    if not complete:
        return
    start = time.time()
    ####################
    ans_list = find_words()
    ####################
    end = time.time()
    print(f'There are {len(ans_list)} words in total')
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words() -> list[str]:
    """
    Find words from Boggle letters if the words are in the dictionary
    :return: The words we found in Boggle letters
    """
    ans_list = []
    for row in range(len(boggle_letters)):
        for col in range(len(boggle_letters[row])):
            find_words_helper(ans_list, boggle_letters[row][col], row, col, row, col, dictionary)
    return ans_list


def find_words_helper(ans_list, current_str, cur_x, cur_y, prev_x, prev_y, cached_words):
    """
    A recursive helper to go through all letters in boggle and find words that are in the dictionary (DFS)
    :param ans_list: list[str]: The list of words that we found
    :param current_str: str: The prefix of words that we should find
    :param cur_x: int: The row index of the current_str
    :param cur_y: The column index of the current_str
    :param prev_x: The row index of the previous letter
    :param prev_y: The column index of the previous letter
    :param cached_words: The list that contains all the words
    """
    for x in range(-1, 2):
        new_x = cur_x + x
        # prevent index out of range
        if new_x < 0 or new_x >= ROWS:
            continue
        for y in range(-1, 2):
            new_y = cur_y + y
            # prevent index out of range, avoid stepping back, avoid using same letter
            if new_y < 0 or new_y >= COLS or (new_x == prev_x and new_y == prev_y) or (x == 0 and y == 0):
                continue
            new_str = current_str + boggle_letters[new_x][new_y]
            new_cache = get_new_cache(new_str, cached_words)
            if len(new_cache) > 0:
                if len(new_str) >= ANS_LEN and new_str not in ans_list and new_str in cached_words:
                    ans_list.append(new_str)
                    print(f'Found "{new_str}"')
                find_words_helper(ans_list, new_str, new_x, new_y, cur_x, cur_y, new_cache)


def get_new_cache(sub_s: str, cache: list[str]) -> list[str]:
    """
    Get all words in the dictionary that start with prefix
    :param sub_s: str: Prefix of the word
    :param cache: list[str]: The list of words in dictionary
    :return: list[str]: The words that start with prefix
    """
    lst = []
    for word in cache:
        if word.startswith(sub_s):
            lst.append(word)
    return lst


def read_dictionary(file):
    """
    Read the file and save data into the dictionary
    """
    with open(file, 'r') as f:
        for line in f:
            dictionary.append(line.strip())


def set_boggle_letters() -> bool:
    """
    Input boggle letters
    :return: bool: True if boggle letters are complete, False if boggle letters are not complete .
    """
    row_count = 0
    while row_count < ROWS:
        row_count += 1
        letters = input(f'{row_count} of letters: ').lower().strip().split(' ')
        if check_input(letters):
            boggle_letters.append(letters)
        else:
            print('Invalid input!')
            return False
    return True


def check_input(letters: list[str]) -> bool:
    """
    Check user input.
    :param letters: list[str]: A list contains of four English characters
    :return: bool: True if input is legal, False if input is illegal
    """
    if len(letters) != COLS:
        return False
    for letter in letters:
        if not letter.isalpha() or len(letter) > 1:
            return False
    return True


if __name__ == '__main__':
    main()


# def find_words_helper(ans_list, current_str, row_num, col_num, prev_x, prev_y, cached_prefix_index):
#     for x in range(-1, 2, 1):
#         row = row_num + x
#         # out of range
#         if row < 0 or row >= ROWS:
#             continue
#         for y in range(-1, 2, 1):
#             col = col_num + y
#             # out of range
#             if col < 0 or col >= COLS or (row == prev_x and col == prev_y) or (x == 0 and y == 0):
#                 continue
#             new_str = current_str + boggle_letters[row][col]
#             cached_prefix_index.append(get_prefix_index(new_str, cached_prefix_index[-1]))
#             if cached_prefix_index[-1] >= 0:
#                 if len(new_str) >= ANS_LEN and new_str in dictionary and new_str not in ans_list:
#                     ans_list.append(new_str)
#                     print(f'Found {new_str}')
#                 find_words_helper(ans_list, new_str, row, col, row_num, col_num, cached_prefix_index)
#             cached_prefix_index.pop()
#
#
# def get_prefix_index(sub_s, cached_index):
#     if cached_index > 0:
#         for word in dictionary[cached_index:]:
#             if word.startswith(sub_s):
#                 return dictionary.index(word)
#             if not word.startswith(sub_s[0:-1]):
#                 return -1
#     else:
#         for word in dictionary[cached_index:]:
#             if word.startswith(sub_s):
#                 return dictionary.index(word)
#     return -1
