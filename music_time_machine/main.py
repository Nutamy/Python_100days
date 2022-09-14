import telebot
import os
TOKEN = os.environ("TOKEN")
bot = telebot.Turtle(f"{TOKEN}")