
from collections import deque

class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        
    def insert(self, d):
        # This is when we don't allow duplicates, here we are allowing
        # if we do not want to allow the duplicates
        # just uncomment first two line and instead of < lt use <= lteq afterwards.
        
        #if self.data == d:
        #    return False
        # This is done to make pretty print work, 
        if d == None:
            return
        
        if d <= self.data:
            if self.left:
                self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    
    def preorder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preorder(l)
        return l
            
    def postorder(self, l):
        if self.left:
            self.left.postorder(l)
        if self.right:
            self.right.postorder(l)
        l.append(self.data)
        return l
    
    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.data)
        if self.right:
            self.right.inorder(l)
        return l
    
    def levelorder(self, l, queue = deque()):
        l.append(self.data)
        [queue.append(node) for node in [self.left, self.right] if node]
        if queue:
            queue.popleft().levelorder(l, queue)
        return l
            
    def levelorder2(self, l, head, queue = deque()):
        if head is None:
            return l
        l.append(head.data)
        [queue.append(node) for node in [head.left, head.right] if node]
        if queue:
            self.levelorder2(l, queue.popleft(), queue)
        return l
        
    
class BST(object):
    
    def __init__(self):
        self.root = None
    
    # For now it will return true for all the values since we are allowind duplicates
    def insert(self, d):
        
        # This is done to make pretty print work, 
        if d == None:
            return
        
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
    
    def preorder(self):
        if self.root:
            return self.root.preorder([])
        else:
            return []
        
    
    def postorder(self):
        if self.root:
            return self.root.postorder([])
        else:
            return []
    
    
    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []
        
    def levelorder(self):
        if self.root:
            return self.root.levelorder([])
        else:
            return []
        
    