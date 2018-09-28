import scrapy
from .. import items
from urlparse import urlparse
from urlparse import urljoin
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class NovelSpider(scrapy.Spider):
    name = "novel"
    origin_url ='https://www.piaotian.com/html/8/8290/5171544.html'
    render_url = 'http://127.0.0.1:8050/render.html'
    start_urls = [
        #"https://www.piaotian.com/html/8/8290/5171544.html"
        'http://127.0.0.1:8050/render.html?url=https://www.piaotian.com/html/8/8290/5171544.html'
    ]

    def parse(self, response):
        chapter_name = response.xpath('//h1/child::text()').extract_first()
        next_url = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "bottomlink", " " ))]//a[last()]/@href').extract_first()
        next_url = urljoin(self.origin_url, next_url)
        content = response.xpath('//*[@id="content"]/child::text()').extract()
        print dir(content)
        print type(content)
        item = items.NovelItem()
        item['chapter_name'] = chapter_name
        item['url'] = next_url 
        item['content'] = '\n'.join(content) 
        #print '\n'.join(content), chapter_name
        yield item 
        if next_url.find('index.html') > -1:
            print('mission finish.')
        else:
            yield scrapy.Request(self.render_url + '?url=' + next_url, callback=self.parse)
        #yield scrapy.Request(self.render_url + '?url=' + next_url, callback=self.parse) 
