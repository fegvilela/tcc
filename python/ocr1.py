############################
######### NAO FINALIZADO!!! -> provavelmente, não irei treinar a máquina para ######### OCR (já usar código pronto)
################################
######### Início de código para treinar máquina para OCR
######### Reconhece local da letra na imagem, desenha retangulo em volta e     ######### já extrai features
#############################



import sys
import numpy as np
import cv2
import os
from PIL import Image
import glob

#C,E,F,G,H,I,J,K,L,M,N,S,T,U,V,W,X,Y,Z = 0| A,D,O,P,Q,R = 1 | B=2
#muda de diretorio
os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/Maiusculas/A/")


#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos gif em png
gifFiles = glob.glob("*.gif")
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif


#salva o nome de todos arquivos do diretorio em "filenames"
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        os.path.join(dirname, subdirname)
    # percorre todos os arquivos no diretório, remove DS_Store
    for filename in filenames:
        if filename == '.DS_Store':
            filenames.remove('.DS_Store')



print(filenames) #quantidade de arquivos na pasta
#im = cv2.imread(filenames[0])
#cv2.namedWindow("Original")
#cv2.imshow("Original", im)
#cv2.waitKey(0)

file1 = open("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/generalsamples.txt", "a")
file2 = open("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/generallabel.txt", "a")

#aplica a todas imagens da pasta
for i in range(0,len(filenames)):
    im = cv2.imread(filenames[i])
    #im3 = im.copy() #faz cópia de imagem
    #output original image
    cv2.namedWindow("Original")
    cv2.imshow("Original", im)
    cv2.waitKey(0)

    #grayscale e blur
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    #output image na mesma janela grayscale e blur
    out1 = np.hstack([gray, blur])
    cv2.imshow("Out1", out1)
    cv2.waitKey(0)

    #binarização inversa e output image
    _,thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)
    #thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    cv2.namedWindow("Thresh")
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)
    #If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.
    #print(thresh.shape)
    #print(thresh.dtype)

    #################      Now finding Contours         ###################
    #Finds contours in a binary image.
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    #print(len(contours))
    cv2.drawContours(im, contours, -1, (0,255,0), 3) #contorno dos objetos (espera-se que seja a letra principal)
    cv2.imshow(str(filenames[i]), im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)



    samples =  np.empty((0,100))
    responses = []
    #keys = [i for i in range(48,58)]

    #if cv2.contourArea(contours)>50:
    #C,E,F,G,H,I,J,K,L,M,N,S,T,U,V,W,X,Y,Z = 0| A,D,O,P,Q,R = 1 | B=2
    [x,y,w,h] = cv2.boundingRect(contours[1])
    print(x)
    print(y)
    print(w)
    print(h)
    #if  h>28:
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
    roi = thresh[y:y+h,x:x+w]
    roismall = cv2.resize(roi,(10,10))
    cv2.imshow('norm',im)
    key = cv2.waitKey(0)

    #if key == 27:  # (escape to quit)
    #    sys.exit()
    #elif key in keys:
    responses.append('A_Ma')
    sample = roismall.reshape((1,100))
    #cv2.imshow('reshape',roismall)
    #key = cv2.waitKey(0)
    samples = np.append(samples,sample,0)

    #responses = np.array(responses,np.float32)
    #responses = responses.reshape((responses.size,1))
    print("training complete")
    #print(samples)
    file1.seek(0)
    file1.write(str(sample).strip() + "\n")
    file2.seek(0)
    file2.write(str(responses).strip() + "\n")
    #np.savetxt('generalsamples.txt',samples)
    #np.savetxt('generalresponses.txt',responses)
file1.close()
file2.close()

'''
#########################################
#######PARTES SEM USO POR ENQUANTO#########
#########################################

RGB_gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
RGB_blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
plt.subplot(221),plt.imshow(RGB_gray), plt.title('gray')
plt.subplot(223),plt.imshow(RGB_blur), plt.title('blur')

RGB_thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
plt.subplot(122),plt.imshow(RGB_thresh), plt.title('thresh')
#plt.subplot(123),plt.imshow(thresh), plt.title('thresh')
plt.show()



#####APARECEM MANCHAS PRETAS DENTRO DA LETRA (MELHOR USAR THRESHOLD)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
cv2.namedWindow("Thresh")
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)



'''

