import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

x = urllib.request.urlopen('https://www.cnn.com/')

print(x.read())
