from typing import List, Optional
import sys
import traceback


# TODO: Have to write MaxHeap Class and comments in code

# function to get the parent index
def get_parent_index(child_index: int) -> int:
    return (child_index - 1) // 2


# function to get the left child index
def get_left_child_index(parent_index):
    return (2 * parent_index) + 1


# function to get the right child index
def get_right_child_index(parent_index):
    return (2 * parent_index) + 2


def has_parent_node(child_index):
    return get_parent_index(child_index) >= 0


# class definition of minheap
class MinHeap:
    def __init__(self) -> None:
        self.nodes: List[int] = []

    # method to swap the values of two nodes
    def swap_nodes(self, first_index: int, second_index: int) -> None:
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

    def get_min_child_index(self, parent_index: int) -> int:
        min_child_index = get_left_child_index(parent_index)

        if self.has_right_child(parent_index) and self.nodes[get_right_child_index(parent_index)] < self.nodes[
            min_child_index]:
            return get_right_child_index(parent_index)
        return min_child_index

    def has_left_child(self, parent_index: int) -> bool:
        return get_left_child_index(parent_index) < len(self.nodes)

    def has_right_child(self, parent_index: int) -> bool:
        return get_right_child_index(parent_index) < len(self.nodes)

    def heapify_up(self, child_index: Optional[int] = None) -> None:
        if child_index is None:
            child_index = len(self.nodes) - 1

        parent_index = get_parent_index(child_index)

        # check whether the parent is grater than the child node value
        if has_parent_node(child_index) and self.nodes[parent_index] > self.nodes[child_index]:
            # swap the parent with child
            self.swap_nodes(parent_index, child_index)

            # recursively traverse the tree to heapify up
            self.heapify_up(parent_index)

    def heapify_down(self, parent_index: Optional[int] = 0) -> None:

        if parent_index > len(self.nodes) or not self.has_left_child(parent_index):
            return

        min_child_index = self.get_min_child_index(parent_index)

        if self.nodes[parent_index] > self.nodes[min_child_index]:
            self.swap_nodes(parent_index, min_child_index)
            self.heapify_down(min_child_index)

    def insert_node(self, value):
        self.nodes.append(value)
        self.heapify_up()

    def delete_root_node(self):
        deleted_node = self.nodes[0]

        self.nodes[0] = self.nodes[-1]
        del self.nodes[-1]

        self.heapify_down()

        return deleted_node


# MaXHeap Class Definition
class MaxHeap:

    def __init__(self):
        self.nodes: List[int] = []

    # method to check whether the child node has parent node or not
    def has_parent(self, child_index: int) -> bool:
        return 0 <= get_parent_index(child_index) < len(self.nodes)

    # method to check whether the parent has left child or not
    def has_left_child(self, parent_index: int) -> bool:
        return get_left_child_index(parent_index) < len(self.nodes)

    # method to check whether the parent has right child or not
    def has_right_child(self, parent_index: int) -> bool:
        return get_right_child_index(parent_index) < len(self.nodes)

    # helper method to swap the nodes
    def swap_nodes(self, first_index: int, second_index: int) -> None:
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

    # method to heapify up the tree when new node is inserted
    def heapify_up(self, child_index: Optional[int] = None) -> None:
        if child_index is None:
            child_index = len(self.nodes) - 1

        parent_index = get_parent_index(child_index)

        if self.has_parent(child_index) and self.nodes[child_index] > self.nodes[parent_index]:
            # swap the parent and child nodes
            self.swap_nodes(parent_index, child_index)
            # recursively heapify up till the root node
            self.heapify_up(parent_index)

    # method to get the max nodes of two children
    def get_max_child_index(self, parent_index: int) -> int:
        left_child_index = get_left_child_index(parent_index)
        if self.has_right_child(parent_index) and self.nodes[left_child_index] < self.nodes[
            get_right_child_index(parent_index)]:
            return get_right_child_index(parent_index)
        return left_child_index

    # method to heapify down the max heap
    def heapify_down(self, parent_index: int = 0) -> None:

        # return if parent node doesn't have a left child
        if parent_index >= len(self.nodes) or not self.has_left_child(parent_index):
            return

        # get the max child of two child nodes
        max_child_index = self.get_max_child_index(parent_index)

        # heapify the tree
        if self.nodes[max_child_index] > self.nodes[parent_index]:
            # swap the child and parent nodes
            self.swap_nodes(max_child_index, parent_index)

            # recursively heapify down the tree until the last node
            self.heapify_down(max_child_index)

    # method to insert a new node
    def insert_node(self, value):
        self.nodes.append(value)
        self.heapify_up()

    # method to delete the root of maxheap
    def delete_root_node(self) -> int:
        node = self.nodes[0]

        # swap the first node with last node in tree
        self.nodes[0] = self.nodes[-1]
        # delete the last node
        del self.nodes[-1]

        # rearranging the tree
        self.heapify_down()

        return node


# main function
if __name__ == "__main__":
    try:

        # Min Heap Implementation
        min_heap = MinHeap()
        elements = [10,8,5,15,6] # map(int,input("Enter the elements as comma seperated values: ").split(","))
        for element in elements:
            min_heap.insert_node(element)
        print("Array Representation of Min Heap: ",min_heap.nodes)
        print(min_heap.delete_root_node())
        print("Array Representation of Min Heap: ",min_heap.nodes)

        # Max Heap implementation
        max_heap = MaxHeap()
        elements = [10, 8, 5, 15, 6]  # map(int,input("Enter the elements as comma seperated values: ").split(","))
        for element in elements:
            max_heap.insert_node(element)
        print(f"Array representation of max heap: {max_heap.nodes}")
        print(f"The Deleted Root Node: {max_heap.delete_root_node()}")
        print(f"Array representation of max heap: {max_heap.nodes}")


    except Exception as e:
        print(f"*** Error: Something went wrong,  runtime error occurred: {str(e)} ***")
        traceback.print_exc()
