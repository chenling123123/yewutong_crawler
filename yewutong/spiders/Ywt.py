# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup
from yewutong.items import YewutongItem

class YwtSpider(scrapy.Spider):
    name = 'Ywt'
    start_urls = []
    start_url='http://win.madeinchina.cn/YellowPages01_revise.aspx?p='
    last_url='&keys=%%E6%9C%89%%E9%99%90%%E5%85%AC%%E5%8F%B8%&begintime=2018-01-01&proname=%E6%B1%9F%E8%8B%8F&cityname=%E7%9B%90%E5%9F%8E%E5%B8%82&endtime=2018-05-09'
    cookie={
        'ASP.NET_SessionId':'jihndrzcs2aev2ej5kxk1gxh'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    def start_requests(self):
        for i in range(1,654):
            url=self.start_url+str(i)+self.last_url
            yield Request(url=url,cookies=self.cookie, callback=self.parse)

    def parse(self, response):
        item=YewutongItem()
        selector = Selector(response)
        text0=selector.extract()
        soup = BeautifulSoup(text0,'lxml')
        divs=soup.find_all(attrs = {'style':'margin-left :23px'})

        for div in divs:
            list=[]
            item["name"]=div.find('a').text
            item["creating_date"]=str(div).split('成立时间：')[1].split('\r\n')[0]
            item["address_img_url"]="http://win.madeinchina.cn/"+div.find(id='img1').get('src')
            item["phone_img_url"]="http://win.madeinchina.cn/"+div.find(id='img2').get('src')
            list.append(item["address_img_url"])
            list.append(item["phone_img_url"])
            item["img_urls"]=list
            item["img_urls"]=','.join(item["img_urls"])
            yield item


