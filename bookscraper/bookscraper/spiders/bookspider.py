import scrapy
import json
from bookscraper.bookscraper.items import BookscraperTodoItem
from bookscraper.bookscraper.items import BookscraperUserItem


class BookspiderSpider(scrapy.Spider):

    name = "bookspider"

    url = "https://jsonplaceholder.typicode.com/"

    def __init__(self, path=None, *args, **kwargs):
        super(BookspiderSpider, self).__init__(*args, **kwargs)
        self.path = path
        print(path)
        self.url2 = f"{self.url}{path}"

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
        if self.path == "todos":
            yield scrapy.Request(url=self.url2, callback=self.discover_todos)
        elif self.path == "users":
            yield scrapy.Request(url=self.url2, callback=self.discover_users)
        else:
            return None

    def discover_todos(self, response):
        python_dict = json.loads(response.text)
        todo_item = BookscraperTodoItem()
        for item in python_dict:
            print("start*************************************************")
            print(item)
            print("end*************************************************")
            todo_item["userId"] = item["userId"]
            todo_item["id"] = item["id"]
            todo_item["title"] = item["title"]
            todo_item["completed"] = item["completed"]

            yield todo_item

    def discover_users(self, response):
        python_dict = json.loads(response.text)
        user_item = BookscraperUserItem()
        for item in python_dict:
            user_item["id"] = item["id"]
            user_item["name"] = item["name"]
            user_item["username"] = item["username"]
            user_item["email"] = item["email"]

            yield user_item
