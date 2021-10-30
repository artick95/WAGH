from scrapy.spiders import SitemapSpider


class icobench(SitemapSpider):
    name = 'icobench'
    sitemap_urls = ['https://icobench.com/sitemap-ico.xml']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    #download_delay = 1.0

    def parse(self, response):
        
        print('########PAGE######SCRAPED###SUCCESSFULLY###########')
       
        data = {
            'title': response.css("title ::text").extract_first(),
            'url': response.url,
            'name': response.css('h1.notranslate::text').extract_first(),
            'short-description':
            response.css('div.name>h2::text').extract_first(),
            'website':
            response.css('a.button_big::attr(href)').extract_first(),
        }

        try:
            data['social0'] = response.css(
                'div.socials>a::attr(href)').extract()[0]
        except:
            data['social0'] = ''

        try:
            data['social1'] = response.css(
                'div.socials>a::attr(href)').extract()[1]
        except:
            data['social1'] = ''
        try:
            data['social2'] = response.css(
                'div.socials>a::attr(href)').extract()[2]
        except:
            data['social2'] = ''

        try:
            data['social3'] = response.css(
                'div.socials>a::attr(href)').extract()[3]
        except:
            data['social3'] = ''

        try:
            data['social4'] = response.css(
                'div.socials>a::attr(href)').extract()[4]
        except:
            data['social4'] = ''

        try:
            data['social5'] = response.css(
                'div.socials>a::attr(href)').extract()[5]
        except:
            data['social5'] = ''

        try:
            data['social6'] = response.css(
                'div.socials>a::attr(href)').extract()[6]
        except:
            data['social6'] = ''

        try:
            data['social7'] = response.css(
                'div.socials>a::attr(href)').extract()[6]
        except:
            data['social7'] = ''

        try:
            data['linkedin1'] = response.css('#team>div.row')[0].css(
                'a.linkedin::attr(href)').extract()[0]
        except:
            data['linkedin1'] = ''
        try:
            data['linkedin2'] = response.css('#team>div.row')[0].css(
                'a.linkedin::attr(href)').extract()[1]
        except:
            data['linkedin2'] = ''
        try:
            data['linkedin3'] = response.css('#team>div.row')[0].css(
                'a.linkedin::attr(href)').extract()[2]
        except:
            data['linkedin3'] = ''
        yield data
