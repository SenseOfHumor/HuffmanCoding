## @Author: Swapnil Deb
## Implementation of functions for huffman coding

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

def huffman_code(st: str) -> dict:
    """
    Function to create huffman code for the passed string
    
    input: st : string to create huffman code for
    output: dict : huffman code for the string
    dependency : tree.py, frequency_table
    """
    freq = frequency_table(st)
    heap = []

    for char, freq in freq.items():
        heapq.heappush(heap, Node(char, freq))

    # print(heap)

    ## build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)  ## left node
        right = heapq.heappop(heap) ## right node
        ## crete the new node

        char = ""
        freq = left.frequency + right.frequency
        node = Node(char, freq)
        heapq.heappush(heap, node) 

        ## connection
        node.left = left
        node.right = right
       
    # print(heap)

    ## actual huffman code
    

## Tests
st = "abbcccdddd"
print(huffman_code(st))