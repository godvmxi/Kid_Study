from urllib.request import urlopen
html = urlopen('http://helloworldbook2.com/data/message.txt')
print(html.read())