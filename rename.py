#!/usr/bin/env python
# encoding: utf-8

import os
import unicodedata

""" 
Renames the filenames within the same directory in ascii encoding.
1- convert utf-8 in ascii
2- replace specials characters of your choice by the one you want by calling the fonction
   replaceChar()

Usage:
1- put the script in the forlder you want rename the files
2- execute the script from this folder in terminal or shell with: python rename.py

By Jeremie Ricard
"""

path = os.getcwd()
filenames = os.listdir(path)

for file in filenames:
    if not file.endswith(".py") and not file.startswith("."):
            
        f = unicode(file, "utf-8")
        os.rename(file, unicodedata.normalize("NFKD", f).encode("ascii", "ignore"))
        

def replaceChar(char, newChar):
    filenames = os.listdir(path)

    for file in filenames:
        if not file.endswith(".py") and not file.startswith("."):
               
            if char in file and char != ".":
                os.rename(file, file.replace(char, newChar))

replaceChar(" ", "_")
replaceChar("-", "")
replaceChar("'", "")
replaceChar('"', "")


