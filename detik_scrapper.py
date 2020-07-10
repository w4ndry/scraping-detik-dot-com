import requests
from bs4 import BeautifulSoup

def popular(**kwargs):
  html_doc = requests.get(kwargs['url'], params={" + kwargs['param']['key'] +":"+ kwargs['param']['value'] + "})

  soup = BeautifulSoup(html_doc.text, 'html.parser')

  popular_area = soup.find(attrs={'class': 'grid-row list-content'})

  titles = popular_area.findAll(attrs={'class': 'media__title'})
  images = popular_area.findAll(attrs={'class': 'media__image'})

  return images
