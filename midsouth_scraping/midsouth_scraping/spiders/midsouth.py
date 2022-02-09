import scrapy 

class midsouthSpider(scrapy.Spider):
    name = 'supply'
    start_urls=[
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
    ]
    custom_settings = {"FEEDS":{"results.json":{"format":"json"}}} # creates json data stores in result
    def parse(self,response):
        for supplies in response.css("div.product"): # iterate through each product and collect one attribute at a time
            price =supplies.css(".price span::text").get() #extracts rpice
            title = supplies.css(".catalog-item-name::text").get() #extracts product title
            if supplies.css(".out-of-stock::text")[0].get() == 'Out of Stock': #if the product is out of stock , stock is set to false
                stock=False
            else:
                stock=True
            
            manufacturer =supplies.css(".catalog-item-brand::text").get()# extracts manufacturer

            yield { # data yeilded in json format
                'price':price,
                'title' : title,
                'stock': stock,
                'manufacturer' : manufacturer           
                }
        
        next_page = response.css(".pagination a:nth-child(5)::attr(href)").get() # scraping for next page
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
