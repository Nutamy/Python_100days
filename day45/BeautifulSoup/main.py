from bs4 import BeautifulSoup
import requests

url_movies = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
url_hack_news = 'https://news.ycombinator.com/news'
response = requests.get(url_movies)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
list_movies = [movie.getText() for movie in movies]
list_movies.reverse()
with open("movies.txt", "w", encoding='utf-8') as f:
    for movie in list_movies:
        f.write(movie + "\n")



# HACK NEWS
# articles = soup.find_all(name="a", class_="titlelink")
# article_text = [tag.getText() for tag in articles]
# article_link = [tag.get("href") for tag in articles]
# scores_tags = soup.find_all(name="span", class_="score")
# article_scores = [int(tag.getText().split()[0]) for tag in scores_tags]
# print(*article_link, sep="\n")
# print(*article_text, sep="\n")
# print(*article_scores, sep="\n")
# sorted_articles = []
# max_score = 0
# while len(article_scores) > 0:
#     max_score = max(article_scores)
#     idx_max = article_scores.index(max_score)
#     sorted_articles.append((article_text[idx_max],
#                             article_link[idx_max],
#                             article_scores[idx_max]
#                             ))
#     article_scores.pop(idx_max)
# print(*sorted_articles, sep="\n")