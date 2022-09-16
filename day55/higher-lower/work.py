links = ["https://tenor.com/view/counting-calculating-math-fingers-1234-gif-22565275",
         "https://media.giphy.com/media/",
         "dfgdfg"]

with open("static/gif/gifs.csv", "w") as f:
    for link in links:
        f.write(link+ "\n")
