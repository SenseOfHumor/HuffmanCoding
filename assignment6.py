## Full Name: Swapnil Deb
## UCID: sd2269

## CS 435 Advanced Data Structures and Algorithms
## Assignment 6 Huffman Coding
## @date: 4/27/25
## @author: Swapnil Deb

import heapq

class Node:
    def __init__(self, character = "", frequency = 0):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"Node({self.character}, {self.frequency})"

    def __traverse__(self):
        if self.left is not None:
            self.left.__traverse__()
        print(f"Node: {self.character} Frequency: {self.frequency}")
        if self.right is not None:
            self.right.__traverse__()    


from collections import defaultdict
import heapq
from tree import Node

def frequency_table(st: str) -> dict:
    """
    Function to create a frequency table for the passed string
    
    input:
    st: str : string to create frequency table for
    output:
    dict : frequency table
    """
    freq = defaultdict(int)
    for char in st:
        freq[char] += 1
    return dict(freq)   ## for readability


def Huffman_code(st: str) -> dict:
    """
    Function to create huffman code for the passed string
    
    input: st : string to create huffman code for
    output: dict : huffman code for the string
    dependency : tree.py, frequency_table, internal function dfs
    NOTE: for debugging, uncomment the print statements, they will show the complete process till the tree is built
    """
    freq = frequency_table(st)
    heap = []

    for char, freq in freq.items():
        heapq.heappush(heap, Node(char, freq))

    # print(f"Heap at start: {heap}")

    ## build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)  ## left node
        # print(f"left: {left}")
        right = heapq.heappop(heap) ## right node
        # print(f"right: {right}")
        # print(f"Heap after pop: {heap}")

        ## crete the new node
        char = ""
        freq = left.frequency + right.frequency
        node = Node(char, freq)
        heapq.heappush(heap, node)
        # print(f"node: {node}")
        # print(f"Heap after push: {heap}")
        # print("-" * 80)

        ## connection
        node.left = left
        node.right = right
       
    # print(f"After building the tree: {heap}")

    ## actual huffman code
    code = {}
    path_code = ""

    ## recursive DFS
    def __dfs(node, path_code):
        if node is None:
            return
        
        ## base case
        if node.left is None and node.right is None:
            code[node.character] = path_code
            return
        
        ## recursive case
        __dfs(node.left, path_code + "0")
        # print(f"left: {node.left} path_code: {path_code + '0'}")
        __dfs(node.right, path_code + "1")
        # print(f"right: {node.right} path_code: {path_code + '1'}")

    # print(f"heap[0]: {heap[0]}")
    __dfs(heap[0], path_code)
    return code


def Huffman_encode(st: str, code: dict) -> str:
    """
    Function to encode the string using huffman code
    
    input: st : string to encode
           code : huffman code
    output: str : encoded string
    NOTE: Assumption that the code is passed in a dictionary format
    """   
    encoded_string = ""
    for char in st:
        encoded_string += code[char]
    return encoded_string


def Huffman_tree(L: list) -> Node:
    """
    Function to create a huffman tree from the list of characters and their codes
    
    input: : L : list of tuples (char, code)
    output: Node : root of the tree"""

    root = Node()
    for char, code in L:
        curr = root  ## reset to root
        for bit in code:
            if bit == '0':
                if not curr.left:
                    curr.left = Node()
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node()
                curr = curr.right
        curr.character = char
    return root


def Huffman_decode(bst: str, tree: Node) -> str:
    """
    Function to decode the huffman code using the tree
    
    input: bst : string to decode
           tree : huffman tree
    output: str : decoded string
    """

    decoded_string = ""
    curr = tree

    ## traverse
    # for bit in bst:
    #     if bit == '0':
    #         curr = curr.left
    #         if not curr.left and not curr.right:
    #             decoded_string += curr.character
    #             curr = tree
    #     else:
    #         curr = curr.right
    #         if not curr.left and not curr.right:
    #             decoded_string += curr.character
    #             curr = tree

    for bit in bst:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right

        ## base case
        if not curr.left and not curr.right:
            decoded_string += curr.character
            curr = tree
    return decoded_string


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

if __name__ == "__main__":
    main()