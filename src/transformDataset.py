import numpy as np;

def transformExponential(dataSet, index, exponent):
    transformedDataSet = np.array(dataSet);
    dim1 = transformedDataSet.shape[0];
    for i in range(0, dim1):
        transformedDataSet[i][index] = transformedDataSet[i][index] ** exponent;
    return transformedDataSet;

def unTransformExponential(dataSet, index, exponent):
    transformedDataSet = np.array(dataSet);
    dim1 = transformedDataSet.shape[0];
    for i in range(0, dim1):
        transformedDataSet[i][index] = transformedDataSet[i][index] ** (1/exponent);
    return transformedDataSet;
