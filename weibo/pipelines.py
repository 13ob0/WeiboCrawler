# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

from weibo.items import UserItem, WeiboItem


class WeiboPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[UserItem.collection].create_index([('name', pymongo.ASCENDING)])
        self.db[WeiboItem.collection].create_index([('name', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            self.db[item.collection].update({'name': item.get('name')}, {'$set': item}, True)
        if isinstance(item, WeiboItem):
            self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        # if isinstance(item, UserRelationItem):
        return item


class MysqlPipeline:
    def __init__(self, mysql_uri, mysql_db, mysql_user, mysql_password, mysql_port):
        self.mysql_uri = mysql_uri
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_port = mysql_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_uri=crawler.settings.get('MYSQL_URI'),
            mysql_db=crawler.settings.get('MYSQL_DATABASE'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.mysql_uri, self.mysql_user, self.mysql_password, self.mysql_db, port=self.mysql_port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            data = dict(item)
            keys = ', '.join(data.keys())
            # values = ', '.join(['{}'] * len(data))
            values = ', '.join(['%s'] * len(data))
            # print(f'data: {data}')
            # print(f'keys: {keys}')
            # print(f'values: {values}')
            # sql = 'INSERT INTO {} ({}) VALUES ({})'.format(item.table, keys, values)
            # print(f'sql: {sql}')
            sql = 'INSERT INTO %s (%s) VALU ES (%s)' % (item.table, keys, values)
            print(f'sql: {sql}')
            print(f'data.values(): {data.values()}')
            
            print(f'{tuple(data.values())}')
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            return item
            # self.db[item.collection].update({'name': item.get('name')}, {'$set': item}, True)

        if isinstance(item, WeiboItem):
            data = dict(item)
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (item.table, keys, values)
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            return item



# sql2: INSERT INTO users (name, avatar, page, influence, weibo_count, following_count, follower_count) VALUES (%s, %s, %s, %s, %s, %s, %s)
# data.values(): dict_values(['回忆专用小马甲', 'https:/0e80e8q3k.jpg?KI2BYXRabKn', 'https://weibo.cn/u/3217179555', '1283', '34209', '778', '40975696'])