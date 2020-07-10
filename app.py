from detik_scrapper import popular

#Lists => data = [1, '1']
#Tuples => data = (1, '1')
#Dictionary => data = {'1': 1, 'b': '2'}

url = 'https://www.detik.com/terpopuler'
param = {
  'key': 'tag_from',
  'value': 'wp_cb_mostPopular_more'
}

popularNews = popular(param = param, url = url)

# print(popularNews)


for title in popularNews:
  print(title.find('a').find('img')['title'])
