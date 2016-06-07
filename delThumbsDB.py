#!/usr/bin/python3
#coding: utf8

import os
from send2trash import send2trash

searchDir = r'/Users/<username>/Pictures/'
searchFor = 'Thumbs.db'

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
            send2trash(os.path.join(root, name))
    return len(result)

def main():
    print(find_all(searchFor,searchDir), " files found and deleted!")
    

if __name__ == '__main__': 
    main()
