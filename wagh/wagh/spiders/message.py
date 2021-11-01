# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor


class message(scrapy.Spider):
    name = "message"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"

    start_urls = [
        "https://coinmarketcap.com/ico-calendar/upcoming/",
    ]

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_ico,
                endpoint="render.json",
                args={"har": 1, "html": 1,"wait":8},
            )

    def parse_ico(self, response):

        data = {
            "name": response.css("div.nameHeader>h2::text").extract_first(),
            "website": response.css("a.link-button::attr(href)").extract_first(),
        }

        try:
            data["dateStart"] = (
                response.css("div.stage-header-date>span::text")
                .get()
                .split(",")[0]
                .split(" - ")[0]
            )

        except:
            data["dateStart"] = ""
        yield data

        try:
            data["dateEnd"] = (
                response.css("div.stage-header-date>span::text")
                .get()
                .split(",")[0]
                .split(" - ")[1]
            )
        except:
            data["dateEnd"] = ""
        try:
            data["timeToMarket"] = (
                response.css("div.stage-header-date>span::text").get().split(",")[1]
            )
        except:
            data["timeToMarket"] = ""

        # fetch('http://localhost:8050/render.html?url=https://coinmarketcap.com/it/currencies/galatic-arena/ico/')

        # Scraping the detailTable
        cell = response.css("div.detailTable>div")

        try:
            data["tokens4Sale"] = cell[0].css("span::text").extract()[1]
        except:
            data["tokens4Sale"] = ""
        try:
            data["tokensSold"] = cell[1].css("span::text").extract()[1]
        except:
            data["tokensSold"] = ""
        try:
            data["ICOprice"] = cell[2].css("span::text").extract()[1]
        except:
            data["ICOprice"] = ""
        try:
            data["where2Buy"] = cell[3].css("span::text").extract()[1]
        except:
            data["where2Buy"] = ""
        try:
            data["softCap"] = cell[4].css("span::text").extract()[1]
        except:
            data["softCap"] = ""
        try:
            data["percentaceOfTotalSupply"] = cell[5].css("span::text").extract()[1]
        except:
            data["percentaceOfTotalSupply"] = ""
        try:
            data["fundraisingGoal"] = cell[6].css("span::text").extract()[1]
        except:
            data["fundraisingGoal"] = ""
        try:
            data["Accept"] = cell[7].css("span::text").extract()[1]
        except:
            data["Accept"] = ""
        try:
            data["personalCap"] = cell[8].css("span::text").extract()[1]
        except:
            data["personalCap"] = ""
        try:
            data["Access"] = cell[9].css("span::text").extract()[1]
        except:
            data["Access"] = ""

        # Finance Info
        # fetch('http://localhost:8050/render.html?url=https://coinmarketcap.com/currencies/moonriver/ico/')

        try:
            data["priceValue"] = response.css("div.priceValue::text").get()
        except:
            data["priceValue"] = ""

        stats = response.css("div.statsValue::text").extract()
        try:
            data["MarketCapStat"] = stats[0]
        except:
            data["MarketCapStat"] = ""

        try:
            data["fullDilutitedMarketCap"] = stats[1]
        except:
            data["fullDilutitedMarketCap"] = ""

        try:
            data["Volume24h"] = stats[2]
        except:
            data["Volume24h"] = ""

        try:
            data["volume2MarketcapRatio"] = stats[3]
        except:
            data["volume2MarketcapRatio"] = ""

        try:
            data["circulatingSupply"] = stats[4]
        except:
            data["circulatingSupply"] = ""

        # Social Info
        try:
            data["social1"] = response.css("a.modalLink::attr(href)").extract()[1]
        except:
            data["social1"] = ""

        try:
            data["social2"] = response.css("a.modalLink::attr(href)").extract()[2]
        except:
            data["social2"] = ""

        try:
            data["social3"] = response.css("a.modalLink::attr(href)").extract()[3]
        except:
            data["social3"] = ""

        try:
            data["social4"] = response.css("a.modalLink::attr(href)").extract()[4]
        except:
            data["social4"] = ""

        try:
            data["social5"] = response.css("a.modalLink::attr(href)").extract()[5]
        except:
            data["social5"] = ""
        try:
            data["social6"] = response.css("a.modalLink::attr(href)").extract()[6]
        except:
            data["social6"] = ""
        yield data

