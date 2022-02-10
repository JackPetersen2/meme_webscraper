from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests
import re

app = Flask(__name__)


urls=['https://www.reddit.com/']



@app.route('/')
def home():
  for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
    images = soup.find_all('img')

    for image in images:
      x = image['src']

      print(x)
      return render_template("index.html", x=x)

    return render_template("index.html", memes=images)
if __name__ == '__main__':
  app.run()











