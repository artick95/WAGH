import scrapy
from scrapy_splash import SplashRequest

class applSpider(scrapy.Spider):
    start_urls = ["http://apple.com"]
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        response.css('div.cta-links>a::attr(href)')[1]