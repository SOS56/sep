import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_titles = soup.find_all('h2', class_='news-title')  # Replace with actual class name
        for title in news_titles:
            print(title.text)
    else:
        print('Failed to fetch the page.')

if __name__ == '__main__':
    target_url = 'https://example.com/news'  # Replace with the actual URL
    scrape_news_titles(target_url)
