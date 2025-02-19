import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://www.theodorerooseveltcenter.org/Learn-About-TR/TR-Quotes?page=1"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with class 'quote_box'
quote_boxes = soup.find_all('div', class_='quote_box')

# Open a file to write the quotes to
with open("TRQuotes.txt", "w") as file:
    for box in quote_boxes:
        # Inside each 'quote_box', find the 'quote' div
        quote_div = box.find('div', class_='quote')
        if quote_div:
            quote_text = quote_div.get_text(strip=True)
            # Check if the quote length is 200 characters or less
            if len(quote_text) <= 200:
                # Write the quote to the file
                file.write(quote_text + "\n")
