import csv
import numpy as np
code = '<aiml version = "1.0.1" encoding = "UTF-8">\n' 
arr = np.zeros((5,))
with open('books_new.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		if row[2]=="fiction":
			if arr[0]==0:
				code = code + "<category>\n<pattern>"+row[2].upper()+"</pattern>\n<template>"
				arr[0]=1
			code = code+row[0]+" \\n "
		elif row[2]=="nonfiction":
			if arr[1]==0:
				code = code + "</template>\n</category>\n<category>\n<pattern>"+row[2].upper()+"</pattern>\n<template>"
				arr[1]=1
			code = code+row[0]+" \\n "
		elif row[2]=="philosophy":
			if arr[2]==0:
				code = code + "</template>\n</category>\n<category>\n<pattern>"+row[2].upper()+"</pattern>\n<template>"
				arr[2]=1
			code = code+row[0]+" \\n "
		elif row[2]=="science":
			if arr[3]==0:
				code = code + "</template>\n</category>\n<category>\n<pattern>"+row[2].upper()+"</pattern>\n<template>"
				arr[3]=1
			code = code+row[0]+" \\n "
		elif row[2]=="tech":
			if arr[4]==0:
				code = code + "</template>\n</category>\n<category>\n<pattern>"+row[2].upper()+"</pattern>\n<template>"
				arr[4]=1
			code = code+row[0]+" \\n "	


code = code+"</template>\n</category>"
code = code+"\n </aiml>"
code = code.replace("&","AND")
code = code.replace("'","")
code = code.replace("-"," ") 
print(code)
