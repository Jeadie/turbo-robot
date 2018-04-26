from AbstractDecisionFunctionStrategy import AbstractDecisionFunctionStrategy

class PythonDecisionFunctionStrategy(AbstractDecisionFunctionStrategy):
    def __init__(self, decisionTreeHandler, functionName, inputs = None, classes = None):
        super(PythonDecisionFunctionStrategy, self).__init__(decisionTreeHandler, functionName)
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
        return self.tab_count * "    "

    def get_input_variable(self, group_index):
        return self.input_label(group_index)

    def get_output_variable(self, output_index):
        return self.class_label(output_index)

    def express_tree_conditional_block_start(self, treeNode):
        block = "{0}if {1} <= {2}:\n".format(self.get_tab_string(), self.get_input_variable(treeNode.group), treeNode.threshold)
        self.tab_count +=1
        return block

    def express_tree_conditional_block_end(self, treeNode):
        self.tab_count -=1
        return ""

    def express_tree_leaf_start(self, treeLeaf):
        return "{0}return {1}\n".format(self.get_tab_string(), self.get_output_variable(treeLeaf.group))

    def express_tree_leaf_end(self, treeLeaf):
        return ""

    def express_function_header(self):
        self.tab_count += 1
        return "def {0}({1}):\n\t{2}\n".format(self.functionName, self.function_variables, self.get_function_docstring())

    def get_function_docstring(self):
        segments = ['"""']
        if self.inputs is not None:
            segments.append(
                "\n\t".join([":param {0}:".format(_class) for _class in self.inputs])
                )
        else:
            segments.append(":param x: a input array of appropriate dimension.")
        if self.classes is not None:
            segments.append(":return: a class label of possible outcome: {0}".format(", ".join(self.classes)))
        else:
            segments.append(":return: an index indicating the output class.")
        segments.append('"""')
        return "\n\t".join(segments)