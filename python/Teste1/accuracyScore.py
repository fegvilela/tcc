#################
### Código mal feito, só para ver a acurácia da predição do primeiro treino da ### máquina (com lbp e linear svm)
### modifica o nome das imagens que foram classificadas errado
### PROB_<number>_<tipografia>
################


from sklearn.metrics import accuracy_score
import os
from converteImagem import convertImage

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/testing1/")

file1 = open("pred.txt", "r")
file2 = open("true.txt", "r")

pred = file1.readlines()
true = file2.readlines()

file1.close()
file2.close()

print(accuracy_score(true, pred))
print("\n")

#problem = []
#i = 0
#for i in range(0, len(pred)):
#    im1 = pred[i]
#    im2 = true[i]
#    if im1 != im2:
#        problem.append(str(i))

#print(problem)


#pngFiles = convertImage("/Users/fegvilela/Documents/Unb/TCC/baseDados/testing1/")

#for imChange in problem:
#    os.rename(pngFiles[int(imChange)], ("PROB_" + pngFiles[int(imChange)]))
