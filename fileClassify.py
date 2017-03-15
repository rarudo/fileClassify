# -*- coding: utf-8 -*-
import os
import shutil

# 先頭から何文字参照してフォルダ分けを行うか
workDir = os.getcwd() + "/"
# スペースで分割できなかった場合、指定された文字で分割
secondSplit = "-"
def moveDir(fileName, dirName):
    shutil.move(fileName, dirName)

def getFilesDirs():
    files = os.listdir(workDir)
    fileList = []
    dirList = []
    for file in files:
        if "." in file and file[0] != ".":
            fileList.append(file)
        else:
            dirList.append(file)
    return fileList, dirList

# スペースを含むまでの文字数を返す
def getPrefix(file):
    if len(file.split()) > 1:
        splits = file.split()
    elif len(file.split(secondSplit)) > 1:
        splits = file.split(secondSplit)
    else:
        splits = file.split(".")
    prefix = splits[0]
    return prefix

files, dirs = getFilesDirs()
for file in files:
    prefix = getPrefix(file)
    if prefix in dirs:
        shutil.move(workDir+file,workDir+prefix)
    else:
        mkdirPath = workDir+prefix
        print(mkdirPath)
        os.mkdir(mkdirPath)
        shutil.move(workDir+file,workDir+prefix)
    files, dirs = getFilesDirs()


