import os
import shutil
import time
base = '/Users/kushalsrinivas/Desktop/screenshots'
src = base + '/A'
dst = base + '/B'
ext_lib = os.listdir(dst)
print("starting in 5...")
time.sleep(5)
files = os.listdir(src)

while True:
    for file in files:
        try:
            if file != ".DS_Store":
                ext = os.path.splitext(file)[1][1::]
                print(os.path.splitext(file))
                print(ext)
                if not ext in ext_lib:
                    ext_lib.append(ext)
                    os.mkdir(dst + "/" + ext_lib[ext_lib.index(ext)])
                shutil.move(src + "/" + file, dst+"/" +
                            ext_lib[ext_lib.index(ext)])
        except FileExistsError:
            pass
