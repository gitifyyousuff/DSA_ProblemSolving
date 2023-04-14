# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n)T|(1)S
def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    print(current_node)
    while current_node is not None:
        next_distinct_node = current_node.next
        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next
        
        current_node.next =  next_distinct_node
        current_node = next_distinct_node

    return linkedList


linkedList= {{"id": "1", "next": "1-2", "value": 1},
      {"id": "1-2", "next": "1-3", "value": 1},
      {"id": "1-3", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 3},
      {"id": "3", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "3-3", "value": 4},
      {"id": "3-3", "next": "4", "value": 4},
      {"id": "4", "next": "5", "value": 5},
      {"id": "5", "next": "5-2", "value": 6},
      {"id": "5-2", "next": None, "value": 6}
}   


removeDuplicatesFromLinkedList(linkedList)