class ListNode:
    def __init__(self, data, addr=None):
        self.data, self.addr = data, addr


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append_left(self, value):
        new_node = ListNode(value)
        new_node.addr = self.head
        self.head = new_node

    # def append_right(self, value):
