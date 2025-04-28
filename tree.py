## @Author: Swapnil Deb
## Implementation of a binary tree

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