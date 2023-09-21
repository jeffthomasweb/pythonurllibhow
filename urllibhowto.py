#The Python standard library is fairly well-featured. One does not absolutely need to use an outside library to make the occasional HTTP request.
import urllib.request 

#Create a variable to save the response. The response will be in bytes.
html = b""

#Using the NPR RSS Feed website as an example URL
with urllib.request.urlopen("https://feeds.npr.org/1001/rss.xml") as response:
    html = response.read()

print(html)
