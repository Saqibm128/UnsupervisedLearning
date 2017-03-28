import functions as uLearn;
import transformDataset as tr;
from numpy import genfromtxt;
import matplotlib.pyplot as plt;
import numpy as np;

numRandRestarts = 3;
numK = 3;
numGaussianComps = 3;

#This is where one would choose the dataset to analyze
dataSet = genfromtxt('../data/NHanesDataWColumns.csv',delimiter=',');
#uLearn.kMeansMultipleK(dataSet, 50);
# print(uLearn.kMeansMultipleK(dataSet, 5));
# uLearn.kMeansMultipleK(dataSet, 50);
# dim2 = dataSet.shape[1]; #get the num columns
# resultsForTransform = list();
# for i in range(0, dim2):
#     transformedDataSet = tr.transformExponential(dataSet, i, 2);
#     res = uLearn.kMeansMultipleK(transformedDataSet, 4, graph = False);
#     untransformedResult = tr.unTransformExponential(res[0], i, 2);
#     distortions = uLearn.findDistortions(dataSet, untransformedResult);
#     distortions = np.average(distortions);
#     resultsForTransform.append(distortions);
# plt.plot(range(0, dim2), resultsForTransform);
# plt.xlabel("Transformed Dimension Index");
# plt.ylabel("Average Distortion");
# plt.title("Using Transformed Data for KMeans Analysis");
# plt.show();
