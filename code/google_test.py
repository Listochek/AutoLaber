from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': r'TESTS\Crawler'})
google_crawler.crawl(keyword='cat', max_num=100)