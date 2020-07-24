# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = [
        'https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        gdps = response.xpath(
            '//table[@class="datatableStyles__StyledTable-ysgkm4-1 dXImya table table-striped"][1]/tbody/tr')
        for gdp in gdps:
            name = gdp.xpath(".//td[1]/a/text()").get()
            g = gdp.xpath(".//td[2]/text()").get()

            yield {
                'country_name': name,
                'gdp_debt': g
            }
