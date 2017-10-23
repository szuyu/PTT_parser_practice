#-*- coding: utf-8 -*-
"""cd /Users/Sean/Documents/ptt_parser"""
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
from urlparse import urljoin

"""""--------------parser-----------------"""""
INDEX = 'https://www.ptt.cc/bbs/Nurse/index.html'

def get_posts_on_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all('div', 'r-ent')

    posts = list()
    for article in articles:
        try:
            meta = article.find('div', 'title').find('a')
            posts.append({
                'title': meta.getText().strip(),
                'link': meta.get('href'),
                'push': article.find('div', 'nrec').getText(),
                'date': article.find('div', 'date').getText(),
                'author': article.find('div', 'author').getText(),
            })
        except: 
            """print("本文已刪除")"""

    next_page = soup.find('div', 'btn-group-paging').find_all('a', 'btn')
    next_link = next_page[1].get('href')
    return posts, next_link

def get_pages(num):
    page_url = INDEX
    print(page_url)
    all_posts = list()
    for i in range(num):
        posts, link = get_posts_on_page(page_url)
        """print(posts, link)"""
        all_posts += posts
        """print(all_posts)"""
        page_url = urljoin(INDEX, link)
    return all_posts

if __name__ == '__main__':
    pages = 5
    for post in get_pages(pages):
        print(post['title'], post['date'], post['author'])





         
    

    
