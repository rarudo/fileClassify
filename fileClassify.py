# -*- coding: utf-8 -*-
import os
import shutil

# スクリプトを実行するフォルダを指定
# デフォルトはスクリプトが置かれたフォルダ
workDir = os.getcwd() + "/"
# workDir = "/Users/user/Downloads/tesPython/tesDir/"

# スペースで分割できなかった場合、指定された文字で分割
splitList = ["-",
             "."
             ]


def moveDir(fileName, dirName):
    shutil.move(fileName, dirName)

def getFilesDirs():
    files = os.listdir(workDir)
    fileList = []
    dirList = []
    for file in files:
        # ファイルの判別
        if "." in file and file[0] != ".":
            fileList.append(file)
        # ディレクトリの判別、隠しファイルは除外
        elif file[0] != ".":
            dirList.append(file)
    return fileList, dirList


# 指定された条件でファイル名を分割
def getPrefix(file):
    for split in splitList:
        if len(file.split()) > 1:
            splits = file.split()
            break
        elif len(file.split(split)) > 1:
            splits = file.split(split)
            break
    prefix = splits[0]
    return prefix


files, dirs = getFilesDirs()
for file in files:
    prefix = getPrefix(file)
    if prefix in dirs:
        shutil.move(workDir + file, workDir + prefix)
    else:
        mkdirPath = workDir + prefix
        print(mkdirPath)
        os.mkdir(mkdirPath)
        shutil.move(workDir + file, workDir + prefix)
    files, dirs = getFilesDirs()
