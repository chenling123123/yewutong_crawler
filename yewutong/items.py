# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class YewutongItem(Field):
    name = Field()
    creating_date = Field()
    address_img_url = Field()
    phone_img_url = Field()
    img_urls = Field()
    images = scrapy.Field()
