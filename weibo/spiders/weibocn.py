# -*- coding: utf-8 -*-
import scrapy
import re


from weibo.items import UserItem, WeiboItem


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn/pub/top?cat=star&rl=0']

    def parse(self, response):
        # self.logger.debug(response.text)
        


        # sel = response.xpath('//tr')
        # print('♦️' * 100)
        # print(sel[0])
        # print(sel[0].xpath('/td').extract())
        # print('♦️' * 100)
        stars = response.xpath('//tr')
        for star in stars:
            user_item = UserItem()

            user_item['name'] = star.xpath('.//a[@class="nk"]/text()').extract_first()
            user_item['avatar'] = star.xpath('.//img[@class="por"]/@src').extract_first()
            user_item['page'] = star.xpath('.//a[@class="nk"]/@href').extract_first()
            user_item['influence'] = star.xpath('.//td[2]/text()').re_first('\d+')
            # user_item['influence'] = star.xpath('.//td[2]/text()').re_first('\d+')
            # print('♦️' * 100)
            # print(sel.xpath('.//a[@class="nk"]/text()').extract_first())
            # print('♦️' * 100)
            yield scrapy.Request(url=user_item['page'], callback=self.parse_user, meta={'key': user_item})
            # yield user_item
            # print(sel.xpath('//text()').extract())
        # content = response.xpath('//span[@class="ctt"]/text()').extract()
        next = response.xpath('//*[@id="pagelist"]/form/div/a[text()="下页"]/@href').extract_first()
        next_url = response.urljoin(next)
        print(next_url)
        yield scrapy.Request(url=next_url, callback=self.parse)
        # print(title)
        # print(content)

    def parse_user(self, response):
        user_item = response.meta['key']
        user_item['weibo_count'] = response.xpath('//span[@class="tc"]/text()').re_first('\d+')
        user_item['following_count'] = response.xpath('//a[contains(@href, "follow")]/text()').re_first('\d+')
        user_item['follower_count'] = response.xpath('//a[contains(@href, "fans")]/text()').re_first('\d+')
        weibos = response.xpath('//div[contains(@id, "M")]')
        for weibo in weibos:
            weibo_item = WeiboItem()
            # print('♦️' * 100)
            # print(weibo.xpath('./@id').extract_first())
            # print('♦️' * 100)
            weibo_item['name'] = user_item['name']
            weibo_item['id'] = weibo.xpath('./@id').extract_first()
            weibo_item['text'] = weibo.xpath('.//span[@class="ctt"]/text()').extract_first()
            weibo_item['pictures'] = weibo.xpath('.//img[@alt="图片"]/@src').extract()
            weibo_item['videos'] = weibo.xpath('.//a[contains(text(), "视频")]/@href').extract_first()
            weibo_item['likes_count'] = weibo.xpath('.//a[contains(text(), "赞")]/text()').re_first('\d+')
            weibo_item['reposts_count'] = weibo.xpath('.//a[contains(text(), "转发")]/text()').re_first('\d+')
            weibo_item['comments_count'] = weibo.xpath('.//a[contains(text(), "评论")]/text()').re_first('\d+')
            # print(weibo_item['id'])
            yield weibo_item

        yield user_item
        

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl weibocn".split())
