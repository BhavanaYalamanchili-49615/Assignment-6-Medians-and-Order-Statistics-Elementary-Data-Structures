# A singly-linked list has been implemented with simple functions like adding at the head, deleting by value and traversal.
# Elements were printed in succession in the list and nodes were added or removed dynamically.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Deletion of a node with a specific value
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    # Traversing the list and printing values
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(10)
# Traversing the linked list
linked_list.traverse()
linked_list.delete(5)
# Traversing after deletion
linked_list.traverse()