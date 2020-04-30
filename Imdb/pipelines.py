# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MongodbPipeline(object):

    collection_name = "best_movies"

    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://Nouman:GDfieBq8Mjxe4QAk@cluster0-fpdvh.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
