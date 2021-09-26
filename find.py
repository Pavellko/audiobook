import os
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if '.git' not in root:
            path_file = os.path.join(root,file)
            print(path_file)