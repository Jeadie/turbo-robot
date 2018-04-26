# turbo-robot
Using decision tree classifiers for automated code generation and other conditional formats

## About
The aim of this project is to use classifying decision trees to automate code generation of classifying functions in a variety of languages and other formats such as plain, readable text. 

## Example
The following generates python code from the well known iris dataset. 

``` python3
from sklearn.datasets import load_iris
from 

iris = load_iris()
default_options = TurboRobotAPI.generate_python_function(iris.data, iris.target)

# Gives output
def turbo_robot_python_function(x):
    """
    :param x: a input array of appropriate dimension.
    :return: an index indicating the output class.
    """
    if x[3] <= 0.800000011920929:
        return 0
    if x[3] <= 1.75:
        if x[2] <= 4.949999809265137:
            if x[3] <= 1.6500000953674316:
                return 1
            return 2
        if x[3] <= 1.5499999523162842:
            return 2
        if x[2] <= 5.449999809265137:
            return 1
        return 2
    if x[2] <= 4.850000381469727:
        if x[1] <= 3.0999999046325684:
            return 2
        return 1
    return 2
``` 

To add custom input parameters, output parameters and function names, simply include the kwargs. 

```python
custom_options = TurboRobotAPI.generate_python_function(iris.data, iris.target, name="iris_data_classifier", 
                                            classes=["'Iris setosa'", "'Iris virginica'", "'Iris versicolor'"],
                                            labels=["petalLength", 'petalWidth', 'sepalLength', 'sepalWidth']))

# Gives output   
def iris_data_classifier(petalLength, petalWidth, sepalLength, sepalWidth):
    """
    :param petalLength:
    :param petalWidth:
    :param sepalLength:
    :param sepalWidth:
    :return: a class label of possible outcome: 'Iris setosa', 'Iris virginica', 'Iris versicolor'
    """
    if sepalLength <= 2.450000047683716:
        return 'Iris setosa'
    if sepalWidth <= 1.75:
        if sepalLength <= 4.949999809265137:
            if sepalWidth <= 1.6500000953674316:
                return 'Iris virginica'
            return 'Iris versicolor'
        if sepalWidth <= 1.5499999523162842:
            return 'Iris versicolor'
        if sepalLength <= 5.449999809265137:
            return 'Iris virginica'
        return 'Iris versicolor'
    if sepalLength <= 4.850000381469727:
        if petalLength <= 5.949999809265137:
            return 'Iris virginica'
        return 'Iris versicolor'
    return 'Iris versicolor'
```
