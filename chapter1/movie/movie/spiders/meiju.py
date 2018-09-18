# -*- coding: utf-8 -*-
import scrapy
import time
from movie.items import LeetcodeItem


class MeijuSpider(scrapy.Spider):
    # name = 'meiju'
    # allowed_domains = ['meijutt.com']
    # start_urls = ['http://www.meijutt.com/new100.html']
    #
    # def parse(self, response):
    #     movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
    #     for movie in movies:
    #         item = MovieItem()
    #         item['name'] = movie.xpath('./h5/a/@title').extract()[0]
    #         yield item

    name = 'meiju'
    allowed_domains = ['bookshadow.com']
    base_url = "http://bookshadow.com"
    start_urls = ['http://bookshadow.com/leetcode/']

    def parse(self, response):
        questions = response.xpath('//td/a[starts-with(@href, "/weblog")]')
        count = 1
        for question in questions:
            item = LeetcodeItem()
            item['name'] = question.xpath('./text()').extract()[0]
            item['url'] = self.base_url + question.xpath('./@href').extract()[0]
            count = count + 1
            item['num'] = count
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)

    def detail_parse(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        #一级内页数据提取
        item['content'] = response.xpath("//div[@class='entry-content lead']").xpath('string(.)').extract()[0]
        yield item



