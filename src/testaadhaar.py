#!/usr/bin/env python
import os
import os.path
import json
import sys
import string
import pytesseract
import re
import difflib
import csv
import nltk
import subprocess
import dateutil.parser as dparser
from dateutil.parser import _timelex, parser
from PIL import Image, ImageEnhance, ImageFilter
path = sys.argv[1]

img = Image.open(path)
img = img.convert('RGBA')
#img = img.filter(ImageFilter.SHARPEN)
pix = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)

img.save('temp.jpg')
'''
w,h=img.size
e=int(0.2*w)
f=int(0.65*h)
e1=int(0.72*w)
f1=int(0.9*h)
img.crop((e,f,e1,f1)).save('img3.jpg')
texttest = pytesseract.image_to_string(Image.open('img3.jpg'))
print(texttest)
#'''
#text = pytesseract.image_to_string(Image.open('temp.jpg'))
subprocess.call("tesseract "+path+" out -4", shell=True)
subprocess.call("tesseract temp.jpg out1 -4", shell=True)
fi = open('out.txt', 'r')
text = fi.read()
fitemp = open('out1.txt', 'r')
texttemp = fitemp.read()

text = filter(lambda x: ord(x)<128,text)
texttemp = filter(lambda x: ord(x)<128,texttemp)

# Initializing data variable
name = None
gender = None
ayear = None
uid = None
yearline = []
genline = []
nameline = []
text1 = []
text2 = []

name1 = None
gender1 = None
ayear1 = None
uid1 = None
yearline1 = []
genline1 = []
nameline1 = []
text11 = []
text21 = []


# Searching for Year of Birth
lines = text
print lines
#tokens = nltk.word_tokenize(lines)
#sentences = nltk.sent_tokenize(lines)
#sentences = [nltk.word_tokenize(sent) for sent in sentences]
#sentences = [nltk.pos_tag(sent) for sent in sentences]
#print sentences
#print "_________________"
#print tokens

for wordlist in lines.split('\n'):
	xx = wordlist.split( )
	if ([w for w in xx if re.search('(Year|Birth|irth|YoB|YOB:|DOB:|DOB)$', w)]):
		yearline = wordlist
		break
	else:
		text1.append(wordlist)
try:
	text2 = text.split(yearline,1)[1]
except:
	pass

try:
	yearline = re.split('Year|Birth|Birth |Birth :|Birth:|irth|YoB|YOB:|DOB:|DOB', yearline)[1:]
	yearline = ''.join(str(e) for e in yearline)
	if(yearline):
		ayear = dparser.parse(yearline,fuzzy=True).year
except:
	pass
#------------------------------------------------------	
'''
try:
	p = parser()
	info = p.info

	def timetoken(token):
	  try:
		float(token)
		return True
	  except ValueError:
		pass
	  return any(f(token) for f in (info.jump,info.weekday,info.month,info.hms,info.ampm,info.pertain,info.utczone,info.tzoffset))

	def timesplit(input_string):
	  batch = []
	  for token in _timelex(input_string):
		if timetoken(token):
		  if info.jump(token):
		    continue
		  batch.append(token)
		else:
		  if batch:
		    yield " ".join(batch)
		    batch = []
	  if batch:
		yield " ".join(batch)

	for item in timesplit(yearline):
	  print "Found:", item
	  print "Parsed:", p.parse(item)
except:
	pass
#'''
#-----------------------------------------------------------

# Searching for Gender
try:
	for wordlist in lines.split('\n'):
		xx = wordlist.split( )
		if ([w for w in xx if re.search('(Female|Male|emale|male|ale|FEMALE|MALE|EMALE)$', w)]):
			genline = wordlist
			break

	if 'Female' in genline:
	    gender = "Female"
	if 'Male' in genline:
	    gender = "Male"

	text2 = text.split(genline,1)[1]

except:
	pass

#-----------Read Database
with open('namedb1.csv', 'rb') as f:
	reader = csv.reader(f)
	newlist = list(reader)    
newlist = sum(newlist, [])
#'''

'''
#-----------Read Database
with open('namedb.csv', 'rb') as f:
	reader = csv.reader(f)
	newlist = list(reader)    
newlist = sum(newlist, [])
#'''

# Searching for Name and finding closest name in database
try:
	text1 = filter(None, text1)
	for x in text1:
		for y in x.split( ):
			if(difflib.get_close_matches(y.upper(), newlist)):
				nameline.append(x)
				break
	name = ''.join(str(e) for e in nameline)
except:
	pass

# Searching for UID
try:
	newlist = []
	for xx in text2.split('\n'):
		newlist.append(xx)
	newlist = filter(lambda x: len(x)>5, newlist)
	ma = 0
	uid = ''.join(str(e) for e in newlist)
	for no in newlist:
		if ma<sum(c.isdigit() for c in no):
			ma = sum(c.isdigit() for c in no)
			uid = int(filter(str.isdigit, no))
except:
	pass

# Making tuples of data
data = {}
data['Name'] = name
data['Gender'] = gender
data['Birth year'] = ayear
data['Uid'] = uid
'''
# Writing data into JSON
with open('../result/'+ os.path.basename(sys.argv[1]).split('.')[0] +'.json', 'w') as fp:
    json.dump(data, fp)
'''

# Removing dummy files
os.remove('temp.jpg')

'''
# Reading data back JSON
with open('../result/'+ os.path.basename(sys.argv[1]).split('.')[0] +'.json', 'r') as f:
     ndata = json.load(f)
#'''
print "+++++++++++++++++++++++++++++++"     
print(data['Name'])
print "-------------------------------"
print(data['Gender'])
print "-------------------------------"
print(data['Birth year'])
print "-------------------------------"
print(data['Uid'])
print "-------------------------------"
#'''
