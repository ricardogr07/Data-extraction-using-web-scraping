from process_ds_jobs import run_ds_daily_scraper
from Utils.logger import Logger

if __name__ == '__main__':
    logger = Logger('main.log')
    logger.log.info('Initializing web scraping for LinkedIn Jobs.')
    file = 'LinkedIn_Jobs_Data_Scientist_Monterrey.csv'
    run_ds_daily_scraper(logger=logger, file_name=file)