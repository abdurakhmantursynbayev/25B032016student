import os
import shutil

dst = os.path.join(os.getcwd(), "cop_of_input.txt")
shutil.copy("input.txt", dst)

os.remove("input.txt")