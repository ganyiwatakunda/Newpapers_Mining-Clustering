import scrapy

class Telegraph(scrapy.Spider):
    name = "newyorktimes_spider"
    allowed_domains = ["nytimes.com"]
    start_urls = [
        "https://www.nytimes.com/"
    ]

    def parse(self, response):
        categories_to_scrap = ['politics', 'sport', 'business', 'arts']






# List of categories
# response.css('header > div.css-1d8a290 > ul > li > a::text').getall()

# Get links to articles
# Section 1: response.css('ol > li > article > div > h2 > a::attr(href)').getall()
# Section 2:  response.css('ol > li > div > div.css-1l4spti > a::attr(href)').getall()

# Get heading 
# response.css('header > div.css-1vkm6nb > h1::text').get()

# Get story
# response.css('#story > section > div.css-1fanzo5  > div > p::text').getall()
