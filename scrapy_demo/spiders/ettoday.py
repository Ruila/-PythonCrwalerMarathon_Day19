import scrapy
from scrapy_demo.items import ScrapyDemoItem

class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.html','https://www.ettoday.net/news/20210120/1902773.html']

    def parse(self, response):
        item = ScrapyDemoItem()
        for v in response.css('p::text'):
        # print(v.extract(), '\n')
         item['text'] = v.extract()
         yield item
