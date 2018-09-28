# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from scrapy import log

class NovelPipeline(object):
    def __init__(self):
        self.path = '/home/parallels/Documents/scrapy/novel/my-novel.txt'
        self.file = open(self.path,'a')
        
 
    def process_item(self, item, spider):
        
        log.msg('receive item.',
                    level=log.DEBUG,spider=spider)
        self.file.write(item['chapter_name'] +'\n'+item['content']+'\n')
        return item

    def close_spider(self, spider):
        self.file.close()
