import telebot
import re
import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# CONSTANTS
ID = os.environ["CLIENT_ID"]
SECRET = os.environ["CLIENT_SECRET"]
MY_EMAIL = os.environ["EMAIL"]
RECIPIENT = os.environ["RECIPIENT"]
MY_PASSWORD = os.environ["PASSWORD"]
TOKEN = os.environ["TOKEN"]


bot = telebot.TeleBot(TOKEN)

# LOGIN SPOTIFY
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=ID,
                                                           client_secret=SECRET))

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Please enter the date you wish to travel in.')
  bot.send_message(message.chat.id, 'Date format: YYYY-MM-DD')
  sent = bot.send_message(message.chat.id, 'Example: 2015-05-28')
  bot.register_next_step_handler(sent, hello)


def hello(message):
    flag = True
    while flag:
        date = message.text
        pattern_date = r"\d\d\d\d-\d\d-\d\d"
        match = re.fullmatch(pattern_date, date)
        if match is not None:
            bot.send_message(message.chat.id, 'The date which you have chosen ' + date)
            bot.send_message(message.chat.id, 'Bon Voyage and get there safe!')
            # GET DATE FOR SEARCHING TOP 5 SONGS
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
            bot.send_message(message.chat.id, massage_body)
            flag = False
        else:
            bot.send_message(message.chat.id, 'Please enter the date in format YYYY-MM-DD')
            bot.send_message(message.chat.id, 'Type /start')
            break




bot.infinity_polling()