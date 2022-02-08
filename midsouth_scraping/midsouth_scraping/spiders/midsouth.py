import scrapy 

class midsouthSpider(scrapy.Spider):
    name = 'supply'
    start_urls=[
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
    ]
    custom_settings = {"FEEDS":{"results.json":{"format":"json"}}}
    def parse(self,response):
        for supplies in response.css("div.product"):
            price =supplies.css(".price span::text").get()
            title = supplies.css(".catalog-item-name::text").get()
            if supplies.css(".out-of-stock::text")[0].get() == 'Out of Stock':
                stock=False
            else:
                stock=True
            
            manufacturer =supplies.css(".catalog-item-brand::text").get()

            yield {
                'price':price,
                'title' : title,
                'stock': stock,
                'manufacturer' : manufacturer           
                }
        
        next_page = response.css(".pagination a:nth-child(5)::attr(href)").get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
