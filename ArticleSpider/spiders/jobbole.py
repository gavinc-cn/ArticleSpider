# -*- coding: utf-8 -*-
import scrapy, re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        :param response:
        :return:
        """

        # 解析列表页中的所有文章url
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            print(post_url)



        # # 通过xpath选择器提取字段
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        # create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·", "").strip()
        # praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        # fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = match_re.group(1)
        #
        # comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     comment_nums = match_re.group(1)
        #
        # content = response.xpath("//div[@class='entry']").extract()[0]
        #
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        #
        #
        # # 通过css选择器提取字段
        # title = response.css(".entry-header h1::text").extract_first("")
        # create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()
        #
        # fav_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = match_re.group(1)
        #
        # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", comment_nums)
        # if match_re:
        #     comment_nums = match_re.group(1)
        #
        #
        # content = response.css("div.entry").extract()[0]
        #
        # tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)




        # print(title, create_date, praise_nums, fav_nums, comment_nums, tags)








