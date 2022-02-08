from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests

app = Flask(__name__)


url = requests.get('https://www.reddit.com/r/Offensivejokes/').text

soup = BeautifulSoup(url,'lxml')

@app.route('/')
def home():

  memes = soup.find_all('div', class_='Post')
  image_container=[]
  for meme in memes:
    image=meme.find('img')
  image.append(image)


  return render_template("index.html", content=memes,image=image)
if __name__ == '__main__':
  app.run()


