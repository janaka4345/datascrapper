import scrapy
import json


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    url = "https://jsonplaceholder.typicode.com/todos"
    # allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com/"]

    # def parse(self, response):
    #     books = response.css("article.product_pod")
    #     print(len(books))
    #     for book in books:
    #         yield {
    #             "name": book.css("h3 a::text").get(),
    #             "price": book.css("p.price_color::text").get(),
    #         }

    #     next_page = response.css("li.next a").attrib["href"]
    #     if next_page is not None:
    #         print(f"{self.start_urls[0]}{next_page}")
    #         # if "catalogue/" in next_page:
    #         next_page_url = f"{self.start_urls[0]}{next_page}"
    #         # else:
    #         # next_page_url = f"{self.start_urls[0]}catalogue/{next_page}"

    #         yield response.follow(next_page_url, callback=self.parse)
    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.discover)

    def discover(self, response):
        python_dict = json.loads(response.text)
        for item in python_dict:
            yield {
                "userId": item["userId"],
                "id": item["id"],
                "title": item["title"],
                "completed": item["completed"],
            }
