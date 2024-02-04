class ListNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next = next_node
  
class LinkedList:
  def __init__(self) -> None:
    self.head = ListNode(-1)
    self.tail = self.head
    self.length = 0
  
  def get(self, index: int) -> int:
    if index >= self.length or index < 0:
      return -1

    i = 0
    curr = self.head.next
    while i < index:
      curr = curr.next
      i += 1
    return curr.value

    # alternative
    # i = 0
    # while curr:
    #   if i == index:
    #     return curr.value
    #   i += 1
    #   curr = curr.next
    # return -1
  
  def insertHead(self, val: int) -> None:
    new_node = ListNode(val)
    new_node.next = self.head.next
    self.head.next = new_node
    self.length += 1

  def insertTail(self, val: int) -> None: 
    new_node = ListNode(val)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1

  def remove(self, index: int) -> bool:
    i = 0
    curr = self.head
    while i < index and curr:
      curr = curr.next
      i += 1
    
    if curr and curr.next:
      if curr.next == self.tail:
        self.tail = curr
      curr.next = curr.next.next
      self.length -=1
      return True
    return False
        
      
  def getValues(self) -> list[int]:
    values = []
    
    curr = self.head.next
    while curr:
      values += [curr.value]
      curr = curr.next
    
    return values
  
  def getLength(self) -> int:
    print(self.length)
      
class main():
  list = LinkedList()
  
  list.insertTail(1)
  # value = list.get(0)
  # print(value)
  
  list.insertTail(3)
  # value = list.get(1)
  # print(value)
  
  # remove = list.remove(5)
  # print(remove)
  
  array = list.getValues()
  print(array)
  
  # remove = list.remove(1)
  # print(remove)

  # list.getLength()

  # remove = list.remove(0)
  # print(remove)

  # list.getLength()