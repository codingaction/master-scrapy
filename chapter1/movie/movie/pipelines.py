# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        with open("my_meiju.out", 'a', encoding='utf8') as fp:
            fp.write(item['name'] + '\n')
        return item
