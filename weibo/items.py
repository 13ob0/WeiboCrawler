# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UserItem(scrapy.Item):
    collection = table = 'users'
    name = scrapy.Field()
    avatar = scrapy.Field()
    page = scrapy.Field()
    influence = scrapy.Field()
    weibo_count = scrapy.Field()
    following_count = scrapy.Field()
    follower_count = scrapy.Field()


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = table = 'weibos'
    name = scrapy.Field()
    id = scrapy.Field()
    text = scrapy.Field()
    pictures = scrapy.Field()
    videos = scrapy.Field()
    likes_count = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()

