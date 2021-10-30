
# -*- coding: utf-8 -*-
import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "coinmarketcap"

    #Input = Start Urls
    start_urls = [
        'https://coinmarketcap.com/ico-calendar/upcoming/',
    ]

    def parse(self, response):
        domain="https://www.coinmarketcap.com"
        urls_end = response.css('table.cmc-table>tbody>tr>td>a::attr(href)').extract()

        for url in urls_end: 
          next_page=domain+url
          yield response.follow(next_page,callback=self.ico_details)

    def ico_details(self,response):
      data={
        'name':response.css('div.nameHeader>h2::text').extract_first(),
        'website':response.css('a.link-button::attr(href)').extract_first(),
      }
      try:
            data['social1'] = response.css('a.modalLink::attr(href)').extract()[1]
      except:
            data['social1'] = ''

      try:
            data['social2'] = response.css('a.modalLink::attr(href)').extract()[2]
      except:
            data['social2'] = ''

      try:
          data['social3'] = response.css('a.modalLink::attr(href)').extract()[3]
      except:
            data['social3'] = ''

      try:
            data['social4'] = response.css('a.modalLink::attr(href)').extract()[4]
      except:
            data['social4'] = ''

      try:
            data['social5'] = response.css('a.modalLink::attr(href)').extract()[5]
      except:
            data['social5'] = ''
      try:
            data['social6'] = response.css('a.modalLink::attr(href)').extract()[6]
      except:
            data['social6'] = ''   
      yield data   
