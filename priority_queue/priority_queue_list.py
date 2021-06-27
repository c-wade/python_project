"""
File: priority_queue_list.py
Author: Wade Chao
----------------------------------
This program shows how to build a priority queue by
using Python list. We will be discussing 3 different
conditions while appending:
1) Prepend
2) Append
3) Append in between
"""

# This constant controls when to stop the user input
EXIT = ''


def main():
    priority_queue = []

    print('--------------------------------')
    while 1:
        name = input('Patient: ')
        if name == EXIT:
            break
        priority = int(input('Priority: '))
        data = (name, priority)
        if len(priority_queue) == 0:
            priority_queue.append(data)
        else:
            # prepend
            if priority < priority_queue[0][1]:
                # tie-breaking
                priority_queue.insert(0, data)
            # append
            elif priority >= priority_queue[-1][1]:
                priority_queue.append(data)
            # in between
            else:
                for i in range(len(priority_queue)-1):
                    # i -> i+1
                    if priority_queue[i][1] <= priority < priority_queue[i+1][1]:
                        priority_queue.insert(i+1, data)
                        break

    print('--------------------------------')

    print(priority_queue)


if __name__ == '__main__':
    main()
