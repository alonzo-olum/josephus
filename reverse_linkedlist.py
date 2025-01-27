#!/usr/bin/env python3

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    previous, current = None, head

    while current:
        next_node = current.next
        current.next = previous

        previous = current
        current = next_node
    return previous

def to_string(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# main block
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    to_string(reverse(head))
