from Empty import Empty

class ArrayDeque:
    """Implementation of double ended queue using List"""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty Deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __str__(self):
        """string representation of deque"""
        return str(self._data)

    def is_empty(self):
        """returns true if deque is empty"""
        return self._size == 0

    def add_last(self, e):
        """Add an element to the back of queue"""
        # check if we have some place at the beginning of queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size
        # check avaible position at the beginning of queue for insert new element
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        # wrap arround beginning of the array
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._front = avail
        self._size += 1


    def delete_first(self):
        """Remove and return the first element of the queue FIFO"""
        """Element is not truly removed from List due to inefficiency"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shrink the underlying array
        # robust approach - reduce array to halfof its current size
        # whenever the number of elements sored in it falls below
        # one fourth of its capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        """Remove from the back of queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        last_element_index = (self._front + self._size -1) % (len(self._data))
        value_of_last = self._data[last_element_index]
        self._data[last_element_index] = None
        self._size -= 1
        # shrink array if possible
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return value_of_last

    def _resize(self, cap):         # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data         # keep track of existing list
        self._data = [None] * cap   # allocate list with new capacity
        # we use walk variable to walk on old array and put the elements to the right indices
        # because modular arithmetic depend on the size of the array that changed
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]   # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size aj modulus
        self._front = 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue
        If empty - raise exception
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]


    def last(self):
        """Return (but do not remove) the last element of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        last_element_index = (self._front + self._size - 1) % (len(self._data))
        return self._data[last_element_index]


#==============================================================================Driver code
if __name__=="__main__":
    d = ArrayDeque()
    for i,c in enumerate("ABCDEFGHIJKLMNOP"):
        d.add_last(c)
        print(d)
    # for k in range(d.__len__()):
    #     d.delete_first()
    #     print(d)
    d.delete_first()
    print(d)
    d.add_first('X')
    d.add_first('t')
    d.add_first('y')
    print(d)
    d.add_last('L')
    print(d)
    d.add_last('G')
    print(d)
    # d.add_first('y')
    # print(d)
    # delete last test
    # for k in range(d.__len__()):
    #     d.delete_last()
    #     print(d)
    print(d.first())
    print(d.last())