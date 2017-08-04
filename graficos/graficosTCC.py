import matplotlib.pyplot as plt
import numpy
import pylab


with open("SVM.txt", "r") as ins:
    SVM = []
    #lines = [line.rstrip('\n') for line in open("tempo(x).txt")]
    for line in ins:
        SVM = [x1.strip() for x1 in SVM]
        SVM.append(line)
    SVM[-1] = SVM[-1].strip()

with open("RFC.txt", "r") as ins:
    RFC = []
    #lines = [line.rstrip('\n') for line in open("tempo(x).txt")]
    for line in ins:
        RFC = [x2.strip() for x2 in RFC]
        RFC.append(line)
    RFC[-1] = RFC[-1].strip()

y = numpy.linspace(2,9,8)

#eSVM = numpy.array([2,5,4,5,2,2,3,3])
#filex = open("tempo(x).txt", "r")
#filey = open("Altura(y).txt", "r")

#x = filex.readlines()
#y = filey.readlines()
#markers_on = [12, 17, 18, 19]
#plt.plot(xs, ys, '-gD', markevery=markers_on)

#print(contentx[0], contentx[9], contentx[23], contentx[-2])

#(1;34,4); (10;29,6), (24;24,4), (80;11,4)


markers_on = [94.2, 83.16, 64.47, 57.58]

#plt.plot(contentx,contenty, '-bD', markevery=markers_on)
#plt.plot( y,SVM, '-bD', markevery=markers_on)
#plt.plot(  y,SVM,  markevery=markers_on)
plt.plot( y,SVM, '--bo', label='SVM')
#plt.plot(y,RFC, '--ro', label='Random Forest')
#plt.errorbar(y,SVM, eSVM,  linestyle='None', marker='^')
#plt.plot(x, i * x, label='$y = %ix$' % i)
plt.legend()
plt.grid(True)
plt.xlabel('Quantidade de tipografias', fontsize = 16)
plt.ylabel('Acurácia da classificação [%]', fontsize = 16)

plt.show()
#print(contenty)

exit()
