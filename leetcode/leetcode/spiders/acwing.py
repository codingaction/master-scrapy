import scrapy
from leetcode.items import LeetcodeItem


class AcwingSpider(scrapy.Spider):
    name = 'acwing'
    allowed_domains = ['www.acwing.com']
    start_urls = [
        # 'https://www.acwing.com/solution/leetcode/1/',
        # 'https://www.acwing.com/solution/leetcode/2/',
        # 'https://www.acwing.com/solution/leetcode/3/',
        # 'https://www.acwing.com/solution/leetcode/4/',
        # 'https://www.acwing.com/solution/leetcode/5/',
        # 'https://www.acwing.com/solution/leetcode/6/',
        # 'https://www.acwing.com/solution/leetcode/7/',
        'https://www.acwing.com/solution/leetcode/8/',
        # 'https://www.acwing.com/solution/leetcode/9/',
        # 'https://www.acwing.com/solution/leetcode/10/',
        # 'https://www.acwing.com/solution/leetcode/11/',
        # 'https://www.acwing.com/solution/leetcode/12/',
        # 'https://www.acwing.com/solution/leetcode/13/',
        # 'https://www.acwing.com/solution/leetcode/14/',
        # 'https://www.acwing.com/solution/leetcode/15/',
        'https://www.acwing.com/solution/leetcode/16/',
        # 'https://www.acwing.com/solution/leetcode/17/',
        # 'https://www.acwing.com/solution/leetcode/18/',
        # 'https://www.acwing.com/solution/leetcode/19/',
        # 'https://www.acwing.com/solution/leetcode/20/',
        # 'https://www.acwing.com/solution/leetcode/21/',
        # 'https://www.acwing.com/solution/leetcode/22/',
        # 'https://www.acwing.com/solution/leetcode/23/',
        # 'https://www.acwing.com/solution/leetcode/24/'
    ]

    def parse(self, response):
        questions = response.xpath('//tbody//td/a[starts-with(@href, "/solution/LeetCode/content/")]')
        count = 1
        for question in questions:
            item = LeetcodeItem()
            try:
                count = count + 1
                item['num'] = count
                name_list = question.xpath('./text()').extract()
                if len(name_list) > 0:
                    item['name'] = name_list[0]
                href_list = question.xpath('./@href').extract()
                if len(href_list) > 0:
                    item['url'] = "https://www.acwing.com" + href_list[0]
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
            item['title'] = response.xpath("//div[@class='panel-body']").xpath("./h2/text()").extract()[0]
            item['content'] = response.xpath("//div[@class='ui bottom attached tab active martor-preview']").xpath('string(.)').extract()[0]

        yield item
