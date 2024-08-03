from icrawler.builtin import GoogleImageCrawler, BingImageCrawler

class PictureCrawler:
    def __init__(self) -> None:
        pass

    def run_pars(self, key_words: str, main_dirr: str, crawl_mode: str = 'Google', max_pic: int = 1):
        if crawl_mode == 'Google':
            g_pars = GoogleImageCrawler()
            #g_pars.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
            self.parser(key_words=key_words, parser=g_pars, main_dirr=main_dirr, max_pic=max_pic)
        #сделать bingcrawler
        elif crawl_mode == 'Bing':
            b_pars = BingImageCrawler()
            self.parser(key_words=key_words, parser=b_pars, main_dirr=main_dirr, max_pic=max_pic)

    def parser(self, key_words: list, parser: classmethod, main_dirr: str, max_pic: int):
        #проверить работает ли быстрее если каждый раз удалить парсер и потом его пресоздовать
        for i in key_words:
            copy_parser = parser
            #g = GoogleImageCrawler(storage={'root_dir': f'{main_dirr}/{i}'})
            copy_parser.__init__(storage={'root_dir': f'{main_dirr}/{i}'})
            copy_parser.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
           
