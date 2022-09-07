##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done
# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
import smtplib
import datetime as dt
from random import choice

my_email = "yellow.python@yandex.ru"
password = "lhxbztaszoysqymr"
placeholder = "[NAME]"
templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
now = dt.datetime.now()
now_day = now.day
now_month = now.month
data = pd.read_csv("birthdays.csv").to_dict(orient="records")
print(data)
for person in data:
    if person["day"] == now_day and person["month"] == now_month:
        print(person)
        letter_template = choice(templates)
        with open(letter_template) as letter:
            letter_to_sand = letter.read()
            letter_to_sand = letter_to_sand.replace(placeholder, person["name"])
            print(letter_to_sand)
            with smtplib.SMTP("smtp.yandex.ru") as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=person["email"],
                    msg=f"Subject:Happy Birthday, {person['name']}!!!\n\n{letter_to_sand}"
                )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




