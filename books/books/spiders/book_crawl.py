# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
	name = 'book_crawl'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	rules = (
		Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback='parse_item', follow=True),
		Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
	)

	def parse_item(self, response):
		yield {
			'book_name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
			'Book_price': response.xpath("//div[@class='col-sm-6 product_main']/p/text()").get(),
		}
