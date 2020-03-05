from LinkedList import SingleLinkedList


class Queue:
    def __init__(self):
        self.mylist = SingleLinkedList()

    def push_queue(self, data):
        SingleLinkedList.add_tail(data)

    def pop_queue(self):
        return SingleLinkedList.remove_head()

