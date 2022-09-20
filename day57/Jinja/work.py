import requests
cur_name = "Nataly"
params = {"name": cur_name}
url_gender = "https://api.genderize.io/"
url_age = "https://api.agify.io/"
response_gender = requests.get(url_gender, params=params)
response_age = requests.get(url_age, params=params)
age = response_age.json()['age']
gender = response_gender.json()['gender']
url_blog = "https://api.npoint.io/0a50e5219852c16cb6cb"
response_blog = requests.get(url_blog).json()
blog = response_blog
print(blog)