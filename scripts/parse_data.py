import os
import json
import re

files_paths = ["data/crawl_zalando.nl_2016-05-30T23-14-36.jl"]

import json_lines
import re
from bs4 import BeautifulSoup


def remove_tags(tags, html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    for s in soup(tags):
        s.decompose()
    return str(soup)



def selectProductList(html_doc):
    css_soup = BeautifulSoup(html_doc, "html.parser")
    return css_soup.select("li.catalogArticlesList_item")

def select_text(html_doc, element, is_price = False):
    css_soup = BeautifulSoup(html_doc, "html.parser")
    string = str(css_soup.select(element)[0].find(text=True))
    if is_price:
        return ''.join(e for e in string if e.isnumeric() or e == ',')
    return  ''.join(e for e in string if e.isalnum() or e == ',' or e == ' ')

def select_sizes(html_doc):
    css_soup = BeautifulSoup(html_doc, "html.parser")
    sizes = list(map(lambda a: a.find(text=True), BeautifulSoup(str(css_soup.select('div.catalogArticlesList_sizeInfo'))).select('a')))
    return sizes

def get_href(html_doc, element):
    css_soup = BeautifulSoup(html_doc, "html.parser")
    return css_soup.select(element)


def get_brands():
    with open(files_paths[0], 'rb') as f:
        data = []
        items = json_lines.reader(f)
        for item in items:
            if item['page_type'] == 'product_listing':
                html_doc = item['body']
                cleaned_doc = remove_tags(['script', 'style', 'head', 'noscript', 'iframe', 'path', 'svg'], html_doc) 
                list_items = selectProductList(cleaned_doc)

                for item in list_items:
                    list_item = str(item)
                    item_brand = select_text(list_item, 'div.catalogArticlesList_brandName')
                    data.append(item_brand)
                yield data


def get_products():
    with open(files_paths[0], 'rb') as f:
        items = json_lines.reader(f)
        for item in items:
            data = []
            if item['page_type'] == 'product_listing':
                html_doc = item['body']
                cleaned_doc = remove_tags(['script', 'style', 'head', 'noscript', 'iframe', 'path', 'svg'], html_doc) 
                list_items = selectProductList(cleaned_doc)

                for item in list_items:
                    list_item = str(item)
                    item_price = select_text(list_item, 'div.catalogArticlesList_price', True)
                    item_brand = select_text(list_item, 'div.catalogArticlesList_brandName')
                    item_name = select_text(list_item, 'div.catalogArticlesList_articleName')
                    item_sizes = select_sizes(list_item)
                    item_href = get_href(list_item, "a.catalogArticlesList_productBox")
                    links = [] 
                    for a in item_href:
                        links.append(a['href'])
                    data.append({
                        "brand": item_brand, 
                        "name": item_name,
                        "price": float(item_price.replace(',', '.')),
                        "sizes": item_sizes, 
                        "links": links
                    })
                yield data
