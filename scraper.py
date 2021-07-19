import bs4
import requests_html
import time
from class_num import class_num

# Scraping url for current ASU class portal
URL = (
    "https://webapp4.asu.edu/catalog/classlist?t=2217&k="
    + str(class_num)
    + "&k="
    + str(class_num)
    + "&hon=F&promod=F&e=open&page=1"
)


def get_seats():
    ses = requests_html.HTMLSession()
    response = ses.get(URL)
    response.html.render(sleep=1)
    soup = bs4.BeautifulSoup(response.html.html, "html.parser")
    results = soup.find(id="CatalogList")

    if results is None:
        return False
    else:
        available = results.find("td", class_="availableSeatsColumnValue")
        seats_arr = available.find_all("span")
        print(
            "There are "
            + seats_arr[0].text
            + " seats available in your class, out of "
            + seats_arr[2].text
            + " at "
            + time.ctime()
        )
        return True
