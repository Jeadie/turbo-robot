from sklearn.datasets import load_iris

from JavaScriptDecisionFunctionStrategy import JavaScriptDecisionFunctionStrategy
from NumericClassifyingDecisionTree import NumericClassifyingDecisionTree
from PlainTextDecisionFunctionStrategy import PlainTextDecisionFunctionStrategy
from PythonDecisionFunctionStrategy import PythonDecisionFunctionStrategy


class TurboRobotAPI(object):
    DEFAULT_PYTHON_NAME = "turbo_robot_python_function"
    DEFAULT_PLAINTEXT_NAME = "To classify the data: "
    DEFAULT_JAVASCRIPT_NAME = "turboRobotJavascriptFunction"

    @staticmethod
    def generate_python_function(data, outputs, name=None, labels=None, classes=None):
        classifier = NumericClassifyingDecisionTree(data, outputs)
        handler = classifier.get_decision_flow()
        if (labels is not None and max(classifier.features) +1 != len(labels)):
            print("Dimensions of labels must match the number of features in data. The number of features in data is the number of columns in the matrix.")
            labels=None

        return PythonDecisionFunctionStrategy(handler, name if name is not None else TurboRobotAPI.DEFAULT_PYTHON_NAME, inputs=labels, classes=classes).construct_function()

    @staticmethod
    def generate_plaintext_function(data, outputs, name=None, labels=None, classes=None):
        classifier = NumericClassifyingDecisionTree(data, outputs)
        handler = classifier.get_decision_flow()
        if (labels is not None and max(classifier.features) +1 != len(labels)):
            print("Dimensions of labels must match the number of features in data. The number of features in data is the number of columns in the matrix.")
            labels=None

        return PlainTextDecisionFunctionStrategy(handler, name if name is not None else TurboRobotAPI.DEFAULT_PLAINTEXT_NAME, inputs=labels, classes=classes).construct_function()

    @staticmethod
    def generate_javascript_function(data, outputs, name=None, labels=None, classes=None):
        classifier = NumericClassifyingDecisionTree(data, outputs)
        handler = classifier.get_decision_flow()
        if (labels is not None and max(classifier.features) +1 != len(labels)):
            print("Dimensions of labels must match the number of features in data. The number of features in data is the number of columns in the matrix.")
            labels=None

        return JavaScriptDecisionFunctionStrategy(handler, name if name is not None else TurboRobotAPI.DEFAULT_JAVASCRIPT_NAME, inputs=labels, classes=classes).construct_function()


if __name__ == '__main__':
    iris = load_iris()
    # print(TurboRobotAPI.generate_python_function(iris.data, iris.target))
    # print(TurboRobotAPI.generate_python_function(iris.data, iris.target, name = "Iris_data_classifier"))
    # print(TurboRobotAPI.generate_python_function(iris.data, iris.target, name="iris_data_classifier",
    #                                             classes=["'Iris setosa'", "'Iris virginica'", "'Iris versicolor'"],
    #                                             labels=["petalLength", 'petalWidth', 'sepalLength', 'sepalWidth']))

    print(TurboRobotAPI.generate_javascript_function(iris.data, iris.target, name="iris_data_classifier",
                                                 classes=["'Iris setosa'", "'Iris virginica'", "'Iris versicolor'"],
                                                 labels=["petalLength", 'petalWidth', 'sepalLength', 'sepalWidth']))