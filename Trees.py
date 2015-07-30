'''
Created on April 10, 2015

@author: SUV
'''
class BSTNode(object):
    
    def __init__(self, key, value, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        
class BST(object):
    
    def __init__(self):
        self.root = None
        
    def find_node(self, node, key):
        if None == node or key == node.key:
            return node
        elif key<node.key:
            return self.find_node(node.left, key)
        else:
            return self.find_node(node.right, key)
        
    def insert(self, key, value):
        if None == self.root:
            self.root = BSTNode(key, value)
            return True
        
        current_node = self.root
        
        while current_node:
            if key == current_node.key:
                print 'The key does exist!!'
            
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key, value, current_node)
                    return True
            
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(key, value, current_node)
                    return True
                
    def replace_node(self, node, new_node):
        if node == self.root:
            self.root = new_node
            return
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print 'Incorrect parent-child relationship!'
            raise RuntimeError
        
    def remove_node(self, node):
        if node.left and node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.value = successor.value
            self.remove_node(successor)
        elif node.left:
            self.replace_node(node, node.left)
        elif node.right:
            self.replace_node(node, node.right)
        else:
            self.replace_node(node, None)
            
    def delete(self, key):
        node = self.search(key)
        if node:
            self.remove_node(node)
            
    def traverse(self, node):
        if node is None:
            return
        self.traverse(node.left)
        print node.value
        self.traverse(node.right)
        
            
tree = BST()

items = range(100000)

import random

random.shuffle(items)

for item in items:
    tree.insert(item, item)

#tree.insert(13,13)
#tree.insert(2,2)
#tree.insert(14,14)
#tree.insert(1,1)
#tree.insert(4,4)
#tree.insert(18,18)

tree.traverse(tree.root)