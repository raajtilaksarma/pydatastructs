from __future__ import print_function, division
from pydatastructs import DynamicOneDimensionalArray as DODA

__all__ = [
    'TreeNode'
]

_check_type = lambda a, t: isinstance(a, t)
NoneType = type(None)

class TreeNode(object):
    """
    Represents node in trees.

    Parameters
    ==========

    data
        Any valid data to be stored in the node.
    key
        Required for comparison operations.
    left: int
        Optional, index of the left child node.
    right: int
        Optional, index of the right child node.
    """

    __slots__ = ['key', 'data', 'left', 'right', 'is_root',
                 'height', 'parent', 'size']

    def __new__(cls, key, data):
        obj = object.__new__(cls)
        obj.data, obj.key = data, key
        obj.left, obj.right, obj.parent, obj.height, obj.size = \
            None, None, None, 0, 1
        obj.is_root = False
        return obj

    def __str__(self):
        """
        Used for printing.
        """
        return str((self.left, self.key, self.data, self.right))


class GraphNode(object):
    """
    Represents node in Graphs.

    Parameters
    ==========

    data
        Any valid data to be stored in the node.
    key
        Required for comparison operations.
    """

    __slots__ = ['key', 'data']

    def __new__(cls, key, data, adj_list = DODA(int,0)):
        obj = object.__new__(cls)
        obj.data, obj.key = data, key
        obj.adj_list = {'adjacent_nodes':adj_list}
        return obj

    def __str__(self):
        """
        Used for printing.
        """
        return str((self.key, self.data))

    def add_adjacent_key(self, key):
        """
        key : key of adjacent node to be appended to the adj_list of the node
        """
        self.adj_list['adjacent'].append(key)
        
    def remove_adjacent_key(self, key):
        """
        key : key of adjacent node to be removed from the adj_list of the node
        """
        self.adj_list['adjacent'].remove(key)