import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Initialize totalsum and count values to 0
totalsum = 0
count = 0

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Set an input function for the url address and parse it through BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Convert the values in that class into text and append it to the numlist
commentsclass = soup.select('span[class="comments"]') 
numlist = list()
for comment in commentsclass:
	numlist.append(comment.get_text())

#Parse through each individual value in numlist and add it to the totalsum and count
if len(numlist) > 0:
	for num in numlist:
		totalsum = totalsum + int(num)
		count = count + 1
#Print out the final values
print("Count :",count)
print("Total Sum :", totalsum)