import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, PARSER_NAME, START_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = PARSER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URL

    def parse(self, response):
        page_links = response.css('a[href^="pep"]')
        for link in page_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get().split()
        data = {
            'number': page_title[1],
            'name': page_title[3:],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
