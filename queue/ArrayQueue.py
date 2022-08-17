from Empty import Empty

class ArrayQueue:
    """FIFO queue implementation using a python list as underlying storage"""
    DEFAULT_CAPACITY = 10       # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue
        If empty - raise exception
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue FIFO"""
        """Element is not truly removed from List due to inefficiency"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
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
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]   # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size aj modulus
        self._front = 0


Q = ArrayQueue()
for i in range(1,10):
    Q.enqueue(i)
Q.dequeue()
Q.enqueue(5)
Q.enqueue(6)
for i in range(1,10):
    Q.enqueue(i)
Q.enqueue(6)
Q.enqueue(7)
Q.dequeue()
for i in range(1,10):
    Q.enqueue(i)
Q.enqueue(7)
Q.dequeue()
print(Q.first())