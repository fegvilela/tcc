import os

list = []
os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/")
file1 = open("list.txt", "w")

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        os.path.join(dirname, subdirname)
        if subdirname == '.DS_Store':
        # don't go into any .git directories.
            dirnames.remove('.DS_Store')
        '''
        if '.DS_Store' in subdirname:
        # don't go into any .git directories.
            subdirname.remove('.DS_Store')
'''

    i = 0
    # print path to all filenames.
    for filename in filenames:
        if filename != '.DS_Store':
            # don't go into any .git directories.
            #filenames.remove('.DS_Store')
            i = i+1
            print(os.path.join(dirname, filename))

    print(os.path.join(dirname, subdirname) + ": " + str(i))
    if i < 7 :
        list.append(os.path.join(dirname, subdirname) + ": " + str(7 - i))
        file1.write(os.path.join(dirname, subdirname) + " - faltam: " + str(7 - i) + "\n")
    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.DS_Store' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.DS_Store')

    if '.DS_Store' in filenames:
        # don't go into any .git directories.
        filenames.remove('.DS_Store')


file1.close()
