import scrapy

class Telegraph(scrapy.Spider):
    name = "newyorktimes_spider"
    allowed_domains = ["foxnews.com"]
    start_urls = [
        "https://www.foxnews.com/"
    ]

    def parse(self, response):
        categories_to_scrap = ['politics', 'sport', 'business', 'arts']




# List of categories
# response.css('#main-nav > ul > li > a::text').getall()

# Get links to articles
# Section 1: response.css('div.info > header > h2 > a::attr(href)').getall()
# Section 2: response.css('div.info > header > h4 > a::attr(href)').getall()

# Get heading 
# response.css('main > article > header > h1::text').get())

# Get story
# response.css(' div.article-content > div.article-body > p::text').getall()
