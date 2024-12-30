import scrapy


class FideSpider(scrapy.Spider):
    name = "fide_spider"

    def __init__(self, fide_id=None, *args, **kwargs):
        super(FideSpider, self).__init__(*args, **kwargs)
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
        fide_id = response.meta['fide_id']
        # Extract FIDE ID from the page
        # extracted_fide_id = response.xpath('//div[@class="profile-top-info__block__row__data"]/text()').get().strip()
        extracted_fide_id = response.xpath('//div[contains(text(), "FIDE ID:")]/following-sibling::div/text()').get().strip()
        # Assert that the extracted FIDE ID matches the one passed to the URL
        assert str(fide_id) == str(extracted_fide_id), f"FIDE ID mismatch: {fide_id} != {extracted_fide_id}"
        # extract Bird Year
        bird_year = response.xpath('//div[contains(text(), "B-Year:")]/following-sibling::div/text()').get().strip()        
        # Extract player name
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
            'fide_id': fide_id,
            'bird_year': bird_year,
        }