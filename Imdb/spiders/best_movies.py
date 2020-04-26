# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?sort=ir,desc&mode=simple&page=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//tbody[@class = 'lister-list']/tr/td[2]/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'title':response.xpath('//div[@class = "title_wrapper"]/h1/text()').get(),
            'year':response.xpath('//div[@class = "title_wrapper"]/h1/span/a/text()').get(),
            'duration':response.xpath('normalize-space((//time)[1]/text())').get(),
            'genre':response.xpath('//div[@class = "subtext"]/a[1]/text()').get(),
            'rating':response.xpath('//span[@itemprop="ratingValue"]/text()').get(),
            'movie_url':response.url,

        }