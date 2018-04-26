from AbstractDecisionFunctionStrategy import AbstractDecisionFunctionStrategy

class PlainTextDecisionFunctionStrategy(AbstractDecisionFunctionStrategy):
    def __init__(self, decisionTreeHandler, functionName, inputs = None, classes = None):
        super(PlainTextDecisionFunctionStrategy, self).__init__(decisionTreeHandler, functionName)
        self.tab_count = 0
        self.inputs = inputs
        self.classes = classes

        if inputs is None:
            self.function_variables = "x"
            self.input_label = lambda i: "x[{}]".format(i)

        else:
            self.function_variables = ", ".join(inputs)
            self.input_label = lambda i: inputs[i]

        if classes is None:
            self.class_label = lambda i: "{0}".format(i)
        else:
            self.class_label = lambda i: classes[i]

    def get_tab_string(self):
        return "" # self.tab_count * "    "

    def get_input_variable(self, group_index):
        return self.input_label(group_index)

    def get_output_variable(self, output_index):
        return self.class_label(output_index)

    def express_tree_conditional_block_start(self, treeNode):
        block = "{0}if {1} is less than {2}\n".format(self.get_tab_string(), self.get_input_variable(treeNode.group), treeNode.threshold)
        self.tab_count +=1

        return block

    def express_tree_conditional_block_end(self, treeNode):
        self.tab_count += 1
        block = "{0}otherwise\n".format(self.get_tab_string())
        self.tab_count -=1
        return block

    def express_tree_leaf_start(self, treeLeaf):
        block = "{0}Classify it as {1}\n".format(self.get_tab_string(), self.get_output_variable(treeLeaf.group))
        self.tab_count -=1
        return block

    def express_tree_leaf_end(self, treeLeaf):
        return "\n"

    def express_function_header(self):
        return "Given some inputs {0} how do they classify to outputs {1}.\n".format(self.inputs if not None else "in array x", self.classes if not None else "as class indexes")

