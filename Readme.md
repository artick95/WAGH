
-fix dates and goals for the last session --> importdata from sheets
-make script to scrape ICO website of each
-once they go live scrape the market cap and trading volume

https://coinmarketcap.com/it/ico-calendar/upcoming/



https://icodrops.com/category/upcoming-ico/
https://icodrops.com/category/active-ico/
https://icodrops.com/category/ended-ico/


✔️https://icobench.com/icos


Cannot find where is the data in here -->
https://www.coingecko.com/en/api/documentation


pip install shub
shub login
API key: 4c210cbc255d48278ba5e367cb67f02d
shub deploy 564603


https://docs.zyte.com/scrapy-cloud/items.html#
curl -u 4c210cbc255d48278ba5e367cb67f02d: https://storage.scrapinghub.com/items/564603/2/6
curl -u 4c210cbc255d48278ba5e367cb67f02d: https://storage.scrapinghub.com/jobq/564603/list
curl -u 4c210cbc255d48278ba5e367cb67f02d: https://app.scrapinghub.com/api/run.json -d project=564603 -d spider=toscrape-xpath