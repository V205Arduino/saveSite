import requests
from bs4 import BeautifulSoup

def extract_urls(url, output_file):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all URLs on the page
    urls = []
    for a in soup.find_all('a', href=True):
        urls.append(a['href'])

    # Write the URLs to a text file
    with open(output_file, 'w') as f:
        for url in urls:
            f.write(url + '\n')

    print(f'Extracted {len(urls)} URLs and saved to {output_file}')

# Example usage:
url = "https://forum.arduino.cc/"
output_file = "extracted_urls.txt"
extract_urls(url, output_file)



