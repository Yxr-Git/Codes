from numpy import *
import operator

def creatDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0.1],[0,0.0]])
    labels = ['A','A','B','B']
    return group, labels

def classify_1(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diff = tile(inX, (dataSetSize,1)) - dataSet
    diffSquare = diff**2
    diffSum = diffSquare.sum(axis=1)
    distance = diffSum**0.5
    sortedIndices = distance.argsort()
    classCount = {}
    for i in range(k):
        elementLabel = labels[sortedIndices[i]]
        classCount[elementLabel] = classCount.get(elementLabel, 0) + 1
    sortedClass = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    print(sortedClass)
    return sortedClass[0][0]

    
    
