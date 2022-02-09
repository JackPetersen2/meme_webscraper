from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests
import re

app = Flask(__name__)


urls=['https://mui.com/components/material-icons/']



@app.route('/')
def home():
  for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')


    memes = soup.find_all('li', class_='css-cd6vjr')
    
    print(soup.prettify())


    print(memes)

    return render_template("index.html", memes=memes)
if __name__ == '__main__':
  app.run()





