import os
from os import path
import datetime

print("Input path folder")
file_path =  input()
if not os.path.exists(file_path):
    print("Path not found")
    exit()

files = []
dirs = [file_path]

def checkdir(folder):
    dirs.pop(0)
    content = os.listdir(folder)
    for el in content:
        fullname = os.path.join(folder, el)
        if os.path.isfile(fullname):
            files.append(fullname)
        elif os.path.isdir(fullname):
            dirs.append(fullname)
    return dirs

def abs_name(files_arr):
    names = []
    for file in files_arr:
        full_name = path.basename(file)
        name = path.splitext(full_name)[0]
        names.append(name)
    names.sort()
    return names

def dublicator(names_arr):
    new_arr = []
    for name in names_arr:
        if "— копия" in name:
            new_str = name.split(" — копия", 1)[0]
            if new_str not in new_arr:
                new_arr.append(new_str)
        elif name not in new_arr:
            new_arr.append(name)
    return new_arr

def remove_files(folder):
    dirs.pop(0)
    content = os.listdir(folder)
    for el in content:
        fullname = os.path.join(folder, el)
        if os.path.isfile(fullname):
            full_name = path.basename(el)
            name = path.splitext(full_name)[0]
            if name not in end_arr:
                deleted.append(fullname)
                os.remove(fullname)
            else:
                end_arr.remove(name)
        elif os.path.isdir(fullname):
            dirs.append(fullname)
    return dirs
            

while len(dirs) > 0:
    checkdir(dirs[0])

end_arr = dublicator(abs_name(files))

filename = "deleted_"+str(datetime.date.today())+".txt"

file = open(filename, "w+")
deleted = []
dirs = [file_path]
while len(dirs) > 0:
    remove_files(dirs[0])

for note in deleted:
    file.write(note+'\n')

file.close()

print("Script ended success!")