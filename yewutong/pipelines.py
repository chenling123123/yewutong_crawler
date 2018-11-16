# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from yewutong.models_sql import Ywt,engine
from sqlalchemy.orm import sessionmaker
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import copy
from scrapy.exceptions import DropItem
from yewutong.items import YewutongItem


class YewutongPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        print(item,123123)
        asynItem = copy.deepcopy(item)
        print(asynItem,234234)
        for image_url in item['img_urls']:
            print(image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        asynItem = copy.deepcopy(item)
        print(item,4444444444)
        print(asynItem,55555555555)
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        pic_list = []
        for v in image_paths:
            pic_list.append(v)
        item["img_urls"]=pic_list
        item["img_urls"]=','.join(item["img_urls"])
        return item


class YewutongPipeline1(object):
    def process_item(self, item, spider):
        self.session.add(Ywt(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


# class MyImagesPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         for image_url in item['img_urls']:
#             yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#
#         return item