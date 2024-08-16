import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls(url, output_file):
    """
    Extracts all URLs from a webpage and saves them to a file, 
    converting relative URLs to absolute ones.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')

        urls = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            # Convert relative URLs to absolute URLs
            absolute_url = urljoin(url, href) 
            urls.append(absolute_url)

        with open(output_file, 'w') as f:
            for url in urls:
                f.write(url + '\n')

        print(f'Extracted {len(urls)} URLs and saved to {output_file}')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
url = "https://forum.arduino.cc/" 
output_file = "arduino_forum_urls.txt"
extract_urls(url, output_file)