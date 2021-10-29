
# -*- coding: utf-8 -*-
import scrapy



class icobenchSpider(scrapy.Spider):
    name = "icobench"
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    page_number=1
    start_urls = [
        'https://icobench.com/icos?page=1',
    ]

    def parse(self, response):
        domain='https://icobench.com'
        table=response.css('div.ico_list> table')
        rows = table.xpath('//tr')

        i=0
        for row in rows:   
          print('################'+ str(i)+'##############')
          data = {
            'name':row.css('a.name::text').extract_first(),
          }
          
          try:
            data['icobenchURL']=domain + row.css('a.name::attr(href)').extract()[0]
          except:
            data['icobenchURL']='-'
            
          try:
              data['StartDate']=row.css('td.rmv::text').extract()[0]
          except:
              data['StartDate']='-'
          try:
              data['endDate']=row.css('td.rmv::text').extract()[1]
          except:
              data['endDate']='-'
          
          i+=1 
          yield data

          next_page= 'https://icobench.com' + response.css('a.next::attr(href)').extract_first()
          
          #if next_page is not None:
          if icobenchSpider.page_number<12:
            print('I AM HERE ################'+str(icobenchSpider.page_number))
            icobenchSpider.page_number=icobenchSpider.page_number+1
            yield response.follow(next_page,callback=self.parse)


    
  




#pip install scrapy
# scrapy shell -s user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' https://icobench.com/icos



# scrapy shell -s user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' https://icobench.com/ico/tycoon
#domain='https://icobench.com/icos'
#table=response.css('div.ico_list> table')
#rows = table.xpath('//tr')
#row=rows[1]