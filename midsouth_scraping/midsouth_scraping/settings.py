

BOT_NAME = 'midsouth_scraping'

SPIDER_MODULES = ['midsouth_scraping.spiders']
NEWSPIDER_MODULE = 'midsouth_scraping.spiders'

ROBOTSTXT_OBEY = False

PROXY_POOL_ENABLED = True


DOWNLOADER_MIDDLEWARES = {
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620
}

