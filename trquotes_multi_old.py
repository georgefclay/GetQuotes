import requests
from bs4 import BeautifulSoup

def scrape_quotes_from_page(page_number):
    """
    Scrapes quotes from a specific page number and returns them as a list of strings.
    """
    base_url = "https://www.theodorerooseveltcenter.org/Learn-About-TR/TR-Quotes?page={}"
    url = base_url.format(page_number)
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all DIVs with class 'quote'
        quotes = soup.find_all('div', class_='quote')

        # Extract text from each quote and return as a list
        return [quote.get_text(strip=True) for quote in quotes]
    else:
        print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")
        return []

def scrape_all_quotes():
    """
    Loops through pages 1 to 20, scrapes quotes, and writes them to a file.
    """
    with open('TRQuotes.txt', 'w') as file:
        # Loop through page numbers 1 to 20
        for page_number in range(1, 8):
            # Scrape quotes from the current page
            quotes = scrape_quotes_from_page(page_number)

            # Write each quote to the file
            for quote in quotes:
                file.write(quote + "\n\n")
            
            print(f"Page {page_number} quotes have been written to TRQuotes.txt")
    
    print("All pages have been processed.")

# Call the function to scrape all quotes
scrape_all_quotes()
