# -*- coding: utf-8 -*-

import scrapy


class PollenspiderItem(scrapy.Item):
    name = scrapy.Field()
    level_text = scrapy.Field()
    level = scrapy.Field()
    city = scrapy.Field()
