# Idea: go through downloads folder 
# take all the .pdf and put them in a pdf folder 

import os 
import shutil 

source = 'C:\\Users\\castr\\Downloads\\'
destination = 'C:\\Users\\castr\\Desktop\\PDFFiles\\'

files = os.listdir(source)
for file in files:
    if file.endswith('.pdf'):
        shutil.move(source + file, destination + file)
        print("Success")
        break
    else:
        print("File not found")
        break
