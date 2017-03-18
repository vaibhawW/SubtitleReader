from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen as uo
import requests
import sys
text =0
count=0
artistName = 0
def work(x):
	artistName=x
	artistName=artistName.replace(' ','')
	url = "http://www.azlyrics.com/"+artistName[0]+"/"+artistName+"/"
	page = bs(uo(url))
	listAlbum = page.find('div',attrs={'id':'listAlbum'})
	allLinks=listAlbum.findAll('a',attrs={'target':'_blank'})
	songsLink=[]
	for x in AllSongs:
		if(x[0]=='.'):
			songsLink.append("http://www.lyrics.com"+str(x['href'])[2:])
	count=0
	for x in songsLink:
		count+=str(bs(uo(x))).count(text)
	return count
		
file=open("readme1.txt",'r')
d = file.read().split()
text = d[-1]
d.pop();
lol	=[]
for jj in d:
	lol.append(work(jj))
Doun=open("writeMe.txt",'w')
p=lol
p=p.sort()
for x in p:
	Doun.write(d[lol.index(x)])
	Doun.write("\n\0")
