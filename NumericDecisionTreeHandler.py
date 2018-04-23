
class NumericDecisionTreeHandler(object):
    """
    Handling data structure for the decision tree created from a numeric dataset.
    """
    
    def __init__(self, root):
        """
        Constructor. 
        :param root: Root of decision tree
        """
        self.root = root

    def two_part_inorder_traversal(self, start_visit, end_visit):
        self._two_part_inorder_recurse(self.root, start_visit, end_visit)

    def inorder_traversal(self, visit):
        """
        Performs an inorder traversal of the graph, applying visit at each node.
        :param visit: function that takes in a NumericDecisionTreeNode with the return value ignored.
        """
        self._inorder_recurse(self.root, visit)

    def postorder_traversal(self, visit):
        """
        Performs an postorder traversal of the graph, applying visit at each node.
        :param visit: function that takes in a NumericDecisionTreeNode with the return value ignored.
        """
        self._postorder_recurse(self.root, visit)

    def preorder_traversal(self, visit):
        """
        Performs an preorder traversal of the graph, applying visit at each node.
        :param visit: function that takes in a NumericDecisionTreeNode with the return value ignored.
        """
        self._preorder_recurse(self.root, visit)

    """
    Recursive inner functions for the in, post and preoder traversals. 
    """
    def _inorder_recurse(self, node, visit):
        visit(node)
        if not node.is_leaf():
            self._inorder_recurse(node.children[0], visit)
            self._inorder_recurse(node.children[1], visit)

    def _two_part_inorder_recurse(self, node, start_visit, end_visit):
        start_visit(node)
        if not node.is_leaf():
            self._two_part_inorder_recurse(node.children[0], start_visit, end_visit)
            end_visit(node)
            self._two_part_inorder_recurse(node.children[1], start_visit, end_visit)
        else:
            end_visit(node)

    def _postorder_recurse(self, node, visit):
        if not node.is_leaf():
            self._inorder_recurse(node.children[0], visit)
            self._inorder_recurse(node.children[1], visit)
        visit(node)

    def _preorder_recurse(self, node, visit):
        if not node.is_leaf():
            self._inorder_recurse(node.children[0], visit)
            visit(node)
            self._inorder_recurse(node.children[1], visit)
        else:
            visit(node)