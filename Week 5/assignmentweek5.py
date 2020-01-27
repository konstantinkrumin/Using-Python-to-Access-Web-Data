import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0


address = input('Enter location: ')
	
print('Retrieving ' + address)
data = urllib.request.urlopen(address, context=ctx).read()
	
tree = ET.fromstring(data)
lst = tree.findall('.//count')
	
for item in lst:
	count += 1
	sum = sum + int(item.text)

print('Count: ', count)
print('Sum: ', sum)
	