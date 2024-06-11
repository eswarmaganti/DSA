from typing import List
import sys
import traceback


class BinarySearchTree:

    def __init__(self, value: int = None) -> None:
        self.value = value
        self.left = None
        self.right = None

    # method to check the node is empty or not
    def is_empty_node(self) -> bool:
        return self.right is None and self.left is None and self.value is None

    # method to check whether the node is left or not
    def is_leaf_node(self) -> bool:
        if self.left is None and self.right is None:
            return True
        else:
            return False
        
    # method to insert new node in BST
    def insert_node(self,value):
        # if it's a empty node, create a node
        if self.value is None:
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

        # value is greater than current node value, recursively traverse right subtree and insert
        elif self.value > value:
            self.left.insert_node(value)

        # value is less than the current node value, recursively traverse the left subtree and insert
        else:
            self.right.insert_node(value)

    # method to traverse the right subtree and get the minimum node
    def traverse_right_subtree(self) -> object:
        if self.left.is_empty_node():
            return self
        else:
            return self.left.traverse_right_subtree()
        
    # method to delete a node
    def delete_node(self,key: int) -> None:
        if self.is_empty_node(): # check for empty node, if it is return
            return

        # if key is greater than current node value, recursively traverse right subtree
        elif key > self.value:
            self.right.delete_node(key)

        # if key is less than the current node value, recursively traverse left subtree
        elif key < self.value:
            self.left.delete_node(key)

        # if key is found, delete the node
        else:

            # delete the node if it's leaf
            if self.is_leaf_node():
                self.value = None
                self.right = None
                self.left = None

            # delete the node and replace with right child if it doesn't have left child
            elif self.left.is_empty_node():
                self.value = self.right.value
                self.right = self.right.right
                self.left = self.right.left

            # delete the node and replace with left child if it doesn't have right child
            elif self.right.is_empty_node():
                self.value = self.left.value()
                self.right = self.left.right
                self.left = self.left.left

            # traverse and find the minimum node in right subtree of key is found and replace it with that node
            else:
                # get the node with minimum value in right subtree
                min_val_node = self.right.traverse_right_subtree()
                print(f"Min Value in Right Sub Tree: {min_val_node.value}")
                # update the node to be deleted 
                self.value = min_val_node.value

                # delete the min value node
                min_val_node.value = None
                min_val_node.left = None
                min_val_node.right = None
                
    # method to print the inorder traversal
    def inorder_traversal(self):
        if self.value is None:
            return []
        else:
            return self.left.inorder_traversal()+[self.value]+self.right.inorder_traversal()
    
    # method to traverse preorder traversal
    def preorder_traversal(self):
        if self.value is None:
            return []
        else:
            return [self.value]+ self.left.preorder_traversal()+ self.right.preorder_traversal()

    # method to traverse postorder traversal    
    def postorder_traversal(self):
        if self.value is None:
            return []
        else:
            return self.left.postorder_traversal() + self.right.postorder_traversal() + [self.value]


# main function
if __name__ == "__main__":
    try:
        bst = BinarySearchTree()
        elements = list(map(int, input("Enter elements as comma seperated values: ").split(",")))
        for element in elements:
            bst.insert_node(element)
        
        print("The In-Oder Traversal : ",bst.inorder_traversal())
        print("The Pre-Order Traversal: ",bst.preorder_traversal())
        print("The Post-Order Traversal: ",bst.postorder_traversal())

        bst.delete_node(5)
        print(f"The In_Order Traversal after deletion: {bst.inorder_traversal()}")

    except Exception as e:
        print(f"*** Error: Runtime Exception occured: {str(e)} ***")
        traceback.print_exc()