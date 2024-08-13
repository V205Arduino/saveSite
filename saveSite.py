import requests

def save_to_wayback(url):
    # The URL for saving a page to the Wayback Machine
    wayback_save_url = 'https://web.archive.org/save/'
    
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # Make the request to save the page
    response = requests.post(wayback_save_url + url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # The response often contains a link to the archived version
        if 'Content-Location' in response.headers:
            archive_url = 'https://web.archive.org' + response.headers['Content-Location']
            print(f"Page archived successfully. View it at: {archive_url}")
        else:
            print("Page was submitted for archiving, but no immediate URL provided.")
    else:
        print(f"Failed to archive the page. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    url_to_archive = "https://forum.arduino.cc/"
    save_to_wayback(url_to_archive)