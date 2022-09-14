import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import smtplib

# CONSTANTS
ID = os.environ["CLIENT_ID"]
SECRET = os.environ["CLIENT_SECRET"]
MY_EMAIL = os.environ["EMAIL"]
RECIPIENT = os.environ["RECIPIENT"]
MY_PASSWORD = os.environ["PASSWORD"]

# LOGIN SPOTIFY
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=ID,
                                                           client_secret=SECRET))

# GET DATE FOR SEARCHING TOP 5 SONGS
date = input("Type the date which you wish to travel in.\n"
             "the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# REQUEST TO CHARTS
response = requests.post(url)
soup = BeautifulSoup(response.text, "html.parser")

# CREATING LIST OF TOP 5 SONGS
top = soup.find_all(name="h3", id="title-of-a-story", class_="a-truncate-ellipsis")
top_5 = [tag.getText().strip() for tag in top][:5]

#  GET LINKS FROM SPOTIFY
playlist = []
for song in top_5:
    playlist.append(sp.search(q=song, limit=1))

links = []
for song in playlist:
    link = song['tracks']['items'][0]['album']['artists'][0]['external_urls']['spotify']
    links.append(link)

def sewing(song, link):
    return f"{song}: {link}\n"

msg = map(sewing, top_5, links)
massage_body = ""
for row in msg:
    massage_body += row

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECIPIENT,
        msg=f"Subject:Let's travel in {date}\n\n"
            f"TOP 5:\n\n {massage_body}")
    print("done")



