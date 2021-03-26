# To change this template, choose Tools | Templates
# and open the template in the editor.

#base url
#http://profile.ak.fbcdn.net/hprofile-ak-snc4/173670_657280951_6938939_n.jpg
import urllib, re, cookielib, urllib2

target='/home/wasuaje/Documentos/desarrollo/mt'
url='http://www.facebook.com/profile.php?id='
foto=153486434714656
valor=3333333

jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
content = opener.open(urllib2.Request(
    "https://www.facebook.com/login.php",
    "email=wasuaje@hotmail.com&pass=wa12761074&login_attempt=1")
).read()
print content
for n in range (1,3):
	foto=foto+valor
	strfoto=str(foto)
	data=urllib.urlopen(url+strfoto)
	print data.code
	if data.code != 404:
		text=data.read()		
		imgUrls = re.findall('img id=\"myphoto\" .*?src="(.*?)"', text)
		for imgUrl in imgUrls:
			print imgUrl
			try:
				imgData = urllib2.urlopen(imgUrl).read()				
				fileName = basename(urlsplit(imgUrl)[2])
				output = open(fileName,'wb')
				output.write(imgData)
				output.close()
			except:
				pass

		#f=open(target+"/"+strfoto+".jpg",'wb')
		#f.write(text)
		#f.close()
	    
	    
"http://a7.sphotos.ak.fbcdn.net/hphotos-ak-ash1/166602_1799473306113_1218180460_2072025_7809020_n.jpg"
"http://a8.sphotos.ak.fbcdn.net/hphotos-ak-ash2/45171_1602391819199_1218180460_1668579_3210140_n.jpg"
 
" http://a8.sphotos.ak.fbcdn.net/hphotos-ak-snc3/11531_1280127922803_1218180460_842047_1832978_n.jpg"
" http://a7.sphotos.ak.fbcdn.net/hphotos-ak-snc3/11531_1280127962804_1218180460_842048_8264796_n.jpg"
" http://a1.sphotos.ak.fbcdn.net/hphotos-ak-snc3/11531_1280128002805_1218180460_842049_2118847_n.jpg"
