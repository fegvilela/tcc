#########################
########## Utiliza o histograma do LBP para treinar máquina
########## utilizando Linear Support Vector Machine
########################



# import the necessary packages
from localbinarypatterns2 import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from converteImagem2 import convertImage
from accuracyScore2 import accuracy
#from imutils import paths
#import paths #imutils module
#import argparse
import cv2
import os
import glob
import time
import numpy as np

start = time.time()

trainingPath = "/Users/fegvilela/Documents/Unb/TCC/baseDados/training2/"
testingPath = "/Users/fegvilela/Documents/Unb/TCC/baseDados/testing2/"


pngFiles1 = convertImage(trainingPath)


# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(30, 9) # LBP 30 pontos e raio 9 = melhor acurácia
data = []
labels = []
trueClass = []
predClass = []
accuracyList = []

# loop over the training images
for file in pngFiles1:
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # call from made lbp class/module = aplica LBP em imegem e retorna o histograma
    hist = desc.describe(gray)
    # extract the label from the image path (), then update the
    # label and data lists
    file = file.split(".")[0]
    labels.append(file.split("_")[-1])
    data.append(hist)


for ran in range(85,95,1):
    #for c in range(0, 401, 25):
        # train a Linear SVM on the data
        #if c == 0:
        #    model = LinearSVC(C = c + 1, random_state = ran)
        #else:
    model = LinearSVC(C = 300, random_state = ran)
    model.fit(data, labels)

    pngFiles2 = convertImage(testingPath)

    file1 = open("pred.txt", "w+")
    file2 = open("true.txt", "w+")


    # loop over the testing images
    for file in pngFiles2:
        # load the image, convert it to grayscale, describe it,
        # and classify it
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = desc.describe(gray)
        prediction = model.predict(hist)[0]

        # salva a classe prevista na lista predClass
        file1.write(prediction + "\n")
        #predClass.append(prediction)

        # salva a verdadeira classe da imagem na lista trueClass
        file = file.split(".")[0]
        #trueClass.append(file.split("_")[-1])
        file2.write(file.split("_")[-1] + "\n")
    '''
        # display the image and the prediction
        res = cv2.resize(image,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
        cv2.putText(res, prediction, (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1.0, (64, 76, 8), 2)
        cv2.imshow("Image", res)
        cv2.waitKey(0)
    '''

    file1.close()
    file2.close()

    # evaluate accuracy and saves on a list
    msg = ("C = " + str(300) + " rand = " + str(ran) +": " + accuracy() + "\n")
    accuracyList.append(msg)

# escreve a accuracyList on file
fileA = open("Accuracy.txt", "w")
for value in accuracyList:
    fileA.write(value)
fileA.close()

# evaluate accuracy and prints
print("accuracy: " + accuracy())

# print do tempo levado para treinar e testar a máquina
print('It took ' + str(time.time()-start) + ' seconds.')

#print(trueClass.shape)
#print(predClass.shape)


# cria a matriz de confusão para análise de resultados
#confMatrix = confusion_matrix(trueClass, predClass, labels = ["helvetica", "garamond"])
#print(confMatrix)

#with open("confusionMatrix.txt", "w") as f:
#    f.write(confMatrix)

### final command on terminal: $ python recognize.py --training images/training --testing images/testing

##################
###### ADITIONAL FEATURES
######  Transforma label string -> label integer
###### Use automatic split dataset
#3###############

'''
# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split


# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(
    np.array(data), labels, test_size=0.25, random_state=42)

# train the linear regression clasifier
print("[INFO] training Linear SVM classifier...")
model = LinearSVC()
model.fit(trainData, trainLabels)

# evaluate the classifier
print("[INFO] evaluating classifier...")
predictions = model.predict(testData)
print(classification_report(testLabels, predictions,
    target_names=le.classes_))


# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)

'''
