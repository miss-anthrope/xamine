# Basic XML parser in Python3
# Credit: https://www.guru99.com/manipulating-xml-with-python.html
# Yes, I'm using minidom, don't judge me.

import xml.dom.minidom

def main():
	# Use the parse() function to load and parse the XML file.
	myDoc = xml.dom.minidom.parse('sslExpired.xml');

	# Print out the “node name” of the root of the Document and the “firstchild tagname”. 
	# Tagname and nodename are the standard properties of the XML file.
	print (myDoc.nodeName)
	print (myDoc.firstChild.tagName)

	# Generate a list of XML tags from the document and print each one.
	ssltest = myDoc.getElementsByTagName('ssltest')
	print ('%d hosts below responded to the SSLScan certificate query:' % ssltest.length)
	for ipAddress in ssltest:
		print (ipAddress.getAttribute('host'))

	# Were certs found?
	certificates = myDoc.getElementsByTagName('certificates')
	print ('Found certificates for the above.^^^')

	# Looking for the information in the 'certificate' element for the type 'short' below. The print line dosen't want to work anymore, although I had it working earlier. Not sure what I changed, sadly.
	certType = myDoc.getElementsByTagName('certificate')
	for certType in certificates:
		print (certType.getAttribute('type'))
# I get stopped below this line because I'm not sure how to print the date of expiration. I've gotten errors when I try to getElementsByTagName and getAttribute and both tell me the Element cannot be iterated.
# Suggestions on how to get this stupid little script to spit out this last part are welcome!
	#validDate = myDoc.getElementsByTagName('not-valid-after')
	#for endDate in validDate:
	#	print (endDate.[0]);

if __name__ == '__main__':
	main();