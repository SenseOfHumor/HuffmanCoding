## @Author: Swapnil Deb
## Implementation of functions for huffman coding

from collections import defaultdict

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


## Tests
print(frequency_table("hello world"))