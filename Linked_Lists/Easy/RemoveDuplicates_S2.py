# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    while current_node.next is not None:
        if current_node.value == current_node.next.value:
            current_node.next =  current_node.next.next
        else:
            current_node =  current_node.next
        
    return linkedList
