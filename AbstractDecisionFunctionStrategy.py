

class AbstractDecisionFunctionStrategy(object):

    def __init__(self, decisionTreeHandler, functionName):
        self.treeHandler = decisionTreeHandler
        self.functionStringBuilder = []
        self.functionName = functionName

    # Public Methods to override
    def express_tree_conditional_block_start(self, treeNode):
        return ""

    def express_tree_conditional_block_end(self, treeNode):
        return ""

    def express_tree_leaf_start(self, treeLeaf):
        return ""

    def express_tree_leaf_end(self, treeLeaf):
        return ""

    def express_function_header(self):
        return ""

    def express_function_end(self):
        return ""

    # Public Template Method. Can be called, but do not override
    def construct_function(self):
        self.functionStringBuilder.append(self.express_function_header())
        self.treeHandler.two_part_inorder_traversal(self.start_visit_wrapper, self.end_visit_wrapper)
        self.functionStringBuilder.append(self.express_function_end())
        return "".join(self.functionStringBuilder)

    # Private template Methods. Do not override
    def start_visit_wrapper(self, node):
        if node.is_leaf():
            self.functionStringBuilder.append(self.express_tree_leaf_start(node))
        else:
            self.functionStringBuilder.append(self.express_tree_conditional_block_start(node))

    def end_visit_wrapper(self, node):
        if node.is_leaf():
            self.functionStringBuilder.append(self.express_tree_leaf_end(node))
        else:
            self.functionStringBuilder.append(self.express_tree_conditional_block_end(node))