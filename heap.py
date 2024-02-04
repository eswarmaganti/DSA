# Implementing Heap Data structure using python


from typing import List,Optional


class Heap:

    def __init__(self,nodes:List[int]):
        self.nodes = []

        # creating the heap
        for node in nodes:
            self.add_node(node)

    # method which returns the left child node index of parent node in heap
    def __get_left_child_index(self,parent_index:int) -> int:
        return (2 * parent_index) +1

    # method which returns the right child node index of parent node in heap
    def __get_right_child_index(self,parent_index:int)->int:
        return (2 * parent_index) + 2

    # method which returns the parent node index of left/right child in heap
    def __get_parent_index(self,child_index:int)->int:
        return (child_index - 1) // 2

    # method to validate whether the parent node have left child or not
    def __has_left_child(self,parent_index:int)->bool:
        return self.__get_left_child_index(parent_index) < len(self.nodes)

    # method to validate whether the parent node have right child or not
    def __has_right_child(self,parent_index:int)->bool:
        return self.__get_right_child_index(parent_index) < len(self.nodes)

    # method to validate whether the child node have parent or not
    def __has_parent(self,child_index:int)->bool:
        return self.__get_parent_index(child_index) >= 0

    def __left_child(self,parent_index:int)->int:

        return self.nodes[self.__get_left_child_index(parent_index)] if self.__has_left_child(parent_index)  else None

    def __right_child(self,parent_index:int)->int:
        return self.nodes[self.__get_right_child_index(parent_index)] if self.__has_right_child(parent_index) else None

    def __parent(self,child_index:int) -> int:
        return self.nodes[self.__get_parent_index(child_index)] if self.__has_parent(child_index) else None

    def swap(self,index_one:int,index_two:int)->int:
        self.nodes[index_one],self.nodes[index_two] = self.nodes[index_two],self.nodes[index_one]


    # method to rearrange the nodes after new element is inserted into heap
    def __heapify_up(self,child_index:Optional[int]=None):
        if not child_index:
            # if child_index is not specified start with end of the tree
            child_index = len(self.nodes)-1

        parent_index = self.__get_parent_index(child_index)

        # compare the parent and child nodes and perform recursive call till root node
        if self.__has_parent(child_index) and self.nodes[child_index] < self.nodes[parent_index]:
            self.swap(child_index,parent_index) # swap the child and parent node positions

            # recursively call the __heapify_up method to rearrange until its accepts the min_heap condition
            self.__heapify_up(parent_index)

    # method to add a new node to heap
    def add_node(self,node):
        # appending the new element at end of heap
        self.nodes.append(node)
        # re-arranging the heap nodes
        self.__heapify_up()
        # print(self.nodes)


    def __heapify_down(self,parent_index:int = 0):
        if parent_index > len(self.nodes) or not self.__has_left_child(parent_index):
            return

        # finding the smallest child index
        smallest_child_index = self.__get_left_child_index(parent_index)
        # validate whether the right child is present and compare the right and left child values
        if self.__has_right_child(parent_index) and self.__left_child(parent_index) > self.__right_child(parent_index):
            smallest_child_index = self.__get_right_child_index(parent_index)

        # validate, swap and call recursive to follow till the end of the tree
        if self.nodes[parent_index] > self.nodes[smallest_child_index]:
            # swapping the parent and child nodes
            self.swap(parent_index,smallest_child_index)

            # re-arranging the nodes
            self.__heapify_down(smallest_child_index)

    # method to remove the Root node/ min value from the heap
    def poll(self)->Optional[int]:
        # removing the first node
        removed_node = self.nodes[0]

        # copying the last node to first
        self.nodes[0] = self.nodes[-1]

        # deleting the last node
        del self.nodes[-1]

        #re-arraging the tree
        self.__heapify_down()
        return removed_node

    # method to check if heap is empty or not
    def is_empty(self):
        return not self.nodes

    # method which returns the root node from heap
    def peek(self)-> int:
        if not self.is_empty():
            return  None
        return self.nodes[0]

    # method to perform heap sort


def heap_sort():
    data = [1, 10, 2, 5, 11, 6, 19]
    obj = Heap(data)
    sorted_data = []
    for _ in range(len(data)):
        sorted_data.append(obj.poll())
    return sorted_data

# main method
if __name__ == "__main__":
    print(heap_sort())