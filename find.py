from os import path


def finfdi():
    import os
    z=[]
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if '.git' not in root:
                path_file = os.path.join(root,file)
                z.append(path_file)
    return z