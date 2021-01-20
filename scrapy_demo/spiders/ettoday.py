import scrapy


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.html']

    def parse(self, response):
        for v in response.css('p::text').extract():
         print(v, '\n')
