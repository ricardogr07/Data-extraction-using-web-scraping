from LinkedInWebScraper import LinkedInJobScraper, JobScraperConfig, Logger, FileManager, JobScraperConfigFactory, JobScraperAdvancedConfig
from Utils.constants import LOCATION_MAPPING, DATA_SCIENCE_KEYWORDS, TECH_STACK_CATEGORIES
import pandas as pd

def run_ds_daily_scraper(logger: Logger, openai_enabled: bool = True, position:str = 'Data Scientist', location:str = 'Monterrey', time_posted:str = 'DAY', file_name:str = None):
    try:
        logger.log.info(f'Starting web scraping for {position} in {location}.')

        advanced_config = JobScraperAdvancedConfig(LOCATION_MAPPING,DATA_SCIENCE_KEYWORDS,TECH_STACK_CATEGORIES)

        remote_types = ['REMOTE', 'HYBRID', 'ON-SITE']
        scraper_results = {}

        for remote in remote_types:
            config = JobScraperConfigFactory.create(position, location, openai_enabled, time_posted, remote)
            config.advanced_config = advanced_config
            scraper = LinkedInJobScraper(logger=logger, config=config)
            scraper_results[f"scraper_{remote.lower()}"] = scraper.run()

        # Concatenate all the results into a single DataFrame
        df_remote = scraper_results.get('scraper_remote', pd.DataFrame())
        df_hybrid = scraper_results.get('scraper_hybrid', pd.DataFrame())
        df_on_site = scraper_results.get('scraper_on-site', pd.DataFrame())

        df_jobs_all = pd.concat([df_remote, df_hybrid, df_on_site], ignore_index=True)

        # Save to CSV
        file_manager_config = JobScraperConfig(position, location, remote='ALL')
        file_manager = FileManager(logger, file_manager_config)
        if file_name != None:
            file_manager.save_jobs_to_csv(df=df_jobs_all, file_name=file_name,append=True)
        else:
            file_manager.save_jobs_to_csv(df=df_jobs_all)

    except Exception as e:
        print(f"An error occurred: {e}")
