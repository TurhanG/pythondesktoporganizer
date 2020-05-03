import shutil
from glob import glob
from pathlib import Path
import os

copyPath = "C:/Users/turha/Documents/" # Path where the files will be copied to. 
originPath = "C:/Users/turha/Desktop/" # Path where the files will be copied from. 

fileTypes = [
    {
        "fileType": "*.rar", # File extension/type.
        "filePath": "compressed_files", #Path that the files with specified path type will be copied.
        "fileFullName": "Rar Files" # File full name for console messages.
    },
    {
        "fileType": "*.zip",
        "filePath": "compressed_files",
        "fileFullName": "ZIP Files"
    },
    {
        "fileType": "*.pdf",
        "filePath": "pdf_files",
        "fileFullName": "PDF Files"
    },



]

for fileType in fileTypes:
    mkdirPath = copyPath+fileType['filePath'] # Complete path where the file be copied.
    filePaths = glob(originPath+fileType['fileType']) # Get all the files with the chosen type in the origin path. 
    fileCount = len(filePaths) # Total file count.

    dirExists = os.path.isdir(mkdirPath) # Here we check if the file path exists. If it isn't created file path will be created.
    if dirExists == False:
        try:
            os.mkdir(mkdirPath)
        except OSError:
            print("Creation of the directory %s failed" % mkdirPath)
        else:
            print("Successfully created the directory %s " % mkdirPath)

    if fileCount == 0: # Check if the files exist.
        print("No " + fileType['fileFullName'] + " to move.")
    else:
        for path in filePaths:  
            fileName = os.path.basename(path)
            Path(path).rename(copyPath + fileType['filePath']+"/" + fileName)
        print("Total " + fileType['fileFullName'] + " moved: " + str(fileCount))

