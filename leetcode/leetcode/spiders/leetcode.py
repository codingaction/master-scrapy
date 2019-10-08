import scrapy
from leetcode.items import LeetcodeItem


class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/grandyang/p/4606334.html']

    def parse(self, response):
        questions = response.xpath('//tbody//td/a[starts-with(@href, "http://www.cnblogs.com/grandyang/p/")]')
        count = 1
        for question in questions:
            try:
                item = LeetcodeItem()
                count = count + 1
                item['num'] = count
                name_list = question.xpath('./text()').extract()
                if len(name_list) > 0:
                    item['name'] = name_list[0]
                href_list = question.xpath('./@href').extract()
                if len(href_list) > 0:
                    item['url'] = href_list[0]
                    yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)
            except BaseException:
                print("Fail to load question's detail info" + question)
                item['name'] = 'Valid'
                yield item

    def detail_parse(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        #一级内页数据提取
        if item['name'] == 'Valid':
            item['content'] = 'Null'
        else:
            item['content'] = response.xpath("//div[@id='cnblogs_post_body']").xpath('string(.)').extract()[0]

        yield item
