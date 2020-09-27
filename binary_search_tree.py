# Class to implement binary search tree ADT

class BST:
    def __init__( self ):
        self._root = None

    # add a (key, value) pair to the binary search tree
    def add( self, key, value ):
        node = self._bstSearch( self._root, key )
        if node is not None :
            node.value = value
            return False
        else :
            self._root = self._bstInsert(self._root, key, value )
            return True
     
    # recursive method to insert a (key, value) pair
    # takes the current "place in tree" as an extra argument
    def _bstInsert(self, subtree, key, value):
        if subtree is None :   
            subtree = _BSTNode(key, value)
        elif key < subtree.key :
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key :
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    # recursive method to search for a key 
    # takes the current "place in tree" as an extra argument
    def _bstSearch( self, subtree, target ): 
        if subtree is None :        
            return None
        elif target < subtree.key :  
            return self._bstSearch( subtree.left, target )
        elif target > subtree.key : 
            return self._bstSearch( subtree.right, target )       
        else :                    
            return subtree

    # return number of items in the binary search tree
    def count(self):
        return self._bstSize(self._root)
        
    # recursive method to count nodes
    # takes the current "place in tree" as an extra argument
    def _bstSize(self, subtree):
        if subtree == None:
            return 0
        else:
            return self._bstSize(subtree.left) + self._bstSize(subtree.right) + 1
        
    # prune a binary search tree - remove every leaf node from the tree, making each branch "one shorter"
    # note that the following two methods don't produce a correct solution
    # they are left here to illustrate a line of thinking leading towards a correct solution
    def prune1(self):
        self._bstPrune(self._root)
    
    # recursive method that takes the current "place in tree" as an extra argument
    def _bstPrune(self, subtree):
        if subtree.left == None and subtree.right == None:
            print("pruning")
            subtree = None
            return
        else:
            if subtree.left != None:
                self._bstPrune(subtree.left)
            if subtree.right != None:
                self._bstPrune(subtree.right)
                   
    # prune a binary search tree - remove every leaf node from the tree, making each branch "one shorter"
    # this and the following two methods will produce a correct solution
    def prune(self):
        #print("pruning")
        if self._root == None:
            return
        if self._root.left == None and self._root.right == None:
            self._root = None
            return
        else:
            self._bstLPrune(self._root, self._root.left)
            self._bstRPrune(self._root, self._root.right)
    
    # two mutually recursive methods, each calls the other
    # both the current "place in tree" and its parent are required as arguments
    # need to know if current node is left or right child of the parent
    def _bstLPrune(self, parent, subtree):
        if subtree.left == None and subtree.right == None:
            #print("pruning")
            parent.left = None
            return
        else:
            if subtree.left != None:
                self._bstLPrune(subtree, subtree.left)
            if subtree.right != None:
                self._bstRPrune(subtree, subtree.right)
                
    def _bstRPrune(self, parent, subtree):
        if subtree.left == None and subtree.right == None:
            #print("pruning")
            parent.right = None
            return
        else:
            if subtree.left != None:
                self._bstLPrune(subtree, subtree.left)
            if subtree.right != None:
                self._bstRPrune(subtree, subtree.right)
                
    def printTI(self):
        self.printTreeIndented(self._root, 0) 
        
    def printTreeIndented(self, subtree, level):
        if subtree == None:
            return
        else:
            self.printTreeIndented(subtree.right, level+1) 
            print(" "*8*level + "(" + str(subtree.key) + str(subtree.value) + ")")
            self.printTreeIndented(subtree.left, level+1) 
          
    def show(self):
        self._bstShow(self._root)
        
    def _bstShow(self, subtree):
        if subtree == None:
            return
        else:
            print(subtree.key, subtree.value)
            self._bstShow(subtree.left)
            self._bstShow(subtree.right)
        
# Class to represent a single node in a binary search tree
class _BSTNode :                        
    def __init__( self, key, value ):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

bst = BST()
bst.add(6, "fff")
bst.add(2, "bbb")
bst.add(5, "eee")
bst.add(4, "ddd")
bst.add(7, "ggg")
bst.add(3, "ccc")
bst.add(1, "aaa")
print(bst.count())

bst.printTI()
bst.prune()
print
print(bst.count())
bst.printTI()
print

bst1 = BST()
bst1.add(1, "string")
bst1.printTI()
bst1.prune()
bst1.printTI()


