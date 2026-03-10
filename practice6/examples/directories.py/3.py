import shutil

shutil.move('nesteddir/1.py', '1.py')
shutil.move('1.py', 'nesteddir/1.py')