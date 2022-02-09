from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests
import re

app = Flask(__name__)


urls=['https://www.reddit.com/r/Offensivejokes/']



@app.route('/')
def home():
  for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')


    memes = soup.findAll('img',class_='ImageBox-image')

    print(soup.prettify())


    print(memes)


    return render_template("index.html", memes=memes)
if __name__ == '__main__':
  app.run()








