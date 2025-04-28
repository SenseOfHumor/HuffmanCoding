# HuffmanCoding
 This is the pythonic implementation of Huffman Coding algorithm 

### Design choices
- heapq, alongside custom dunder method for lessThan `__lt__` since the comparison is done between two custom types and not internal types
- in function frequency_table, the return is `dict(freq)` and not `freq` purely because of readability purposes, it technically does cause a little bit overhead cost, but for this project, it is negligible 
