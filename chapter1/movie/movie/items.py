# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()


class LeetcodeItem(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    htmlContent = scrapy.Field()
    content = scrapy.Field()
