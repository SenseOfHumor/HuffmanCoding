## @Author: Swapnil Deb
## Implementation of functions for huffman coding

from collections import defaultdict
import heapq
from tree import Node

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



## Tests
# st = "abbcccdddd"
# # print(f"Huffman code for {st}: {Huffman_code(st)}")
# # print(f"Encoded string for {st}: {Huffman_encode(st, Huffman_code(st))}")

# tree = Huffman_tree([('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')])
# # print(tree.__traverse__())
# bst = "0000010010010101011111"
# print(f"Decoded string for \"{bst}\": \"{Huffman_decode(bst, tree)}\"")