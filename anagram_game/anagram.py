"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
dictionary = []


def main():
    ####################
    read_dictionary(FILE)
    while 1:
        anagram = input('Find anagrams for: ').lower().strip()
        if anagram == '':
            print('Invalid input!')
            continue
        if anagram == EXIT:
            break
        anagrams_list = []
        print('Searching...')
        start = time.time()
        find_anagrams(anagram, '', len(anagram), anagrams_list, [0])
        print(f'{len(anagrams_list)} anagrams: {anagrams_list}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    ####################


def read_dictionary(file):
    """
    Read the file and save data into the dictionary
    """
    with open(file, 'r') as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s, current_s, expected_len, anagrams_list, prefix_index_list):
    """
    Using recursion to re-arrange the given string and to find words consisting of the same characters
    as the given string in the dictionary.

    :param s: string, The given string that should be divided and re-arranged to find the anagrams
    :param current_s: The current prefix
    :param expected_len: The expected number of the characters that should be in the anagrams
    :param anagrams_list: The list that collects all the anagrams we found
    :param prefix_index_list: The list to cache the index of the prefix in the dictionary
    """
    if len(s) == 0:
        anagrams_list.append(current_s)
        print(f'Found: {current_s}\nSearching...')
    else:
        placeholders = []
        for t in s:
            if t not in placeholders:
                placeholders.append(t)
                current_s += t
                prefix_index_list.append(get_prefix_index(current_s, expected_len, prefix_index_list[-1]))
                if prefix_index_list[-1] >= 0:
                    find_anagrams(s.replace(t, '', 1), current_s, expected_len, anagrams_list, prefix_index_list)
                current_s = current_s[:-1]
                prefix_index_list.pop()


def get_prefix_index(sub_s, expected_len, cached_index):
    """
    Find the index of a word in the dictionary that start with the prefix,
    and the number of its characters should be same as the expected number.

    :param sub_s: The prefix that the word should start with
    :param expected_len: The expected number of the characters in the word
    :param cached_index: The index of the prefix we found in the previous round
    """
    if cached_index > 0:
        for word in dictionary[cached_index:]:
            if len(word) == expected_len and word.startswith(sub_s):
                return dictionary.index(word)
            if not word.startswith(sub_s[0:-1]):
                return -1
    else:
        for word in dictionary[cached_index:]:
            if len(word) == expected_len and word.startswith(sub_s):
                return dictionary.index(word)
    return -1


if __name__ == '__main__':
    main()
