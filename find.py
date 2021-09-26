from os import path


import os
def findi(pa=os.getcwd()):
    z=[]
    for root, dirs, files in os.walk(pa):
        for file in files:
            if '.git' not in root:
                path_file = os.path.join(root,file)
                z.append(path_file)
    return z