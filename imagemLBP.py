
from localbinarypatterns2 import LocalBinaryPatterns
from imageResize import imResize
from converteImagem2 import convertImage
import cv2
import os
from skimage import feature
import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py




imagesPath = "/Users/fegvilela/Desktop/enes/"

pngFiles = convertImage(imagesPath)

eps = 1e-7
numPoints = 9
radius = 21

#file = "/Users/fegvilela/Desktop/de704_clarendon.png"

for i in range(0,len(pngFiles)):
    image = cv2.imread(pngFiles[i])
    imageNew = imResize(image, 126)
    gray = cv2.cvtColor(imageNew, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 88, 255, cv2.THRESH_BINARY_INV)

    h, w,_ = imageNew.shape

    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)

    lbp = feature.local_binary_pattern(thresh, numPoints,
                radius, method = "uniform")


    lbp2 = cv2.normalize(lbp,0,200,cv2.NORM_MINMAX)


    (hist, _) = np.histogram(lbp.ravel(),
            bins=np.arange(0, numPoints + 3),
            range=(0, numPoints + 2))

    bins = 0,25,50,75,100,125,150,175,200,225,250,255
    # normalize the histogram
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    #for j in range(0,len(hist)):
    #    print(hist[j])

    cv2.imshow("LBP", lbp2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    #plt.bar(bins[:-1],hist,width=20)
    #plt.title("Histograma do LBP")
    #plt.xlabel("LBP")
    #plt.ylabel("Porcentagem de pixels")
    #plt.show()

'''
    plt.hist(lbp.ravel(), )
    plt.plot(hist)
    plt.title("Histograma do LBP")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.show()

    #py.iplot(hist, filename='basic histogram')


    #for j in range(0,len(lbp)):
    #    print(lbp2[j])

    #cv2.imwrite("/Users/fegvilela/Desktop/enes/" + str(i) + ".png",lbp)
    #lbp2 = cv2.normalize(lbp,255,0,cv2.NORM_MINMAX)

'''






