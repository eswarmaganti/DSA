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
        print(f'{node.value} -> ', end="")
        if node.next is not None:
            self.traverse_single_linked_list(node.next)

    # method to delete the node at specific index in SLL
    def delete_node(self, position: int, node: Node, prev_node: Optional[Node] = None, search_position: int = 0) -> int:
        # if search position is found
        if position == search_position:
            # point the previous node to the targetNode's next pointer value
            prev_node.next = node.next
            # remove the targetNode from the list
            node.next = None
            return
        else:
            search_position += 1
            self.delete_node(position=position, node=node.next, prev_node=node, search_position=search_position+1)

    # method to insert a value in linkedlist at a given position
    def insert_node_at_position(self, position: int, value: int, node: Node, prev_node: Optional[Node] = None, search_position: Optional[int] = 0) -> None:
        if position == search_position:
            # create a new node
            new_node = Node(value)
            # assign the new node next pointer to current node
            new_node.next = node
            # update the previous node next pointer to new node
            prev_node.next = new_node
            print(f"*** Success: The Key - {value} is inserted at position - {position} successfully ***")
            return
        elif node.next is None:
            print(f"*** Warning: The position - {position} is not available in List to insert key - {value} ***")
            return
        else:
            self.insert_node_at_position(position, value, node=node.next, prev_node=node, search_position=search_position+1)

    # method to search a value in linked list
    def search_node(self, value: int, node: Node, search_position: int = 0) -> int:
        if node.value == value:
            return search_position
        elif node.next is None:
            return -1
        else:
            return self.search_node(value, node.next, search_position=search_position+1)


# main function
if __name__ == "__main__":
    try:
        sll = SingleLinkedList()
        elements = map(int,input("Enter elements as comma separated values: ").split(","))

        for element in elements:
            sll.insert_node(sll.head, element)

        sll.traverse_single_linked_list(sll.head)
        print()

        delete_key = int(input("Enter a key to delete: "))
        # Searching a key in LinkedList
        print(f"The Value - {delete_key} is found at position: {sll.search_node(value=delete_key, node=sll.head.next)}")

        # deleting a node and traversing the LL
        sll.delete_node(position=2, node=sll.head.next)
        sll.traverse_single_linked_list(sll.head)
        print("\n")

        # insert a node at given position
        [value,position] = map(int,input("Enter the (value,position) as comma separated values: ").split(","))
        sll.insert_node_at_position(value=value, position=position, node=sll.head)
        sll.traverse_single_linked_list(sll.head)
        print("\n")

    except Exception as e:
        print(f"*** Error: Something went wrong, runtime exception occurred: {str(e)} ***")
        traceback.print_exc()

