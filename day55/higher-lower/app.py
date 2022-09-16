from flask import Flask, render_template
from random import randint, choice

app = Flask(__name__)
number_to_guess = randint(0,9)
no_list_gif = ["https://c.tenor.com/4YuXNYIdo5YAAAAd/smdh-smh.gif", "https://c.tenor.com/gpRFb5ZF_jkAAAAC/dog-no.gif", "https://c.tenor.com/2sC1lN-CT68AAAAC/no-nope.gif",
               "https://c.tenor.com/DsSjqbmG41AAAAAd/nope-no.gif", "https://c.tenor.com/5g3Xy2a3YkYAAAAd/no-way.gif", "https://c.tenor.com/g0QgLd5FiKsAAAAd/dog-triste.gif",
               "https://c.tenor.com/fZepmOuUwt4AAAAC/animals-really.gif", "https://c.tenor.com/mIxgU4p9FKAAAAAC/dog-pup.gif", "https://c.tenor.com/KCaa6xFkUs8AAAAC/friends-no-baby.gif"
               "https://c.tenor.com/zBf7p02Cm4IAAAAC/no-monica.gif", "https://c.tenor.com/ZpWBFy5vTtEAAAAd/wtf-omg.gif", "https://c.tenor.com/n_e2xEnPnpIAAAAC/no-game-of-thrones.gif"
               "https://c.tenor.com/R99VF90Z8MQAAAAd/varys-conleth-hill.gif", "https://c.tenor.com/7tedeJe-6d0AAAAC/chris-evans-captain-america.gif", "https://c.tenor.com/Aqr2XLpjemgAAAAC/spiderman-no-no-no.gif"
               "https://c.tenor.com/_WegcwQTkokAAAAC/robert-downey-jr-tony-stark.gif"]
no_list_text = ["You're wrong!", "No, you've got it wrong.", "That's wrong.", "I don't think you're right about that.", "Try again!", "I’m afraid you’re mistaken."]
yes_list_gif = ["https://c.tenor.com/tEOcw6Pg5z4AAAAC/jim-and.gif", "https://c.tenor.com/AzNJtG4GXToAAAAd/yes.gif", "https://c.tenor.com/w7xtCCEEW_kAAAAC/im-gonna-say-yes-simon-cowell.gif",
                "https://c.tenor.com/iV__D-FgJQQAAAAC/good-fine.gif", "https://c.tenor.com/y_qDvEaALjMAAAAC/spongebob-patrick-star.gif", "https://c.tenor.com/lnd_mwCqZ9IAAAAC/will-ferrell.gif",
                "https://c.tenor.com/t8E69GsoMuIAAAAC/winner-wordle.gif", "https://c.tenor.com/HAGXdX-X-1cAAAAC/no1-happy.gif", "https://c.tenor.com/b2ZykuqZ9KAAAAAC/a-winner-is-you-winner.gif",
                "https://c.tenor.com/QwyDTN_0AfAAAAAC/the-goon-win.gif", "https://c.tenor.com/I7qeNpfhcdEAAAAC/winner.gif"]
yes_list_text = ["champion", "genius", "master", "pro", "star", "winner"]


@app.route('/')
def index():
    return "<h1>Guess a number between 0 and 9</h1>" \
                "<img src='https://c.tenor.com/wpa3Z6uhBkgAAAAC/counting-calculating.gif' width='300'>"

@app.route('/<number>')
def view(number):
    if number_to_guess > int(number):
        return "<h1>it's too low</h1>" \
                        f"<img src={choice(no_list_gif)} width='300'>"
    elif number_to_guess < int(number):
        return "<h1>it's too high</h1>" \
                    f"<img src={choice(no_list_gif)} width='300'>"
    else:
        return "<h1>You win!</h1>" \
                    f"<p>Who are the {choice(yes_list_text)}?</p>" \
                    f"<img src={choice(yes_list_gif)} width='300'>" \
                    f"<h3>The number was {number_to_guess}!</h3>"


if __name__ == '__main__':
    app.run(debug=True)