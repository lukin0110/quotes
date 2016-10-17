import scrapy
import tempfile

from scrapy.crawler import CrawlerProcess
from .write import write


class BrainyQuoteSpider(scrapy.Spider):
    """
    Execute from the shell:
    $ scrapy runspider spiders.py -o in.csv
    """
    name = 'BrainyQuote'
    start_urls = ['']

    def parse(self, response):
        for title in response.css('span.bqQuoteLink'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('ul.pagination > li:last-child > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


def runner(url, file_uri='out.csv'):
    """
    A runner for the Spider declared previously in code.

    https://doc.scrapy.org/en/latest/topics/practices.html
    http://stackoverflow.com/questions/23574636/scrapy-from-script-output-in-json
    """
    temp = tempfile.NamedTemporaryFile()

    try:
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': 'csv',
            'FEED_URI': temp.name
        })

        process.crawl(BrainyQuoteSpider, start_urls=[url])
        process.start()

        write(temp.name, file_uri)
    finally:
        temp.close()
