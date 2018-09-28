import scrapy
from urlparse import urlparse
from urlparse import urljoin
from scrapy_splash import SplashRequest
from scrapy.http.headers import Headers

class NovelSpider(scrapy.Spider):
    name = "novel_js"
    start_urls = [
        "https://www.piaotian.com/html/8/8290/5171544.html"
    ]
    def start_requests(self):
        for url in self.start_urls:
            rest = SplashRequest(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })
            print type(rest) 
            yield rest
    def parse(self, response):
        chapter_name = response.xpath('//h1/child::text()').extract_first()
        next_url = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "bottomlink", " " ))]//a[last()]/@href').extract_first()
        next_url = urljoin(response.url, next_url)
        content = response.xpath('//*[@id="content"]/child::text()').extract_first()
        print chapter_name,next_url,content
        print response.encoding
        print response.body.decode('utf-8').encode('gbk') 
        print type(response.body)
