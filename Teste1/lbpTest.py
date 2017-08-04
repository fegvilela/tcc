#########################
########## Utiliza o histograma do LBP para treinar máquina
########## utilizando Linear Support Vector Machine
########################



# import the necessary packages
from localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from converteImagem import convertImage
#from imutils import paths
#import paths #imutils module
#import argparse
import cv2
import os
import glob
import numpy as np



trainingPath = "/Users/fegvilela/Documents/Unb/TCC/baseDados/training1/"
testingPath = "/Users/fegvilela/Documents/Unb/TCC/baseDados/testing1/"


pngFiles1 = convertImage(trainingPath)


# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(30, 5) # LBP 30 pontos e raio 9 = melhor acurácia
data = []
labels = []
trueClass = []
predClass = []

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

# train a Linear SVM on the data
model = LinearSVC(C = 100.0, random_state = 42)
model.fit(data, labels)

pngFiles2 = convertImage(testingPath)

file1 = open("pred.txt", "w")
file2 = open("true.txt", "w")


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

#print(trueClass.shape)
#print(predClass.shape)


# cria a matriz de confusão para análise de resultados
#confMatrix = confusion_matrix(trueClass, predClass, labels = ["helvetica", "garamond"])
#print(confMatrix)

#with open("confusionMatrix.txt", "w") as f:
#    f.write(confMatrix)

### final command on terminal: $ python recognize.py --training images/training --testing images/testing


