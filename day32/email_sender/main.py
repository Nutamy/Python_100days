import smtplib
import datetime as dt
from random import choice
my_email = "yellow.python@mail.ru"
password = "NPz3vhMnGcd0jqFPrVuA"
friend_email = "redruby705@yahoo.com"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes)
    with smtplib.SMTP("smtp.mail.ru") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject:Good morning!\n\n{quote}"
        )

# # import smtplib
# #
# # my_email = "yellow.python@mail.ru"
# # password = "NPz3vhMnGcd0jqFPrVuA"
# # friend_email = "redruby705@yahoo.com"
# #
# # '''
# # SMTP INFORMATION
# #
# # Gmail
# # connection = smtplib.SMTP("smtp.gmail.com")
# #
# # Hotmail
# # connection = smtplib.SMTP("smtp.live.com")
# #
# # Yahoo
# # connection = smtplib.SMTP("smtp.mail.yahoo.com")
# # '''
# #
# # with smtplib.SMTP("smtp.mail.ru") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(
# #         from_addr=my_email,
# #         to_addrs=friend_email,
# #         msg="Subject:Hello with LOVE!\n\nThis is the body of my email"
# #     )
# #
#
# import datetime as dt
#
# current_date = dt.datetime.now()
# year = current_date.year
# month = current_date.month
# day = current_date.day
# print(f"{day}.{month}.{year}")
#
# date_of_birth = dt.datetime(year=1985, month=7, day=8, hour=5)
# print(date_of_birth)
