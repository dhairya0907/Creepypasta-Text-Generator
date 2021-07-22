# Script to devide large files into small parts.

import os
import math
from tqdm import tqdm

files = ["",""] # Enter all files name, which you want to divide
size = 4670284.5 # Enter size of each file part, (Defalut is for google colab)

for j in tqdm(files):
    with open(j) as fp: 
        data = fp.read()
        
    for i in range(1,math.ceil(len(data)/size) + 1):
        
        out = open(os.path.splitext(j)[0]+"_part_"+str(i)+".txt", "w") 
        halfway = round(4670284.5)
        if i == 1:
            out.write(data[0:halfway]) 
        elif i == 2:
            out.write(data[halfway:halfway * 2])
        elif i == math.ceil(len(data)/4670284.5):
            out.write(data[(halfway*(i - 1))+1:])
        else:
            out.write(data[(halfway*(i - 1))+1:halfway *i])
        out.close() 
        f = open("All_File_Name.txt", "a")
        f.write(os.path.splitext(j)[0]+"_part_"+str(i)+".txt")
        f.write("\n")
        f.close()
