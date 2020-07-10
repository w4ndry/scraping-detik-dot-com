from flask import Flask, render_template
from detik_scrapper import popular

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/detik-popular')
def detik_popular():
  url = 'https://www.detik.com/terpopuler'
  param = {
    'key': 'tag_from',
    'value': 'wp_cb_mostPopular_more'
  }

  popularNews = popular(param = param, url = url)

  return render_template('index.html', popular=popularNews)


if __name__ == "__main__":
  app.run(debug=True)
