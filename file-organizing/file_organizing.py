# file handling: navigate, rename, move, copy, remove
import os
import shutil
from pathlib import Path

# change working directory
print(os.getcwd())

os.chdir("/Users/patrick/Desktop/video-files")
print(os.getcwd())

# rename files
for file in os.listdir():
    # This example changes filenames from
    # 'dictionary - python-course-3.mov'
    # to --> 
    # '03-python-course-dictionary.mov'
    name, ext = os.path.splitext(file)

    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"

    os.rename(file, new_name)

    # or
    # f = Path(file)
    # name, ext = f.stem, f.suffix
    # f.rename(new_name)

# create directory
Path("data").mkdir(exist_ok=True)

# or
if not os.path.exists("data"):
    os.mkdir("data")

# move file and folder
shutil.move('f', 'd')  # works for file and folder

# copy file and folder
shutil.copy("src", "dest")
shutil.copy2("src", "dest")

# remove file and folder
os.remove("filename")  # error if not found
os.rmdir("folder")  # error if not empty, or not found
shutil.rmtree("folder")  # works for non empty directories

