from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen as uo
from requests import get

count = 0
index = 0

file = open('file.txt','r')

singersNam=file.read().split('\n')
singersNam.remove('')
singersName=[]
for x in range(len(singersNam)):
	singersName.append(singersNam[x].replace(' ','+').lower())

text=singersName[-1]
singersName.pop()

def fun(artist,text):
	url = bs(get('http://www.lyricsfreak.com/'+artist[0]+'/'+artist+'/').content)
	script=url.findAll('script',attrs={'id':None,'class':None,'type':None})
	lop=-1
	for k in script:
		if (str(k).startswith("""<script>
var songs_non_display""")):
			lop=script.index(k)
			break
	if(lop==-1): 
		print("ops")
		return 0
	else: script=script[lop]
	global count
	global index
	script=str(script).split(';a ')
	scripts=[]
	for x in script:
		if x.startswith("href"):
			scripts.append(x)
	
	script=[]
	for x in scripts:
		script.append(x[8:].split('" title')[0])
	scripts=[]
	for x in script:
		k=x
		scripts.append(k.replace('\\',''))
	for x in scripts:
		count+=str(get("http://www.lyricsfreak.com"+x).content).count(text)
		index+=1
		print str(index)+": "+ "http://www.lyricsfreak.com"+x
	
def game(artist,text):
	print artist
	global count
	count = 0
	global index
	index =0
	url1 = bs(get('http://www.lyricsfreak.com/'+artist[0]+'/'+artist+'/').content)
	fun(artist,text)
	songs = url1.find('table',attrs={'name':'song'})
	if(songs==None): return 0
	linklist = songs.findAll('a')
	for x in linklist:
	  if(x['href'][0]	=='/'):
		count+=str(get("http://www.lyricsfreak.com"+x['href']).content).count(text)
		index+=1
		print str(index)+": "+"http://www.lyricsfreak.com"+x['href']

	return count
k=[]
for x in singersName:
	k.append(game(x,text))

t=[]
file=open("output.txt",'w')
for x in range(len(k)):
	t.append((k[x],singersName[x]))
print t
t.sort(key=lambda pair: -pair[0])
for x in range(len(k)):
	print>>file,t[x][1].replace('+',' ')
file.close()