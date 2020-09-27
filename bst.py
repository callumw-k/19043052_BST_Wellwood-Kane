# _bstSearchRange is the function that searches through the range, and _valueofRange is the function that returns the values from the search function.


class BSTMap:
    def __init__(self):
        self._root = None
        self._size = 0
        self.node_range = []

    def add(self, key, value):
        node = self._bstSearch(self._root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    def _bstInsert(self, subtree, key, value):
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Invalid map key."
        return node.value

    def _bstSearch(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right, target)
        else:
            return subtree

    def valuesOf(self, min, max):
        self.node_list = []
        self._bstSearchList(self._root, min, max)
        return self.node_list


    def _bstSearchList(self, subtree, min, max):
        if min > max:
            return
        if subtree is None:
            self._bstSearchList(self._root, (min + 1), max)
        elif min < subtree.key:
            return self._bstSearchList(subtree.left, min, max)
        elif min > subtree.key:
            return self._bstSearchList(subtree.right, min, max)
        else:
            self.node_list.append(subtree.value)
            return self._bstSearchList(self._root, (min + 1), max)






class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None




