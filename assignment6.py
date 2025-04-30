## Full Name: Swapnil Deb
## UCID: sd2269

## CS 435 Advanced Data Structures and Algorithms
## Assignment 6 Huffman Coding
## @date: 4/27/25
## @author: Swapnil Deb

import heapq
from collections import defaultdict

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


def frequency_table(st: str) -> dict:
    """
    Function to create a frequency table for the passed string
    
    Args:
        st: string to create frequency table for
    Returns:
        dict: frequency table
    """
    ## defensive programming
    if not st:
        return {}
    
    freq = defaultdict(int)
    for char in st:
        freq[char] += 1
    return dict(freq)   ## for readability


def Huffman_code(st: str) -> dict:
    """
    Function to create huffman code for the passed string
    
    Args: 
        st: string to create huffman code for
    Returns: 
        dict: huffman code for the string
    dependencies: 
        tree.py, frequency_table, internal helper function dfs
    NOTE: for debugging, uncomment the print statements, they will show the complete process till the tree is built
    """
    ## defensive programming
    if not st:
        return {}
    
    freq = frequency_table(st)
    heap = []

    ## bug fix for empty/unique string
    if len(freq) == 1:
        char = next(iter(freq))
        return {char: '0'}  ## observed while testing

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
    
    Args: 
        str: string to encode
        code : huffman code for the string
    Return: 
        str: encoded string
    NOTE: Assumption that the code is passed in a dictionary format
    """
    ## defensive programming
    if not st or not code:
        return ""
       
    encoded_string = ""
    for char in st:
        encoded_string += code[char]
    return encoded_string


def Huffman_tree(L: list) -> Node:
    """
    Function to create a huffman tree from the list of characters and their codes
    
    Args:
        L: list of tuples (char, code)
    Return: 
        Node: root of the tree"""

    ## defensive programming
    if not L:
        return None
    
    root = Node()
    for char, code in L:    ## will work with any iteerable obj
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
        curr.character = char   ## build tree till end and assign the char
    return root


def Huffman_decode(bst: str, tree: Node) -> str:
    """
    Function to decode the huffman code using the tree
    
    Args: 
        bst: string to decode
        tree: huffman tree
    Returns: 
        str: decoded string
    """
    ## defensive programming
    if not bst or not tree:
        return ""

    decoded_string = ""
    curr = tree

    for bit in bst:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right

        ## reached the end
        if not curr.left and not curr.right:
            decoded_string += curr.character
            curr = tree
    return decoded_string


def main():
    """
    Main function to test the functions
    Note: Test case with user input is commented out at the end, uncomment to test with user input (works with unicode as well)
    """

    st = "abbcccdddd"    ## example from the assignment

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
    print(f"\nc) Huffman_encode({st}, {code})\nEncoded String:\n{Huffman_encode(st, code)}")

    ## Huffman_tree
    ## NOTE: This uses a hardcoded example from the assignment and not the tree generated in (b)
    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(L)
    if tree:
        print(f"\nd) Huffman_tree({L})\nHuffman Tree created successfully")
    else:
        print(f"\nd) Huffman_tree({L})\nHuffman Tree creation failed")

    ## Huffman_decode
    ## NOTE: Using professor's example from the assignment for testing
    bst = "0000010010010101011111"
    decode = Huffman_decode(bst, tree)
    print(f"\ne) Huffman_decode({bst})\nDecoded String:\n{decode}")

    # full test with user input, uncomment the below lines to test with user input
    print(f"\n-----------------  full test  -----------------")
    st = input("Enter a string to encode: ")
    if not st:
        print("Please provide a valid string")
        return
    print(f"\nOriginal String: {st}")
    code = Huffman_code(st)
    encoded_string = Huffman_encode(st, code)
    tree = Huffman_tree(code.items())
    print(f"\nHuffman encoding of {st}: {code}\nDecoded String: {Huffman_decode(encoded_string, tree)}")
    print(f"\nDecoded String matches original? {Huffman_decode(encoded_string, tree) == st}")

if __name__ == "__main__":
    main()