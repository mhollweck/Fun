'''
Created on 23.11.2014

@author: Maria Hollweck
'''
class Node:
    data = None
    right = None
    left = None
    
    def __init__(self, data):
        self.data = data
    
    def setRight(self, node):
        self.right = Node(node)
        
    def setLeft(self, node):
        self.left = Node(node)
        
    def getValue(self):
        return self.data
    
    
class BinarySearchTree:
    #Unbalanced Binary Search Tree
    top = None
    
    def __init__(self, data):
        self.top = Node(data)
        
    
    def addNode(self, data, head = None):
        #add a new node recursively 
        
        #unvalid input
        if head == None:
            head = self.top
            
        
        #no tree existing yet
        if head == None:
            head = Node(data)
            return
            
        if data < head.getValue():
            #Do add left
            if head.left == None:
                head.setLeft(data)
            else:
                self.addNode(data, head.left)
        else:
            #do add right
            if head.right == None:
                head.setRight(data)
            else:
                self.addNode(data, head.right)
                         
    def removeFromTree(self, parent):
        #we assume that the we are deleting the parent node
        
        child = parent.left
        grand = child.right
        
        if grand:
            while grand.right:
                child = grand
                grand = child.right
            self.value = grand.getValue()
            child.right = grand.left
        else:
            self.left = child.left
            self.value = child.value
    
    
    def inorder(self, node):
        #BASE CASE 
        if node is not None:
            #---A---
            #-B---C-
            # B A C
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            #---A---
            #-B---C-
            #-> A B C
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data
            
    def isBalanced(self, node):
        #slow solution -> better use the "isBalancedFast" Solution
        if node is None:
            return True
        
        difference = self.getHeight(node.left) - self.getHeight(node.right)
        if abs(difference) > 1:
            return False
        else:
            return True
        
    def getHeight(self, node):
        if node is None:
            return 0
        
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
    
    def isBalancedFast(self, node):
        if self.checkHeight(node) == -1:
            return False
        else:
            return True
            
    def checkHeight(self, node):
        if node is None:
            return 0
        
        #check if left tree is balanced
        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        
        #check if right tree is balanced
        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1
        
        #check if current node is balanced
        difference = leftHeight - rightHeight
        if abs(difference) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1
        
        
    
def main():
    b = BinarySearchTree(5)
    b.addNode(1)
    b.addNode(3)
    b.addNode(4)
    #b.addNode(3)
    #b.postorder(b.top)
    print b.isBalancedFast(b.top)
    
    

if __name__ == '__main__':
    main()
