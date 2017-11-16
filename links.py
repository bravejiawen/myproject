import urllib.request
import re
import webbrowser
website = urllib.request.urlopen("https://www.baidu.com/")
html = website.read()
html=html.decode('utf-8')
links = re.findall('"((http|ftp)s?://.*?)"', html)
print(links)
#for i in links:
    #webbrowser.open(i[0])
