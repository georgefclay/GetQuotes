import requests
from bs4 import BeautifulSoup

# Function to fetch quotes from a given page number
def fetch_quotes_from_page(page_num):
    # Base URL with page number
    url = f"https://www.theodorerooseveltcenter.org/Learn-About-TR/TR-Quotes?page={page_num}"
    
    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all divs with class 'quote_box'
    quote_boxes = soup.find_all('div', class_='quote_box')
    
    # List to store the filtered quotes
    quotes = []
    
    # Iterate through each 'quote_box'
    for box in quote_boxes:
        # Inside each 'quote_box', find the 'quote' div
        quote_div = box.find('div', class_='quote')
        if quote_div:
            quote_text = quote_div.get_text(strip=True)
            # Check if the quote length is 200 characters or less
            if len(quote_text) <= 200:
                quotes.append(quote_text)
    
    return quotes

# Main function to loop through pages and save quotes to a file
def scrape_quotes_to_file():
    # Open the file to write the quotes
    with open("TRQuotes.txt", "w") as file:
        # Loop through all 20 pages
        for page_num in range(1, 201):
            # Fetch quotes from the current page
            quotes = fetch_quotes_from_page(page_num)
            
            # Write each quote to the file
            for quote in quotes:
                file.write(quote + "\n")
    
    print("Quotes have been successfully written to TRQuotes.txt.")

# Run the scraper
scrape_quotes_to_file()
