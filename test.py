import os
import zipfile

file = "Match-2023-11-14_20-12-32-186"

#os.system("r6-dissect.exe " + file + " -x match.xlsx")

nextDirs = next(os.walk('./matches'))[1]
for dir in nextDirs:
    print(dir)
    os.system("r6-dissect.exe " + "matches/" + file + " -x match.xlsx")