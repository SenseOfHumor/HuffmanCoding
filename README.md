# HuffmanCoding
@author: Swapnil Deb
`This is the pythonic implementation of Huffman Coding algorithm `

### Design choices
- **heapq**, alongside custom dunder method for lessThan `__lt__` since the comparison is done between two custom types and not internal types.
- in function frequency_table, the return is `dict(freq)` and not `freq` purely because of readability purposes, it technically does cause a little bit overhead cost, but for this project, it is negligible.
- internal helper function `__dfs` to traverse the nodes in the binary tree.
- Huffman codes generated can be different at times due to the nature of how heapify does its operations for inserting and deleting, it will not affect the actual encoding or decoding however. Given a string, a proper encoded string is generated, and given a tree and encoded string, a proper decoded string is generated.
- Project is broken into three files: `tree.py` , `functions.py`, `main.py` with implementation of the binary tree, huffman functions and main functions are separated respectively.

### What is Huffman Coding?

In short:  
> **Take characters, assign shorter codes to more frequent ones, make longer codes for rarer ones.**

Huffman Coding is a greedy algorithm for lossless data compression.  
It builds a binary tree where the path from the root to each character defines its binary code:
- **Dont waste bits** → Instead of using 7 bits in ASCII and 16 in unicode, we use variable length codes instead of fixed length and as a result (keep reading the following)...
- **Frequent characters** → **shorter codes**
- **Rare characters** → **longer codes**

This ensures that no code is a prefix of another (a.k.a. prefix-free property), and decoding is very easy.

Basically, Huffman figured out that if you're going to waste bits, **at least waste them smartly**.
