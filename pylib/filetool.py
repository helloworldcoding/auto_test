#!/usr/bin/python3
from PIL import Image
from random import random
import time
import os

def get_random_picutre(size="2m",width=100,height=100, ext="png", path="./file/"):
    '''
    @param     size    int float  or string
               12  means  12k
               12.32  means 12.32k
               12m  12M  means  12M
               max size is 50M
    @param     width    int    px
    @param     height   int  px
    @param     ext      string    png,jpg,jpeg,gif 
    convert -size 1000x2000 xc:gray +noise gaussian large.jpg
    convert large.jpg -define jpeg:extent=400kb 400kb.jpg
    '''
    try:
       im = Image.new("RGB",(width,height)) 
       fileName = str(int(time.time()*1000))+'_'+str(width)+'x'+str(height)+"."+ext
       im.save(path+fileName)
       return os.path.abspath(path+fileName)
    except Exception as e:
       print(e)
       return None


if __name__ == "__main__":
    get_random_picutre()
