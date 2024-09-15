from LinkedInScraper.linkedin_scraper import LinkedInJobScraper
from LinkedInScraper.job_scraper_config import JobScraperConfig
from Utils.logger import Logger
from Utils.file_manager import FileManager
import pandas as pd

def run_ds_daily_scraper(logger: Logger, position:str = 'Data Scientist', location:str = 'Monterrey', time_posted:str = 'DAY', file_name:str = None):
    try:
        logger.log.info(f'Starting web scraping for {position} in {location}.')

        ds_remote_config = JobScraperConfig(position, location, time_posted, remote='REMOTE')
        scraper_ds_remote = LinkedInJobScraper(logger=logger,config=ds_remote_config)

        ds_hybrid_config = JobScraperConfig(position, location, time_posted, remote='HYBRID')
        scraper_ds_hybrid = LinkedInJobScraper(logger=logger, config=ds_hybrid_config)

        ds_onsite_config = JobScraperConfig(position, location, time_posted, remote='ON-SITE')
        scraper_ds_onsite = LinkedInJobScraper(logger=logger, config=ds_onsite_config)


        # Run the scraper for different remote types
        df_remote = scraper_ds_remote.run()
        df_hybrid = scraper_ds_hybrid.run()
        df_on_site = scraper_ds_onsite.run()

        # Concatenate all the results into a single DataFrame
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
