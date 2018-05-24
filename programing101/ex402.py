import requests
from bs4 import BeautifulSoup

def get_rating(text):
    key_index = text.index('data-rating')
    return text[key_index+13:key_index+14]

def space_append(s, n):
    while len(s) < n:
        s += ' '
    return s    

def get_item(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    item_list = list()
    for i in soup.find_all(class_='thumbnail'):
        title = space_append(i.find(class_='title').text, 20)
        price = space_append(i.find(class_='price').text, 10)
        stars = space_append(get_rating(str(i)), 7)
        review = space_append(i.find('p', {'class': 'pull-right'}).text[:2], 6)
        item = [title, price, stars, review]
        item_list.append(item)
    return item_list

def main(url):
    url_home = url
    item_all_list = list()
    title = space_append('Name', 20)
    price = space_append('Price', 10)
    stars = space_append('Stars', 7)
    reviews = space_append('Reviews', 6)
    head = [title, price, stars, reviews]
    item_all_list.append(head)
    keyword_list =  ['/computers/laptops', '/computers/tablets', '/phones/touch']
    for i in keyword_list:
        url_item = url_home + i
        item_list = get_item(url_item)
        for j in item_list:
            item_all_list.append(j)
    for i in item_all_list:
        output_str = ''
        for j in i:
            output_str += j
        print(output_str)

main(input())