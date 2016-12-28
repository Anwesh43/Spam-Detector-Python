import urllib2
import urllib
req = urllib2.Request('http://localhost:5000/test')
res = urllib2.urlopen(req)
print res.read()
dataMsg = {"msg":'get 10 off in dp'}
req = urllib2.Request('http://localhost:5000/detect_spam',urllib.urlencode(dataMsg))
urllib2.urlopen(req)
