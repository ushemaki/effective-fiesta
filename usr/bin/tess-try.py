#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PIL import Image
import pytesseract
dosya=open("filename.txt", "w")
sys.stdout=dosya
im = Image.open("imagename.jpg")
text = pytesseract.image_to_string(im, lang='eng')
print text
