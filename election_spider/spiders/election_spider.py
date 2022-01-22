import urllib.request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from data_handler.functions import extractor, delete, data_path

class ElectionSpider(CrawlSpider):
    name = 'election_spider'
    
    start_urls = ['https://dadosabertos.tse.jus.br/dataset/?groups=eleitorado']

    rules = (
        # Extract links matching 'eleitorado' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('eleitorado\-[0-9]+', )), callback='parse_item'),
    )

    def parse_item(self, response):
        file_list = []
        file_url = response.css('.resource-url-analytics::attr(href)').get()
        self.logger.info(file_url)
        file_name = file_url.split('/')[-1]
        file_list = [file_name]
        with urllib.request.urlopen(file_url) as file:
            with open(data_path.joinpath(file_name), 'wb') as out_file:
                out_file.write(file.read())
        extractor(file_list)
        delete(file_list)