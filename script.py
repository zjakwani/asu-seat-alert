from bs4 import BeautifulSoup
from requests_html import HTMLSession


class_num = 75871


URL = (
    "https://webapp4.asu.edu/catalog/classlist?t=2217&k="
    + str(class_num)
    + "&k="
    + str(class_num)
    + "&hon=F&promod=F&e=open&page=1"
)


ses = HTMLSession()
response = ses.get(URL)
response.html.render(sleep=1)
soup = BeautifulSoup(response.html.html, "html.parser")
results = soup.find(id="CatalogList")

if results is None:
    print("Class Full")
else:
    available = results.find("td", class_="availableSeatsColumnValue")
    seats_arr = available.find_all("span")
    print(
        "There are "
        + seats_arr[0].text
        + " seats available in your class, out of "
        + seats_arr[2].text
    )
