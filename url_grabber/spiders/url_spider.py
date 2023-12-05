import scrapy

class UrlSpider(scrapy.Spider):
    name = 'url_spider'
    allowed_domains = ['www.gov.uk']
    start_urls = ['https://www.gov.uk/browse/environment-countryside/farming-land-management']
    visited_urls = set()

    def parse(self, response):
        all_urls = response.css('a::attr(href)').extract()

        with open('urls_full.csv', 'a') as f:
            for url in all_urls:
                full_url = response.urljoin(url)
                if full_url not in self.visited_urls:
                    self.visited_urls.add(full_url)
                    f.write("%s,\n" % full_url)

                    yield scrapy.Request(full_url, callback=self.parse)

        self.log('Saved %s full URLs to urls_full.csv' % len(all_urls))