class ListNode:
    def __init__(self, data, nxt=None):
        self.data, self.nxt = data, nxt


class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None
        self.size = 0

    def get_size(self):
        return self.size

    def append_left(self, value):  # head --> othernode -> othernode -> othernode -> tail
        new_node = ListNode(value)
        new_node.nxt = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def append_right(self, value):  # newnode
        new_node = ListNode(value)

        if self.tail is not None:
            self.tail.nxt = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def pop_left(self):  # node
        # store the value of the curr_head
        result = self.head.data

        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            # move head to nxt
            self.head = self.head.nxt  # head ---> other ----> other ---> other ---> tail

        # return the stored value
        self.size -= 1
        return result

    def pop_right(self):  # node
        result = self.tail.data

        if self.head == self.tail:
            self.head, self.tail = None, None
            self.size -= 1
            return result

        node = self.head
        prev = None

        while node is not self.tail:
            prev = node
            node = node.nxt

        del self.tail

        self.tail = prev
        self.tail.nxt = None

        self.size -= 1
        return result

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end=', ')
            node = node.nxt

    def insert_right(self, node):
        # homework
        pass


if __name__ == '__main__':
    sll = LinkedList()

    sll.append_left(3)
    sll.append_left(2)
    sll.append_left(1)

    sll.append_right(4)
    sll.append_right(5)
    sll.append_right(6)

    print('CurrSize', sll.get_size())

    print(sll.pop_left())  # 1
    print(sll.pop_left())  # 2
    print('CurrSize', sll.get_size())

    print(sll.pop_right())  # 6
    print(sll.pop_right())  # 5
    print(sll.pop_right())  # 4
    print(sll.pop_right())  # 3
    print('CurrSize', sll.get_size())

    sll.print()
