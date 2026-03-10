import os
import shutil

# os.mkdir('new_folder')
# os.makedirs('a/b/c/d', exist_ok=True)

os.rmdir('new_folder')       # delete an empty directory
shutil.rmtree('a')   # delete a directory and ALL its contents