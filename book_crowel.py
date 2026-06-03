import scrapy


class BookCrowel(scrapy.Spider):
    name = 'book_crowel'
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        title_list = response.xpath(
            "//article[@class='product_pod']/h3/a/@title").extract()
        with open("book_title.txt", "a+") as f:
            for title in title_list:
                f.write(title + "\n")

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
