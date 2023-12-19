import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'

# Set a user-agent header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_list = soup.find('tbody', {'class': 'lister-list'})

    for movie in movie_list.find_all('tr'):
        title = movie.find('td', {'class': 'titleColumn'}).find('a').text
        rating = movie.find('td', {'class': 'ratingColumn'}).find('strong').text
        print(f'Title: {title}, Rating: {rating}')

else:
    print(f'Error: Unable to fetch data. Status code: {response.status_code}')
