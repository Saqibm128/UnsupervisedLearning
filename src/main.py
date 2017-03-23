import sklearn.decomposition;
from matplotlib import pyplot as plt;
import numpy;
import scipy.cluster.vq;
from numpy import genfromtxt;

#This is where one would choose the dataset to analyze
dataSet = genfromtxt('../data/NHanesDataWColumns.csv',delimiter=',');
for i in range(3, len(dataSet) / 10):
    kmeans = kmeans(dataSet, i);
    print("K-Means, K = " + i);
    print(kmeans);
