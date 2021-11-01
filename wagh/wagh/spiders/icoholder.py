from scrapy.spiders import SitemapSpider
import scrapy


class icoholder(SitemapSpider):
    name = "icoholder"
    sitemap_urls = ["https://icobench.com/sitemap-ico.xml"]
    sitemap_follow = ["/icos/"]
    sitemap_rules = [
        ("/ico/", "parse"),
    ]
    user_agent = "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots"

    def parse(self, response):
        domain = "https://icoholder.com"
        urls_icos = response.css("div.ico-list-name-d>h3>a::attr(href)").extract()
        next_page_links = response.css(
            'div.navigation>ul.pagination>li>a[rel="next"]::attr(href)'
        ).get()

        for next_page_link in next_page_links:
            if next_page_link is not None:
                for url_ico in urls_icos:
                    ico_page = domain + url_ico
                    yield response.follow(ico_page, callback=self.ico_details)
                yield response.follow(next_page_link, callback=self.parse)

    def ico_details(self, response):

        print("########PAGE######SCRAPED###SUCCESSFULLY###########")

        data = {
            "title": response.css("title ::text").extract_first(),
            "url": response.url,
            "name": response.css("h1.notranslate::text").extract_first(),
            "short-description": response.css("div.name>h2::text").extract_first(),
            "website": response.css("a.button_big::attr(href)").extract_first(),
        }

        try:
            data["social0"] = response.css("div.socials>a::attr(href)").extract()[0]
        except:
            data["social0"] = ""

        try:
            data["social1"] = response.css("div.socials>a::attr(href)").extract()[1]
        except:
            data["social1"] = ""
        try:
            data["social2"] = response.css("div.socials>a::attr(href)").extract()[2]
        except:
            data["social2"] = ""

        try:
            data["social3"] = response.css("div.socials>a::attr(href)").extract()[3]
        except:
            data["social3"] = ""

        try:
            data["social4"] = response.css("div.socials>a::attr(href)").extract()[4]
        except:
            data["social4"] = ""

        try:
            data["social5"] = response.css("div.socials>a::attr(href)").extract()[5]
        except:
            data["social5"] = ""

        try:
            data["social6"] = response.css("div.socials>a::attr(href)").extract()[6]
        except:
            data["social6"] = ""

        try:
            data["social7"] = response.css("div.socials>a::attr(href)").extract()[6]
        except:
            data["social7"] = ""

        try:
            data["linkedin1"] = (
                response.css("#team>div.row")[0]
                .css("a.linkedin::attr(href)")
                .extract()[0]
            )
        except:
            data["linkedin1"] = ""
        try:
            data["linkedin2"] = (
                response.css("#team>div.row")[0]
                .css("a.linkedin::attr(href)")
                .extract()[1]
            )
        except:
            data["linkedin2"] = ""
        try:
            data["linkedin3"] = (
                response.css("#team>div.row")[0]
                .css("a.linkedin::attr(href)")
                .extract()[2]
            )
        except:
            data["linkedin3"] = ""
        yield data
