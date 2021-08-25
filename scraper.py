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

# Scraping script
def get_seats():

    # Uses requests to access dynamic JavaScript-rendered content
    ses = requests_html.HTMLSession()
    response = ses.get(URL)
    response.html.render(sleep=1)
    # uses BeautifulSoup to render and select the correct HTML elements
    soup = bs4.BeautifulSoup(response.html.html, "html.parser")
    results = soup.find(id="CatalogList")

    if results is None:
        return False
    else:
        # If class is open, gets the HTML element for seat numbers
        available = results.find("td", class_="availableSeatsColumnValue")
        seats_arr = available.find_all("span")
        # Console log
        print(
            "There are "
            + seats_arr[0].text
            + " seats available in your class, out of "
            + seats_arr[2].text
            + " at "
            + time.ctime()
        )
        return True
