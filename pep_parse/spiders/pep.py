import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        response.css(
            'section[id="index-by-category"],'
            ' section[id="numerical-index"]'
        ).getall()
        table_strings = response.css('tr').getall()
        for row in table_strings:
            page_link = row.css('a.pep.reference.internal').get
            yield response.follow(page_link, callback=self.parse_pep)


    def parse_pep(self, response):
        ...