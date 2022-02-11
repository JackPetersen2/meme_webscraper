from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests
import re

app = Flask(__name__)

urls=[
  'https://www.reddit.com/r/meme/',
]



@app.route('/')
def home():
  for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    images = soup.find_all('img')
    videos = soup.find_all('source')

    video_container=[]

    for video in videos:
      x=video['src']
      video_container.append(x)


    image_container=[]
    for image in images:
      x = image['src']
      image_container.append(x)


    return render_template("index.html", memes=images, images=image_container, videos=video_container)

if __name__ == '__main__':
  app.run()











