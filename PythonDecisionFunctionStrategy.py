from AbstractDecisionFunctionStrategy import AbstractDecisionFunctionStrategy

class PythonDecisionFunctionStrategy(AbstractDecisionFunctionStrategy):
    def __init__(self, decisionTreeHandler, functionName):
        super(PythonDecisionFunctionStrategy, self).__init__(decisionTreeHandler, functionName)
        self.tab_count = 0

    def get_tab_string(self):
        return self.tab_count * "    "

    def express_tree_conditional_block_start(self, treeNode):
        block = "{0}if x[{1}] <= {2}:\n".format(self.get_tab_string(), treeNode.group, treeNode.threshold)
        self.tab_count +=1
        return block

    def express_tree_conditional_block_end(self, treeNode):
        self.tab_count -=1
        return ""

    def express_tree_leaf_start(self, treeLeaf):
        return "{0}return {1}\n".format(self.get_tab_string(), treeLeaf.group)

    def express_tree_leaf_end(self, treeLeaf):
        return ""

    def express_function_header(self):
        self.tab_count += 1
        return "def {0}(self, x):\n".format(self.functionName)