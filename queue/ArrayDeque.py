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

if __name__=="__main__":
    d = ArrayDeque()
    for i,c in enumerate("ABCDEFGHIJKLMNOP"):
        d.add_last(c)
        print(d)