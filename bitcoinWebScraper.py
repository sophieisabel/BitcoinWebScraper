# coding: utf-8
# Here your code !
#Sophie Reich-Michalik
#Citation: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

#Before starting make sure Python is installed, then go to terminal and import beautiful soup (Type: easy_install pip) next (Type: pip install BeautifulSoup4)

#import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import xlwt
import re


site= "https://bitcointalk.org/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)


soup = BeautifulSoup(page, 'html.parser')

containers = soup.find_all('span', attrs={'class': 'smalltext'})
#print(type(containers))
#print(len(containers))

date = containers[0]



m = re.search('(?<=smalltext">)(.*)(?=<\/span)', str(date))
if m:
    newdate = m.group(1)


news = containers[1]
#print newdate



m = re.search('(?<=download">)(.*)(?=<\/a> )', str(news))
if m:
    newnews = m.group(1)

newstext = "Latest bitcoin core release"
newnews = (newstext + ": " + newnews)
#print newnews


discussioncontainers = soup.find_all('td', attrs={'class': 'windowbg2'})
dcontent = discussioncontainers[1]
dcontent = str(dcontent.text)
dcontent = dcontent.splitlines()[2]
discussion = dcontent.strip()
#print discussion

dpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
dposts = dpostcontainers[1]
dposts = str(dposts.text)
dposts = dposts.splitlines()[1]
dposts =  dposts.strip()
#print dposts

dtopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
dtopics = dtopiccontainers[1]
dtopics = str(dtopics.text)
dtopics = dtopics.splitlines()[2]
dtopics =  dtopics.strip()
#print dtopics












developmentcontainers = soup.find_all('td', attrs={'class': 'windowbg2'})
dtcontent = developmentcontainers[3]
dtcontent = str(dtcontent.text)
dtcontent = dtcontent.splitlines()[2]
development =  dtcontent.strip()
#print development

dtpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
dtposts = dtpostcontainers[3]
dtposts = str(dtposts.text)
dtposts = dtposts.splitlines()[1]
dtposts =  dtposts.strip()
#print dtposts

dttopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
dttopics = dttopiccontainers[3]
dttopics = str(dttopics.text)
dttopics = dttopics.splitlines()[2]
dttopics =  dttopics.strip()
#print dttopics









containers3 = soup.find_all('td', attrs={'class': 'windowbg2'})
content = containers3[5]
content = str(content.text)
content = content.splitlines()[2]
Mining =  content.strip()
#print Mining


Mpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
Mposts = Mpostcontainers[5]
Mposts = str(Mposts.text)
Mposts = Mposts.splitlines()[1]
Mposts =  Mposts.strip()
#print Mposts

Mtopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
Mtopics = Mtopiccontainers[5]
Mtopics = str(Mtopics.text)
Mtopics = Mtopics.splitlines()[2]
Mtopics =  Mtopics.strip()
#print Mtopics




tcontainers = soup.find_all('td', attrs={'class': 'windowbg2'})
tcontent = tcontainers[7]
tcontent = str(tcontent.text)
tcontent = tcontent.splitlines()[2]
technical =  tcontent.strip()
#print technical



tpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
tposts = tpostcontainers[7]
tposts = str(tposts.text)
tposts = tposts.splitlines()[1]
tposts =  tposts.strip()
#print tposts

ttopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
ttopics = ttopiccontainers[7]
ttopics = str(ttopics.text)
ttopics = ttopics.splitlines()[2]
ttopics =  ttopics.strip()
#print ttopics





containers3 = soup.find_all('td', attrs={'class': 'windowbg2'})
content = containers3[9]
content = str(content.text)
content = content.splitlines()[2]
project =  content.strip()
#print project

ppostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
pposts = ppostcontainers[9]
pposts = str(pposts.text)
pposts = pposts.splitlines()[1]
pposts =  pposts.strip()
#print pposts

ptopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
ptopics = ptopiccontainers[9]
ptopics = str(ptopics.text)
ptopics = ptopics.splitlines()[2]
ptopics =  ptopics.strip()
#print ptopics






#Economy


epostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
eposts = epostcontainers[11]
eposts = str(eposts.text)
eposts = eposts.splitlines()[1]
eposts =  eposts.strip()
print eposts

etopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
etopics = ptopiccontainers[11]
etopics = str(etopics.text)
etopics = etopics.splitlines()[2]
etopics =  etopics.strip()
print etopics



mcontainers = soup.find_all('td', attrs={'class': 'windowbg2'})
mcontent = mcontainers[13]
mcontent = str(mcontent.text)
mcontent = mcontent.splitlines()[2]
market =  mcontent.strip()
#print project

mpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
mposts = mpostcontainers[13]
mposts = str(mposts.text)
mposts = mposts.splitlines()[1]
mposts =  mposts.strip()
#print pposts

mdtopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
mdtopics = mdtopiccontainers[15]
mdtopics = str(mdtopics.text)
mdtopics = mdtopics.splitlines()[2]
mdtopics =  mdtopics.strip()





tdcontainers = soup.find_all('td', attrs={'class': 'windowbg2'})
tdcontent = tdcontainers[15]
tdcontent = str(tdcontent.text)
tdcontent = tdcontent.splitlines()[2]
trading =  tdcontent.strip()
#print project

tdpostcontainers = soup.find_all('td', attrs={'class': 'windowbg'})
tdposts = tdpostcontainers[15]
tdposts = str(tdposts.text)
tdposts = tdposts.splitlines()[1]
tdposts =  tdposts.strip()
#print pposts

tdtopiccontainers = soup.find_all('td', attrs={'class': 'windowbg'})
tdtopics = tdtopiccontainers[15]
tdtopics = str(tdtopics.text)
tdtopics = tdtopics.splitlines()[2]
tdtopics =  tdtopics.strip()





#containers3 = soup.find_all('td', attrs={'class': 'windowbg2'})
#content = containers3[2]
#content = str(content.text)
#content = content.splitlines()[2]
#test =  content.strip()
#print test




a=newdate
b=newnews
c=discussion
d=development
e=Mining
f=technical
g=project
h=dposts
i=dtopics
j=dtposts
k=dttopics
l=Mposts
m=Mtopics
n=tposts
o=ttopics
p=pposts
q=ptopics
r=eposts
s=etopics
t=market
u=mposts
v=mdtopics
w=trading
x=tdposts
y=tdtopics

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Main Page")
style = xlwt.XFStyle()
font = xlwt.Font()
font.bold = True
style.font = font


sheet1.write(2, 0, "Bitcoin:", style=style)
sheet1.write(7, 0, "Economy:", style=style)

sheet1.write(0, 0, "Date:", style=style)
sheet1.write(1, 0, "News:", style=style)

#Bitcoin
sheet1.write(2, 1, "Bitcoin Discussion:", style=style)
sheet1.write(3, 1, "Development & Technical Discussion:", style=style)
sheet1.write(4, 1, "Mining:", style=style)
sheet1.write(5, 1, "Bitcoin Technical Support:", style=style)
sheet1.write(6, 1, "Project Development:", style=style)

#Economy
sheet1.write(7, 1, "Economics:", style=style)
sheet1.write(8, 1, "Marketplace:", style=style)
sheet1.write(9, 1, "Trading Discussion:", style=style)


sheet1.write(0, 1, a)
sheet1.write(1, 1, b)
sheet1.write(2, 2, c)
sheet1.write(3, 2, d)
sheet1.write(4, 2, e)
sheet1.write(5, 2, f)
sheet1.write(6, 2, g)
sheet1.write(8, 2, t)
sheet1.write(9, 2, w)


#Printing Posts and Topics to Excel Sheet
sheet1.write(2, 3, h)
sheet1.write(2, 4, i)
sheet1.write(3, 3, j)
sheet1.write(3, 4, k)
sheet1.write(4, 3, l)
sheet1.write(4, 4, m)
sheet1.write(5, 3, n)
sheet1.write(5, 4, o)
sheet1.write(6, 3, p)
sheet1.write(6, 4, q)
sheet1.write(7, 3, r)
sheet1.write(7, 4, s)
sheet1.write(8, 3, u)
sheet1.write(8, 4, v)
sheet1.write(9, 3, x)
sheet1.write(9, 4, y)




book.save("bitcoinSrape.xls")
