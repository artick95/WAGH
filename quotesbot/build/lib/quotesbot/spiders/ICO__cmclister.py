
# -*- coding: utf-8 -*-
import scrapy
import re


class ToScrapeCSSSpider(scrapy.Spider):
    name = "ICO__cmclister"
    start_urls = [
        'https://www.coinmarketcap.com/en/ico-calendar/upcoming/',
    ]

    def parse(self, response):
        ICOs =  response.xpath('//tbody/tr[*]')
        domain='https://coinmarketcap.com'


        for ICO in ICOs:
            data= {
                'icoName': ICO.css('span.bogImm::text').extract_first(),
                'urlCMC':domain + ICO.css('a.cmc-link::attr(href)').extract()[0],
                'url':'',
                'stage': ICO.css('span.gbZOJJ::text').extract_first(),
                # 'StartDate':ICO.css('td::text').extract()[0],
                'StartDate': '',
                'EndDate':'',
                'Goal':''
                # 'EndDate':ICO.css('td::text').extract()[1],
                # 'Goal':ICO.css('td::text').extract()[2],
            }
            try:
                data['StartDate']=ICO.css('td::text').extract()[0]
            except:
                data['StartDate']='----'
            
            try:
                data['EndData']=ICO.css('td::text').extract()[1]
            except:
                data['EndData']='----'

            try:
                data['Goal']=ICO.css('td::text').extract()[2]
            except:
                data['Goal']='----'

            data['url']= scrapy.Request(url=data['urlCMC'],callback=self.parseResoveURLs)
            yield data

    def parseResoveURLs(self, response):
        # return (response.css('a.link-button::attr(href)').extract_first()).ToString()
        return (response.css('a.link-button::attr(href)').extract_first())
        # return (re.search("(?P<url>https?://[^\s]+)",response.css('a.link-button::attr(href)').extract_first())).group("url")
        
        



