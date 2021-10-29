
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider



class icobenchSpider(SitemapSpider):
    name = "icobench"
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    sitemap_urls = ['https://icobench.com/ico/crowdforce']
    sitemap_rules=[]
    DOWNLOAD_DELAY = 10 
    #page_number=1
    #start_urls = [  'https://icobench.com/ico/crowdforce']

    def parse(self, response):
        table= response.css('table.financial_data')
        rows=response.css('table.financial_data> div.data_row')
        data = {
          'name':response.css('h1.notranslate::text').extract_first(),
          'short-description':response.css('div.name>h2::text').extract_first(),
          'website':response.css('a.button_big::attr(href)').extract_first(),
        }


        try:
          data['social1']=response.css('div.socials>a::attr(href)').extract()[0]
        except:
          data['social1']=''

        try:
          data['social1']=response.css('div.socials>a::attr(href)').extract()[1]
        except:
          data['social1']=''
        try:
          data['social2']=response.css('div.socials>a::attr(href)').extract()[2]
        except:
          data['social2']=''
        
        try:
          data['social3']=response.css('div.socials>a::attr(href)').extract()[3]
        except:
          data['social3']=''

        try:
          data['social4']=response.css('div.socials>a::attr(href)').extract()[4]
        except:
          data['social4']=''   


        try:
          data['social5']=response.css('div.socials>a::attr(href)').extract()[5]
        except:
          data['social5']=''

        try:
          data['social6']=response.css('div.socials>a::attr(href)').extract()[6]
        except:
          data['social6']=''

        try:
          data['social7']=response.css('div.socials>a::attr(href)').extract()[6]
        except:
          data['social7']=''

        try:
          data['linkedin1']=response.css('#team>div.row')[0].css('a.linkedin::attr(href)').extract()[0]
        except:
          data['linkedin1']=''
        try:
          data['linkedin2']=response.css('#team>div.row')[0].css('a.linkedin::attr(href)').extract()[1]
        except:
          data['linkedin2']=''
        try:
          data['linkedin3']=response.css('#team>div.row')[0].css('a.linkedin::attr(href)').extract()[2]
        except:
          data['linkedin3']=''
        yield data





#pip install scrapy
# scrapy shell -s user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' https://icobench.com/icos


# scrapy shell -s user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' https://icobench.com/ico/crowdforce


# scrapy shell -s user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' https://icobench.com/ico/tycoon
#domain='https://icobench.com/icos'
#table=response.css('div.ico_list> table')
#rows = table.xpath('//tr')
#row=rows[1]

#https://icobench.com/sitemap-ico.xml