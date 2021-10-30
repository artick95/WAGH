
# -*- coding: utf-8 -*-
import scrapy



class ToScrapeCSSSpider(scrapy.Spider):
    name = "coinmarketcap"

    #Input = Start Urls
    start_urls = [
        'https://www.coinmarketcap.com/en/ico-calendar/upcoming/',
    ]

    def parse(self, response):
        table =  response.css('table.cmc-table>tbody>trtd>a::attr(href)').extract
        rows=table.css('tbody>tr')
        domain='https://coinmarketcap.com/en'


        for row in rows:
            data= {
                'icoName': row.css('span.bogImm::text').extract_first(),
                'urlCMC':domain + row.css('td>a::attr(href)').extract_first(),
                'url':'',
                'stage': row.css('span.gbZOJJ::text').extract_first(),
                'StartDate': '',
                'EndDate':'',
                'Goal':''
            }

            try:
                data['StartDate']=row.css('td::text').extract()[0]
            except:
                data['StartDate']='----'
            
            try:
                data['EndDate']=row.css('td::text').extract()[1]
            except:
                data['EndDate']='----'

            try:
                data['Goal']=row.css('td::text').extract()[2]
            except:
                data['Goal']='----'


            urlsToResolve= data['urlCMC']
            i=0
            #FOR LOOP HERE TO GO IN EACH PAGE
            for urlToResolve in urlsToResolve:
              print('###############URL TO RESOLVE#################'+urlsToResolve[i]+'############################')
              data['url'][i]=scrapy.Request(url=urlToResolve,callback=self.parseResoveURLs)
              i=i+1
                 
            yield data

    def parseResoveURLs(self, response):
        return (response.css('a.link-button::attr(href)').extract_first())



