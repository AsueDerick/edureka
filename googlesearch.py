import sys
import requests
from bs4 import BeautifulSoup

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all("a")
        for link in links:
            if link.get('href') and 'url?q=' in link.get('href'):
                url = link.get('href').split('url?q=')[1].split('&')[0]
                print(url)

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python googlesearch.py <search_query>")
    else:
        search_query = sys.argv[1]
        google_search(search_query)
