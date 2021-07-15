import requests
from bs4 import BeautifulSoup


URL = "https://webapp4.asu.edu/catalog/classlist?t=2217&k=75871&k=75871&hon=F&promod=F&e=open&page=1"


from requests_html import HTMLSession

s = HTMLSession()
response = s.get(URL)
response.html.render(sleep=1)
soup = BeautifulSoup(response.html.html, "html.parser")
results = soup.find(id="classResults")
print(results.prettify())
# print(response.html.text)
# file1 = open("MyFile.txt", "w")
# file1.write(response.html.html)
# file1.close()
