class Stack:
    """ Implementation of a stack data structure to be used during propagation.

    The stack class creates a list which will be populated by 
    the neighbours of most recently collapsed tile.

    """

    def __init__(self):
        """Initialize list."""
        self.items = []

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0 # Returns `True` when stack is empty

    def push(self, item):
        """Adds `item` to top of stack."""
        self.items.append(item)

    def pop(self):
        """Removes top item froms stack, if it is not empty."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def size(self):
        """Returns integer representing size of array."""
        return len(self.items)
