# Ben Lizza
# 03/04/20
# Linked List WITH TAIL POINTER to be used in a Queue


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def prepend(self, data):
        self.head = ListNode(data=data, next=self.head)

    def add_head(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def add_tail(self, data):
        new_node = ListNode(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_tail(self):
        curr_node = self.head
        previous_node = self.head
        while curr_node.next:
            previous_node = curr_node
            curr_node = curr_node.next
        previous_node.next = None
        return curr_node.data

    def clear_list(self):
        self.head = None
