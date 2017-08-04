#import this
import numpy as np
import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

#assignment
#
'''
frase = 'vai dar certo'
print(frase[2])
print(frase)
frase = frase + ' ok'
print(frase)


##########
myArray = numpy.array([[1,2,3],[4,5,6]])
rows = ['a', 'b']
col = ['um', 'dois', 'tres']
mydataFrame = pandas.DataFrame(myArray, index = rows, columns = col)
print(mydataFrame)
'''
#Loadcsv files using panda
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
names2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
name = ['class']
data = pandas.read_csv(url, names=names)

#escrevendo doc com data
f = open('filePimaIndians.txt', 'w')
f.write(str(data))
f.close()

#distribution and some data features
description = data.describe()
dataType = data.dtypes
firstElements = data.head()
correlation = data.corr()
f2 = open('dataAttributesPimaInd.txt', 'w')
f2.write("data shape: \n" + str(data.shape)) #data matrix dimension
f2.write("\n\ndescription: \n" + str(description))
f2.write("\n\nData Type: \n" + str(dataType))
f2.write("\n\n1st elements: \n" + str(firstElements))
f2.write("\n\ncorrelation: \n" + str(correlation))
f2.close()

#histogram and scatter plot matrix
data.hist()
plt.show()
scatter_matrix(data)
plt.show()

#lesson 6
#pre-processing data
array = data.values


# separate array into input and output components
X = pandas.DataFrame(array[:,0:8], columns = names2) #features
Y = pandas.DataFrame(array[:,8], columns = name) #class

#standardize data (0 mean, 1 stdev)
scaler = StandardScaler().fit(X)
Xrescaled = scaler.transform(X) #standardization scaler applied on features
Xrescaled = np.round(Xrescaled, decimals=3) #round for 3 decimals
Xrescaled = pandas.DataFrame(Xrescaled, columns = names2)

# summarize transformed data
f3 = open('dataPreprocessed.txt', 'w')
f3.write("original input\n" + str(X))
f3.write("\noriginal output\n" + str(Y))
f3.write("\nrescaled input\n" + str(Xrescaled))


# normalize data
 #fit does nothing the fit method is useless in this case: the class is stateless as this operation treats samples independently (???)
normalizer = Normalizer().fit(Xrescaled)
Xnormalized = normalizer.transform(Xrescaled) #normalizer applied on features
Xnormalized = pandas.DataFrame(np.round(Xnormalized, decimals=3), columns = names2)
f3.write("\nnormalized input\n" + str(Xnormalized))
f3.close()

#lesson 7
#split data  into subsets (resampling method): train and estimate accuracy
#evaluate using cross validation
Y2 = array[:,8]

kfold = KFold(n_splits = 10) #10-fold cross validation, without shuffling -> best result tested for kfold
model = LogisticRegression()
results = cross_val_score(model, Xrescaled, Y2, cv = kfold)
accuracyMean = np.round(results.mean()*100.0, decimals=3)
accuracyStd = np.round(results.std()*100.0, decimals=3)
print("accuracy: " + str(accuracyMean) + " std dev: " + str(accuracyStd))


