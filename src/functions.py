import sklearn.mixture;
import sklearn.decomposition;
from matplotlib import pyplot as plt;
import numpy;
import scipy.cluster.vq as vq;




#try to go through a few of the k means at a time
#@return a list of iteration results
#   more specifically, each iteration is the mean, followed by distortion/error measure
def kMeansMultipleK(dataSet, numK, fn = "KMeansDistortions", graph = True):
    allResults = list();
    allDistortions = list();
    kmeanResults = [];
    for i in range(1, numK):
        kmeanResults = vq.kmeans(dataSet, i);
        # print("Iteration " + str(i));
        # print("K-Means, K = " + str(numK));
        allDistortions.append([kmeanResults[1]]);
    if (graph):
        plt.plot(range(1, numK), allDistortions);
        plt.title("K over Distortion");
        plt.xlabel("K");
        plt.ylabel("Distortion");
        # print("Final Results for K-Means Algorithm");
        # print(kmeanResults);
        # plt.show();
        plt.savefig(fn);
    return kmeanResults;

def findDistortions(dataSet, clusters):
    results = vq.vq(dataSet, clusters);
    return results[1];


#look up docs here http://scikit-learn.org/stable/modules/mixture.html

#GMO = GaussianMixtureObject
#@return GMO, GaussianMixtureObject
#get means with GMO.means_
def expectationMax(dataSet, numGaussianComps):
    GMO = sklearn.mixture.GaussianMixture(n_components = numGaussianComps);
    GMO.fit(dataSet);
    # print("Means for " + str(numGaussianComps) + "Expectation Maximization (Gaussian)");
    # print(GMO.means_);
    return GMO.means_;

#@return PCA object fitted to data
#get components_ for fun stuff
def PCAResults(dataSet):
    PCAObject = sklearn.decomposition.PCA();
    PCAObject.fit(dataSet);
    # print(PCAObject.components_);
    return PCAObject;

#@return ICA object fitted to data
#get components_ for fun stuff
def ICAResults(dataSet):
    ICAObject = sklearn.decomposition.FastICA();
    ICAObject.fit(dataSet);
    # print(ICAObject.components_);
    return ICAObject.components_;
