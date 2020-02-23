# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    start_urls = [
        'http://www.stampar.hr/hr/peludna-grad/1',
        'http://www.stampar.hr/hr/peludna-grad/16',
        'http://www.stampar.hr/hr/peludna-grad/7'
    ]

    def parse(self, response):
        city = response.xpath('//h1/text()').getall()[1].split(': ')[1].strip()
        pollens = response.css('div.view-content')
        for pollen in pollens:
            plant = {}
            name = pollen.xpath('.//div[has-class("naziv")]/a/text()').get()
            if name is None:
                continue
            plant['name'] = name
            plant['date'] = pollen.xpath('.//div[has-class("datum-resp")]/text()').get()
            plant['level-text'] = pollen.xpath('.//div[has-class("vrijednost-tekst")]/div/text()').get()
            plant['level'] = pollen.xpath('.//div[has-class("vrijednost")]/text()').get()
            plant['city'] = city
            yield plant
