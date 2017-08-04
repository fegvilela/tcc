############
##### Converte todas imagens do diretório dado (jpeg e gif => png)
##### retorna a lista de arquivos png
###########


import os
import glob


def convertImage(path):
    #salva o diretório original
    origPath = os.getcwd()
    # muda de diretório
    os.chdir(str(path))

    # transforma todos jpg em png
    jpgFiles = glob.glob("*.jpeg")
    for file in jpgFiles:
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg

    # transforma todos jpg em png
    jpgFiles = glob.glob("*.jpg")
    for file in jpgFiles:
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg

    # transforma todos gif em png
    gifFiles = glob.glob("*.gif")
    for file in gifFiles:
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove gif

    #todos arquivos png do diretório (ou seja, todas imagens do diretório)
    pngFiles = glob.glob("*.png")

    #retorna para o diretório original
    #os.chdir(origPath)
    return pngFiles

