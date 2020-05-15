import csv
import random
code = '<aiml version = "1.0.1" encoding = "UTF-8">\n' 
with open('books_new.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         code = code + "<category>\n<pattern>"+row[0].upper()+"</pattern>\n<that>* BOOK S NAME *</that>\n<template>"+"Title:"+row[0]+" \\n Author:"+row[1]+" \\n Genre:"+row[2]+" \\n SubGenre:"+row[3]+" \\n Height:"+row[4]+" \\n Publisher:"+row[5]+" \\n Price: Rs."+str(random.randint(700,1400))+" \\n Would you like to buy that book?"+"</template>\n</category>\n"
code = code+"\n </aiml>"
code = code.replace("&","AND")
code = code.replace("'","")
code = code.replace("-"," ") 
print(code)
