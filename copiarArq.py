################################
######## Copia as imagens que estão separadas em diretórios específicos de
######## cada letra para um diretório raiz
#################################

import os
from shutil import copyfile
import string


filePath1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/"

alfabeto = list(string.ascii_uppercase)
numeros = list(string.digits)

#para cada letra do alfabeto (ou seja, cada diretório) -> Mauisculas
for letter in alfabeto:
    #print(letter)
    os.chdir(filePath1 + "Maiusculas/" + letter + "/")
    #copyfile((filePath1 + "Maiusculas/" + letter), filePath1)

    #salva o nome de todos arquivos do diretorio em "filenames"
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
        # percorre todos os arquivos no diretório, remove DS_Store
        for filename in filenames:
            if filename == '.DS_Store':
                filenames.remove('.DS_Store')

    #copia cada arquivo para o diretório letrasSeparadas
    for filename in filenames:
        copyfile((filePath1 + "Maiusculas/" + letter + "/" + filename), (filePath1 + filename))


#para cada letra do alfabeto (ou seja, cada diretório) -> Minusculas
for letter in alfabeto:
    #print(letter)
    os.chdir(filePath1 + "Minusculas/" + letter + "/")
    #copyfile((filePath1 + "Maiusculas/" + letter), filePath1)

    #salva o nome de todos arquivos do diretorio em "filenames"
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
        # percorre todos os arquivos no diretório, remove DS_Store
        for filename in filenames:
            if filename == '.DS_Store':
                filenames.remove('.DS_Store')

    #copia cada arquivo para o diretório letrasSeparadas
    for filename in filenames:
        copyfile((filePath1 + "Minusculas/" + letter + "/" + filename), (filePath1 + filename))

#para cada letra do alfabeto (ou seja, cada diretório) -> Minusculas
for digit in numeros:
    #print(letter)
    os.chdir(filePath1 + "numeros/" + digit + "/")
    #copyfile((filePath1 + "Maiusculas/" + letter), filePath1)

    #salva o nome de todos arquivos do diretorio em "filenames"
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
        # percorre todos os arquivos no diretório, remove DS_Store
        for filename in filenames:
            if filename == '.DS_Store':
                filenames.remove('.DS_Store')

    #copia cada arquivo para o diretório letrasSeparadas
    for filename in filenames:
        copyfile((filePath1 + "numeros/" + digit + "/" + filename), (filePath1 + filename))
