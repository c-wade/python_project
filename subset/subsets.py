"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    count = []
    list_sub_lists_helper(lst, [], count)
    print(f'Total: {sum(count)}')


def list_sub_lists_helper(lst, current_lst, count):
    count.append(1)
    if len(lst) == 0:
        print(current_lst)
    else:
        ele = lst.pop()
        # Not choose and explore
        list_sub_lists_helper(lst, current_lst, count)
        # Choose and explore
        current_lst.append(ele)
        list_sub_lists_helper(lst, current_lst, count)
        # Un-choose
        current_lst.pop()
        lst.append(ele)


if __name__ == '__main__':
    main()
