from scrapy.spiders import SitemapSpider

class AppleSpider(SitemapSpider):
    name = 'apple-spider'
    sitemap_urls = ['https://icobench.com/sitemap-ico.xml']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    download_delay = 5.0
    def parse(self, response):
        yield {
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }