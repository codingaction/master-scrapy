# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        print("Save the {}th question: {}".format(item['num'], item['name']))
        with open("leetcode.out", 'a', encoding='utf8') as fp:
            fp.write(item['name'] + '\n')
            fp.write(item['content'] + '\n')
            fp.write("===========================================\n")
        return item
