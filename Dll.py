'''
Created on April 10, 2015

@author: SUV
'''

class Node(object):
    
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoubleList(object):
    
    head = None
    tail = None
    
    def append(self, data):
        new_node = Node(data,None,None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self, node_value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == node_value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
                    
            current_node = current_node.next
            
    def show(self):
        print 'Show list data:'
        current_node = self.head
        while current_node is not None:
            print current_node.data,
            current_node = current_node.next
        
        print "\n"
        print "*"*50
        
d = DoubleList()

d.append(5)
d.append(10)
d.append(15)
d.append(20)
d.append(25)
d.append(30)

d.show()

d.remove(15)
d.remove(25)

d.show()    