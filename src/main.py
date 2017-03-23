import sklearn.mixture;
from matplotlib import pyplot as plt;
import numpy;
import scipy.cluster.vq as vq;
from numpy import genfromtxt;

numRandRestarts = 3;
numK = 3;
numGaussianComps = 3;

#This is where one would choose the dataset to analyze
dataSet = genfromtxt('../data/NHanesDataWColumns.csv',delimiter=',');

#try to go through a few of the k means at a time
#RANDOM RESTARTS! 3 of them
def kMeans(dataSet, numK, numRandRestarts):
    allResults = list();
    for i in range(0, numRandRestarts):
        kmeanResults = vq.kmeans(dataSet, numK);
        print("Iteration " + str(i));
        print("K-Means, K = " + str(numK));
        print(kmeansResults);
        allResults = allResults + kmeanResults;

#look up docs here http://scikit-learn.org/stable/modules/mixture.html

#GMO = GaussianMixtureObject
def expectationMax(dataSet, numGaussianComps):
    GMO = sklearn.mixture.GaussianMixture(n_components = numGaussianComps);
    GMO.fit(dataSet);
    print("Means for " + str(numGaussianComps) + "Expectation Maximization (Gaussian)");
    print(GMO.means_);
    return GMO.means_;
