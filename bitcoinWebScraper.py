# coding: utf-8
# Here your code !
#Sophie Reich-Michalik
#Cite: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

#Before starting make sure Python is installed, then go to terminal and import beautiful soup (Type: easy_install pip) next (Type: pip install BeautifulSoup4)

#import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#define the url
pageurl = 'http://bitcointalk.org'

#query the website and define the html to 'page'
page = urllib2.urlopen(pageurl)

# parse the html using beautiful soup and store in variable `parsedpage`
parsedpage = BeautifulSoup(page, 'html.parser')

#variable 'parsedpage' contains the HTML of the page

content = parsedpage.find('td', attrs={'class': 'windowbg2'})
cont = content.text.strip() # strip() is used to remove starting and trailing
print (cont)

# get the index name
namebox = parsedpage.find('div', attrs={'class':'catbg'})
name = namebox.text
print (name)

# Write to excel file
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
