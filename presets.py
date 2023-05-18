import os
import time
import pathlib
print(os.getcwd())


# folder path
mypath = os.path.abspath(os.path.dirname(__file__))
#mypath= os.fspath(pathlib.Path(__file__))



print(mypath)

# list file and directories
res = os.listdir(mypath)
print(res)

time.sleep(10)
