"""
File: huffman_encoding_ANS.py
Name: Wade Chao
-----------------------------------
This program demonstrates the idea of zipping/unzipping
through the algorithm of Huffman Encoding.
We will be using all of the important concepts
we learned today to complete this hugh project.
"""

from ds import Tree, PriorityQueue, ListNode

# The string to be zipped/unzipped
TARGET = 'my name is wade chao nice to meet you'


def main():
    d = build_dict()
    print('----------Build dict----------')
    print(d)
    ############################
    priority_queue = PriorityQueue()
    enqueue_with_tuples(priority_queue, d)
    print('----------Char count----------')
    priority_queue.traversal_tree_elements()
    ############################
    tree = encoding_tree(priority_queue)
    print('----------Build tree----------')
    bfs(tree)
    zipped = encoding(tree, TARGET)
    print('--------------Encoded Result--------------')
    print(f'{TARGET} (bits: {len(TARGET) * 8}) \nEncoded: {zipped} (bits: {len(zipped)})')
    decoding(tree, zipped)


def build_dict():
    """
    :return: dict, a Python dictionary containing ch as key,
                    the number of ch occurrence as value
    """
    ans = {}
    for ch in TARGET:
        if ch not in ans:
            ans[ch] = 1
        else:
            ans[ch] += 1
    return ans


def enqueue_with_tuples(priority_queue, d):
    """
    enqueue by passing tuple to pq.enqueue,
    pq.enqueue will first convert tuple into ListNode
    then insert ListNode into queue in order by tuple[1] (count)
    :param priority_queue:
    :param d:
    :return:
    """
    for ch, count in d.items():
        tree = Tree(None, ch, None)
        priority_queue.enqueue((tree, count))


def bfs(tree):
    queue = [tree]
    while len(queue) != 0:
        el: Tree = queue.pop(0)
        print(el.val, end=' | ')
        # left
        if el.left:
            queue.append(el.left)
        # right
        if el.right:
            queue.append(el.right)
    print('')


def encoding_tree(pq: PriorityQueue):
    """
    :param pq: PriorityQueue, containing all the ch we need to encode
    :return: Tree, a binary tree that has all the ch encoded
    """
    while True:
        if pq.is_empty():
            return None
        first_node: ListNode = pq.dequeue()
        first_tree: Tree = first_node.val[0]
        first_priority_count: int = first_node.val[1]
        # if first_node is the last element in queue, finish constructing and return the tree
        if pq.is_empty():
            return first_tree
        second_node: ListNode = pq.dequeue()
        second_tree: Tree = second_node.val[0]
        second_priority_count: int = second_node.val[1]
        new_tree = Tree(first_tree, first_priority_count + second_priority_count, second_tree)
        pq.enqueue((new_tree, first_priority_count + second_priority_count))


def encoding(tree, target):
    """
    :param tree: Tree, Huffman Tree containing the Huffman codes for characters in TARGET
    :param target: str, the unzipped string
    :return: str, the zipped string of TARGET
    """
    encoding_dict = {}
    dfs(tree, tree, encoding_dict, '')
    print('----------Encode for each----------')
    print(encoding_dict)
    ans = ''
    for ch in target:
        ans += encoding_dict[ch]
    return ans


def dfs(tree, current, encoding_d, current_encoding):
    # base case
    if current.left is None and current.right is None:
        encoding_d[current.val] = current_encoding
    else:
        dfs(tree, current.left, encoding_d, current_encoding + '0')
        dfs(tree, current.right, encoding_d, current_encoding + '1')


def decoding(tree, zipped_words):
    """
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, the mystery compressed binary digits to be unzipped
    """
    ans_lst = []
    add_to_ans_lst(tree, zipped_words, ans_lst, tree)
    print('--------------Decoding...-----------------')
    print(''.join(ans_lst))


def add_to_ans_lst(tree, zipped_words, ans_lst, current):
    """
    This function trace all the binaries in zipped_words down to leaves
    and add the character to ans_lst
    -------------------------------------------------
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, binaries that were zipped from TARGET
    :param ans_lst: List[str], containing characters that are in leaf node
    :param current: Tree, pointer of where the current node is
    """
    if len(zipped_words) != 0:
        # base case
        if current.left is None and current.right is None:
            ans_lst.append(current.val)
            add_to_ans_lst(tree, zipped_words, ans_lst, tree)
        else:
            if zipped_words[0] == '0':
                add_to_ans_lst(tree, zipped_words[1:], ans_lst, current.left)
            elif zipped_words[0] == '1':
                add_to_ans_lst(tree, zipped_words[1:], ans_lst, current.right)
    else:
        # When zipped_words is empty, append the last word into ans_lst
        ans_lst.append(current.val)


if __name__ == '__main__':
    main()
