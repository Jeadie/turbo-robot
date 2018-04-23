from sklearn.datasets import load_iris

from NumericClassifyingDecisionTree import NumericClassifyingDecisionTree
from PythonDecisionFunctionStrategy import PythonDecisionFunctionStrategy


class TurboRobotAPI(object):
    DEFAULT_PYTHON_NAME = "turbo_robot_python_function"


    @staticmethod
    def generate_python_function(data, outputs, name=None, labels=None):
        classifier = NumericClassifyingDecisionTree(data, outputs)
        handler = classifier.get_decision_flow()
        if (labels is not None and classifier.features != len(labels)):
            print("Dimensions of labels must match the number of features in data. The number of features in data is the number of columns in the matrix.")
            labels=None
        return PythonDecisionFunctionStrategy(handler, name if name is not None else TurboRobotAPI.DEFAULT_PYTHON_NAME).construct_function()



if __name__ == '__main__':
    iris = load_iris()
    print(TurboRobotAPI.generate_python_function(iris.data, iris.target))
    print(TurboRobotAPI.generate_python_function(iris.data, iris.target, name = "Iris_data_classifier"))