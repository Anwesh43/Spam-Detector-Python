from flask import *
from SpamDetector import *
import os
app = Flask(__name__)
app.debug = True
spamDetector = SpamDetector()
spamDetector.train()
spamDetector.test()
port = 8080
if os.environ.has_key('PORT'):
    port = os.environ['PORT']
@app.route('/test')
def test():
    return "hello"
@app.route('/detect_spam',methods=['GET','POST'])
def detectspam():
    print request.__dict__
    msg =  request.args["msg"]
    result = spamDetector.predict(msg)
    print result
    return 'This is {0}'.format(result)
if __name__ == "__main__":
    app.run(port=port)
