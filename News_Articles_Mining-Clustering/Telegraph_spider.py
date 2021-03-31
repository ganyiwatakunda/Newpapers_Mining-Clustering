import scrapy

class Telegraph(scrapy.Spider):
    name = "telegraph_spider"
    allowed_domains = ["telegraph.co.uk"]
    start_urls = [
        "https://www.telegraph.co.uk"
    ]

    def parse(self, response):
        categories_to_scrap = ['politics', 'sport', 'business', 'culture']

        news_categories = response.css('div.site-header__primary-navigation-wrapper > div > nav > ul > li > a::attr(href)').getall()

        for category in news_categories:
            if category.split("/")[1] in categories_to_scrap:
                category_url = response.url + category
                print(category_url)

                yield scrapy.Request(category_url, callback=self.parse_articles, cb_kwargs=dict(category=category.split("/")[1]))

    def parse_articles(self, response, category):
        article_urls = response.css('section > ul > li > article > div.card__content > h3 > a::attr(href)').getall()
        
        for url in article_urls:
            article_url = "https://www.telegraph.co.uk" + url
            print(article_url)

            yield scrapy.Request(article_url, callback=self.parse_story, cb_kwargs=dict(category=category, url=article_url))


    def parse_story(self, response, category, url):
        heading = response.css('article > header > h1::text').get()
        subheading = response.css('article > header > p::text').get()
        author = response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--header-meta.article__separator > div > span > span > a > span.e-byline__author::text').get()
        datetime = response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--header-meta.article__separator > div > time::text').get()
        article = response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--content > div:nth-child(1) > div.articleBodyText.section > div.component.article-body-text > p::text').getall()

        article = ' '.join([paragraph for paragraph in article])

        yield dict(url=url, category=category, heading=heading, subheading=subheading, author=author, datetime=datetime, article=article)






    
# Get links to different sections
# response.css('div.site-header__primary-navigation-wrapper > div > nav > ul > li > a::attr(href)').getall()
# Filter for business, politics, culture, sports
# Sample link: https://www.telegraph.co.uk/politics/


# Get links to each story on the category on that page
# response.css('section > ul > li > article > div.card__content > h3 > a::attr(href)').getall()


# Get heading of story
# response.css('article > header > h1::text').get()


# Get subheading
# response.css('article > header > p::text').get()


# Get author
# response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--header-meta.article__separator > div > span > span > a > span.e-byline__author::text').get()

# Get Date and Time
# response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--header-meta.article__separator > div > time::text').get()

# Get the article
# response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--content > div:nth-child(1) > div.articleBodyText.section > div.component.article-body-text > p::text').getall()