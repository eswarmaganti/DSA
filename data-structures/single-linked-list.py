import traceback
from typing import Optional, List


# linked list Node Class
class Node:
    def __init__(self,value: Optional[int] = None) -> None:
        self.value: int = value
        self.next: Optional[Node] = None


class SingleLinkedList:
    def __init__(self):
        self.head: Node = Node()

    # method to insert a node in linked list
    def insert_node(self, node: Node, value: int) -> None:
        # check whether the head nodes next pointer is empty
        if node.next is None:
            node.next = Node(value)
            return
        else:
            self.insert_node(node.next, value)

    # method to traverse the single linked list
    def traverse_single_linked_list(self, node: Node):
        print(node.value)
        if node.next is not None:
            self.traverse_single_linked_list(node.next)

    # method to delete the node at specific index in SLL
    def delete_node(self, position: int) -> int:
        pass

    # method to insert a value in linkedlist at a given position
    def insert_node_at_index(self, position: int, value: int, node: Node) -> None:
        pass

    # method to search a value in linked list
    def search_node(self, value: int) -> int:
        pass


# main function
if __name__ == "__main__":
    try:
        sll = SingleLinkedList()
        elements = map(int,input("Enter elements as comma seperated values: ").split(","))

        for element in elements:
            sll.insert_node(sll.head, element)

        sll.traverse_single_linked_list(sll.head.next)

    except Exception as e:
        print(f"*** Eroor: Something went wrong, runtime exception occured: {str(e)} ***")
        traceback.print_exc()

