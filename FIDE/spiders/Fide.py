import scrapy


class FideSpider(scrapy.Spider):
    name = "fide_spider"

    def __init__(self, fide_id=None, *args, **kwargs):
        super(FideSpider, self).__init__(*args, **kwargs)
        self.fide_id = fide_id
        self.fide_ids = [
            22226141,
            32066171,
            22298851,
        ]

    def start_requests(self):
        if not self.fide_ids:
            self.logger.error('FIDE ID is required.')
            return

        for fide_id in self.fide_ids:
            url = f'https://ratings.fide.com/profile/{fide_id}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'fide_id': fide_id})

    def parse(self, response):
        name = response.xpath('//div[@class="col-lg-8 profile-top-title"]/text()').get().strip()
        # Extract standard rating
        std_rating = response.xpath('//div[contains(@class, "profile-top-rating-data_gray")]/text()[normalize-space()]').get().strip()
        # Extract rapid rating
        rapid_rating = response.xpath('//div[contains(@class, "profile-top-rating-data_red")]/text()[normalize-space()]').get().strip()
        # Extract blitz rating
        blitz_rating = response.xpath('//div[contains(@class, "profile-top-rating-data_blue")]/text()[normalize-space()]').get().strip()
        yield {
            'name': name,
            'std_rating': std_rating,
            'rapid_rating': rapid_rating,
            'blitz_rating': blitz_rating,
            'fide_id': self.fide_id,
        }