# file handling: navigate, rename, move, copy, remove
# how to keep your desktop organized
import os
import shutil
from pathlib import Path

print(os.getcwd())

os.chdir("/Users/patrick/Desktop/video-files")
print(os.getcwd())

# rename files
for file in os.listdir():
    name, ext = os.path.splitext(file)

    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"

    print(new_name)
    os.rename(file, new_name)

    f = Path(file)
    name, ext = f.stem, f.suffix
    f.rename(new_name)

Path("data").mkdir(exist_ok=True)
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

shutil.rmtree("folder")  # non empty

