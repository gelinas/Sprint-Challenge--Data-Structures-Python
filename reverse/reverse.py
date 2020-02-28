class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # Head will become tail, next will point to none instead of item 2
    # tail will become head, next will point to next to last item instead of none
    # every item in the middle will point to the prev node instead of the current next
    
    # edge case: empty list
    if self.head == None:
        return None

    # edge case: one item
    if self.head.next_node == None:
        return self.head

    # two ore more items: swap em up
    prev_one = None
    current = self.head
    next_one = current.next_node
    while next_one != None:
        current.next_node = prev_one
        prev_one = current
        current = next_one
        next_one = current.next_node
    # modify last node and fix head
    current.next_node = prev_one
    self.head = current
        