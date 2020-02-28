from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # UNDERSTAND:
        # ring buffer is a linked list of a given capacity where the oldest node touches the newst node
        # when a newer node is added, the oldest is overwritten
        # 4 phases of ring buffer life cycle I can see:
        # 1. add first node
        # 2. add nodes up to capacity
        # 3. add final node, and link that node (tail) to the original node (head), forming ring
        # 4. additional nodes keep the circle of life going
        
        # PLAN, first pass:
        # if sorage list is empty, add to head
        # if storage list has len > 0 but < capacity - 1, add to tail
        # if storage list has len capacity -1, add to tail and connect tail to original head (now ring)
        # if storage list has len capacity, replace the oldest node with the new one

        # EXECUTE:
        # add first node to head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        # add nodes to tail until at capacity minus 1
        elif self.storage.length < self.capacity - 1:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # add last node to tail, then connext tail's "next" to the head node
        # head is now oldest, but it's prev is tail, the newest
        # tail is now newst, but it's next is head, the oldest
        # use current to start tracking the most recent
        elif self.storage.length == self.capacity - 1:
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
            self.storage.head.prev = self.storage.tail
            self.current = self.storage.head

        # overwrite the head (oldest) with the current item (newest)
        # shift head and tail by 1
        elif self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next
        else:
            print("RingBuffer failed, current length exceeds capacity. Please debug.")

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = self.storage.head

        for i in range(0, self.storage.length):
            list_buffer_contents.append(temp.value)
            temp = temp.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cursor = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.cursor] = item
            if self.cursor < self.capacity - 1:
                self.cursor += 1
            else:
                self.cursor = 0

    def get(self):
        return self.storage
