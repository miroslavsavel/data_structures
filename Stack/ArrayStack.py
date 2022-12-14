"""Basic example of an adapter class to provide a stack interface to Python's list."""

from Empty import Empty

"""
adapter class to provide a stack interface to Python's list.
"""
class ArrayStack:
    def __init__(self):
        """Create an empty stack"""
        self._data = []     # private list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list


"""
function that overwrite file line by line reversed using ArrayStack
"""
def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))       # we will reinsert newlines when writing
    original.close()

    # overwrite with contents in LIFO order
    output = open(filename, 'w')    # reopen file
    while not S.is_empty():
        output.write(S.pop() + '\n')    #reinsert newline characters
    output.close()



def match_parentheses(expression):
    """Return true is all delimiters are properly match. Flase otherwise"""
    lefty = '({['           # opening delimiters
    righty = ')}]'          # respective closing delims
    S = ArrayStack()
    for c in expression:
        if c in lefty:
            S.push(c)       # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                # it assumes that characters are in the same order in the lists lefty and righty
                # The index() method returns the index of the specified element in the list.
                return False    # mismatched symbols
    return S.is_empty()     # were all symbols matched?

# ===================================================================
if __name__ == '__main__':
  # S = ArrayStack()                 # contents: [ ]
  # # S.pop()         # raise exception
  # S.push(5)                        # contents: [5]
  # S.push(3)                        # contents: [5, 3]
  # print(len(S))                    # contents: [5, 3];    outputs 2
  # print(S.pop())                   # contents: [5];       outputs 3
  # print(S.is_empty())              # contents: [5];       outputs False
  # print(S.pop())                   # contents: [ ];       outputs 5
  # print(S.is_empty())              # contents: [ ];       outputs True
  # S.push(7)                        # contents: [7]
  # S.push(9)                        # contents: [7, 9]
  # print(S.top())                   # contents: [7, 9];    outputs 9
  # S.push(4)                        # contents: [7, 9, 4]
  # print(len(S))                    # contents: [7, 9, 4]; outputs 3
  # print(S.pop())                   # contents: [7, 9];    outputs 4
  # S.push(6)                        # contents: [7, 9, 6]
  # S.push(8)                        # contents: [7, 9, 6, 8]
  # print(S.pop())                   # contents: [7, 9, 6]; outputs 8

  # reverse_file("textak.txt")
  print(match_parentheses("({()hfbg})"))