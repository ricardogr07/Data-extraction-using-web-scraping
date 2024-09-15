from src.process_ds_jobs import run_ds_daily_scraper
from Utils.logger import Logger
import pandas as pd

if __name__ == '__main__':
    cities = ['Monterrey', 'Guadalajara', 'Mexico City']

    logger = Logger('main.log')

    logger.log.info(f'Initializing web scraping for LinkedIn Jobs for the cities {cities}.')

    for city in cities:
        city_filename = city.replace(" ", "_")
        file = f'LinkedIn_Jobs_Data_Scientist_{city_filename}.csv'
        run_ds_daily_scraper(logger=logger, location=city, file_name=file)

    df_mty = pd.read_csv('LinkedIn_Jobs_Data_Scientist_Monterrey.csv')
    df_gdl = pd.read_csv('LinkedIn_Jobs_Data_Scientist_Guadalajara.csv')
    df_cdmx = pd.read_csv('LinkedIn_Jobs_Data_Scientist_Mexico_City.csv')

    df_jobs_all = pd.concat([df_mty, df_gdl, df_cdmx], ignore_index=True)
    df_jobs_all.to_csv('LinkedIn_Jobs_Data_Scientist_Mexico.csv', index=False)