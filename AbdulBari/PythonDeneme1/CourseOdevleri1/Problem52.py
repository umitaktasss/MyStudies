import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

# Select movie titles and ratings
movies = soup.find_all("h3", {"class": "ipc-title__text"})
ratings = soup.find_all("span", {"class": "ipc-rating-star--rating"})

# Start from the second movie to skip the first unwanted entry
for movie, rating in zip(movies[1:], ratings):
    print(f"{movie.get_text(strip=True)} - Rating: {rating.get_text(strip=True)}")





