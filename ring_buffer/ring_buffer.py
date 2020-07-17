class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.index = 0

    def append(self, item):
        # If the queue is smaller than the capacity (5 in this case)
        if len(self.queue) < self.capacity:
            # Add the item to the back of the queue
            self.queue.append(item)
            # self.index += 1
        # If queue is at capacity    
        else:
            # Replace oldest value; self.queue[0] = first in queue
            self.queue[self.index] = item
            # Increment the index for added item(s)
            self.index += 1
        # If index +1 brings you over capacity
        if self.index +1 > self.capacity:
                # Reset the index
                self.index = 0

    def get(self):
        # Return all elements in given order
        return self.queue