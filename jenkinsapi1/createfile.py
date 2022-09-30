#!/usr/bin/env python3

import os

def main():
    filename = input('Enter file name \n')
    comment = "#!/usr/bin/env python3"
    if checkfile(filename):
        print("{} is present".format(filename))
    else:
        createfile(filename,comment)  

def checkfile(filename):
    if filename in os.listdir(os.getcwd()):
        return True
    else:
        return False

def createfile(filename,comment):
    with open(filename,"w") as file:
        file.write(comment)        

if __name__ == "__main__":
    main()