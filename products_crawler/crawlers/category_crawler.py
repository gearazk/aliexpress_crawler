import re

import sys
from pprint import pprint
from random import randint

from products_crawler.crawlers.base_crawler import BaseCrawler


class CategoryCrawler(BaseCrawler):
    
    
    def __init__(self,category_url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.category_url = category_url
        
        
    def _crawl_now(self):
        
        reps = self._get(self.category_url)
        
        pprint(reps.request.headers)
        print(reps.request.url)
        
        # f = open('ali.html','w')
        # f.write(reps.text)
        # f.close()
        tree = self.parser(reps.text)

        products = self._extract_products(tree)
        return products
    
    def _extract_products(self,tree):
        
        products = []
        for node in tree.select('#list-items li'):
            # print(node)
            try:
                id          = node.select_one('input.atc-product-id').get('value').strip()
                url         = node.select_one('a.product')['href']
                name        = node.select_one('a.product').getText().strip()
                image_url   = node.select_one('img.picCore')
                image_url   = image_url.get('image-src',image_url.get('src',''))
                price       = node.select_one('[itemprop="price"]').getText().replace('US $','').split('-')[0]
                order_count = node.select_one('em').getText()
                order_count = re.findall('\((.*?)\)',order_count)[0]
                store       = node.select_one('.store').getText().strip()
                store_url   = node.select_one('a.store').get('href')
                
                if int(order_count) < 5:
                    continue
            except Exception as e:
                print('Error: %s'%e)
                sys.exc_info()
                continue
                
            p = {
                'product_id'    :id,
                'name'          :name,
                'url'           :url,
                'image_url'     :image_url,
                'price'         :price,
                'order_count'   :order_count,
                'store_name'    :store,
                'store_url'     :store_url,
            }
            # print(p)
            products.append(p)
        
        return products