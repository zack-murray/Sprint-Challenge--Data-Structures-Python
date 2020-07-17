class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Using recursion, not a loop
        # Checking for empty list
        if node is None:
            return
        # Check for last node in the list(points to None)
        elif node.next_node is None:
            # Set the last node as the head
            self.head = node
            # Set the next node to be the previous node instead
            node.next_node = prev
            return
        else:
            # Call the method, reverses the list 
            self.reverse_list(node.next_node, node)
            # Will reverse list again without this
            node.next_node = prev
