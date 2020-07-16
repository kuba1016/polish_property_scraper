import scrapy


class GratkaSpider(scrapy.Spider):
    name = 'otodom'
    allowed_domains = ['www.otodom.pl']
    start_urls = ['https://www.otodom.pl/sprzedaz/dom/?search%5Bfilter_enum_market%5D=primary']

    def parse(self, response):
        for i in response.xpath("//article[@data-featured-name='listing_no_promo']/div[@class='offer-item-details']"):
            yield {
                "url" : i.xpath(".//header/h3/a/@href").get(),
                "title" : i.xpath(".//header/h3/a/span/span/text()").get(),
                "location" : i.xpath(".//header/p/text()").get(),
                "rooms" : i.xpath(".//ul/li[@class='offer-item-rooms hidden-xs']/text()").get(),
                "price" : i.xpath("normalize-space(.//ul/li[@class='offer-item-price']/text())").get(),
                "m2" : i.xpath(".//ul/li[@class='hidden-xs offer-item-area']/text()").get(),
                "plot_m2" : i.xpath(".//ul/li[@class='hidden-xs offer-item-area'][2]/text()").get()




            }
        next_page = response.xpath("//li[@class='pager-next']/a/@href").get()

        if next_page:
            yield scrapy.Request(url= next_page, callback= self.parse)
