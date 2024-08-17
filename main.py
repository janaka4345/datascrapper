import datetime
from scrapy.crawler import CrawlerProcess

from bookscraper.bookscraper.spiders.bookspider import BookspiderSpider

# from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(settings={settings})
name = input("What is your input? ")

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "data_%(time)s.json": {
                "format": "json",
                "overwrite": False,
            }
        },
        # "ITEM_PIPELINES": {
        #     "bookscraper.bookscraper.pipelines.BookscraperPipeline": 300,
        # },
    }
)

process.crawl(BookspiderSpider, path=name)
process.start()
