import sklearn.mixture;
import sklearn.decomposition;
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
#@return a list of iteration results
#   more specifically, each iteration is the mean, followed by distortion/error measure
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
#@return GMO, GaussianMixtureObject
#get means with GMO.means_
def expectationMax(dataSet, numGaussianComps):
    GMO = sklearn.mixture.GaussianMixture(n_components = numGaussianComps);
    GMO.fit(dataSet);
    print("Means for " + str(numGaussianComps) + "Expectation Maximization (Gaussian)");
    print(GMO.means_);
    return GMO.means_;

#@return PCA object fitted to data
#get components_ for fun stuff
def PCAResults(dataSet):
    PCAObject = sklearn.decomposition.PCA();
    PCAObject.fit(dataSet);
    print(PCAObject.components_);
    return PCAObject;

#@return ICA object fitted to data
#get components_ for fun stuff
def ICAResults(dataSet):
    ICAObject = sklearn.decomposition.FastICA();
    ICAObject.fit(dataSet);
    print(ICAObject.components_);
    return ICAObject.components_;
