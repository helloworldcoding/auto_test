#!/usr/bin/python3
from PIL import Image
from random import random

def get_random_picutre(size=2,widht=100,height=100, ext="png", path="./file"):
   im = Image.new("RGB",(width,height)) 
   fileName = int(random.random() * 1000000000000000) 
   im.save(str(fileName)+"."+ext)
   return str(fileName)+"."+ext
