"""
CS2302
Lab3 Part B
Purpose: gain experience with BST
Created on Mon Oct 9, 2019
Diego Aguirre
@author: Nancy Hernandez
"""

from AVL_Tree import AVLTree
from Red_Black_Tree import RedBlackTree


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def print_anagrams(word, english_words, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur)


def count_anagrams(word, english_words, prefix=""):
    global count
    count = 0
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            count += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                count_anagrams(before + after, prefix + cur)
    return count


# Reads file and puts them in the avl tree
def AVL_read_file():
    word_file = open("english_words_two.txt", "r")
    line = word_file.readline()
    avl = AVLTree()

    for line in word_file:
        word = line.replace("\n", "")
        avl.AVL_insert(word)
    return avl


# Reads file and puts them in the rb tree
def RB_read_file():
    word_file = open("english_words_two.txt", "r")
    line = word_file.readline()
    rb = RedBlackTree()

    for line in word_file:
        word = line.replace("\n", "")
        rb.RB_insert(word)
    return rb


def main():
    user_option = input("What type of binary search tree would you like to use? Type 'a' for AVL or 'b' for Red-Black "
                        "Tree")
    if user_option is "a":
        avl = AVL_read_file()
        a_v_l = avl.print_tree(avl.root)
    elif user_option is "b":
        r = RB_read_file()
        r.print_tree(r.root)
    else:
        print("You have entered an invalid option.")

    # print(print_anagrams())
    print(count_anagrams("spot", a_v_l))


main()
