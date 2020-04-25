# -*- coding: utf-8 -*-
import scrapy


class DebtSpider(scrapy.Spider):
	name = 'debt'
	allowed_domains = ['www.worldpopulationreview.com']
	start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

	def parse(self, response):
		countries_debt = response.xpath("//table/tbody/tr")
		for country in countries_debt:
			name = country.xpath(".//td[1]/a/text()").get()
			debt_perc = country.xpath(".//td[2]/text()").get()

			yield {
				'name': name,
				'debt_percentage': debt_perc
			}
