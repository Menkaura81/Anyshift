import os

# folder path
mypath = os.path.abspath(os.path.dirname(__file__))
os.system( f'"{mypath}/anyshift.exe"' ) 


# list file and directories
res = os.listdir(mypath)
print(res)
