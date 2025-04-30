## CS 435 Advanced Data Structures and Algorithms
## Assignment 6 Huffman Coding
## @date: 4/27/25
## @author: Swapnil Deb

from tree import Node
from functions import Huffman_decode, Huffman_code, Huffman_tree, Huffman_encode, frequency_table

def main():
    st = "abbcccdddd"

    ## Frequency Table
    freq_table = frequency_table(st)
    print(f"a) frequency_table({st})")
    print("Character Frequencies:")
    for item in freq_table.items():
        print(f"\'{item[0]}\' : {item[1]}")

    ## Huffman_code
    print(f"\nb) Huffman_code({st})")
    code = Huffman_code(st)
    print(f"Huffman Codes:")
    for item in code.items():
        print(f"\'{item[0]}\' : {item[1]}")

    ## Huffman_encode
    print(f"\nc) Humman_encode({st}, {code})\nEncoded String:\n{Huffman_encode(st, code)}")

    ## Huffman_tree
    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(L)
    if tree:
        print(f"\nd) Huffman_tree({L})\nHuffman Tree created successfully")
    else:
        print(f"\nd) Huffman_tree({L})\nHuffman Tree creation failed")

    ## Huffman_decode
    bst = "0000010010010101011111"
    decode = Huffman_decode(bst, tree)
    print(f"\ne) Huffman_decode({bst}, {tree})\nDecoded String:\n{decode}")


    ## full test, including Unicode
    print(f"\n-----------------  full test  -----------------")
    st = "Swapnil is a student @ NJIT and incoming intern @ Prudential Financial for the year 2025, Unicode test: 🦧sd1234!@#$%^&*()_+"
    print(f"\nOriginal String: {st}")
    print(f"\nFrequency Table: {frequency_table(st)}")
    code = Huffman_code(st)
    print(f"\nHuffman Codes: {code}")
    encoded_string = Huffman_encode(st, code)
    print(f"\nEncoded String: {encoded_string}")
    tree = Huffman_tree(code.items())  ## dict iterable object, so it will work with my Huffman_tree function even tho it is not a list
    print(f"\nHuffman Tree: {tree}")
    decoded_string = Huffman_decode(encoded_string, tree)
    print(f"\nDecoded String: {decoded_string}")
    print(f"\nDecoded String matches original? {decoded_string == st}")

if __name__ == "__main__":
    main()