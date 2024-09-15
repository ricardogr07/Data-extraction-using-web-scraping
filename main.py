from process_ds_jobs import run_ds_daily_scraper
from Utils.logger import Logger

if __name__ == '__main__':
    logger = Logger('main.log')
    logger.log.info('Initializing web scraping for LinkedIn Jobs.')
    run_ds_daily_scraper(logger=logger)