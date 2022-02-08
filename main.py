from bs4 import BeautifulSoup
from flask import Flask,render_template
import requests

app = Flask(__name__)

urls=['','']

@app.route('/')
def home():
  for url in  urls:
  response=requests.git(url)
  soup=BeautifulSoup(response.content,'lxml')
  

  memes = soup.find_all('div', class_='Post')
  
    for meme in memes:
      image=meme.find('img')
    image.append(image)


  return render_template("index.html", content=memes,image=image)

if __name__ == '__main__':
  app.run()


