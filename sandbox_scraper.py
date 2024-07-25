import os
import json
from datascraper import Scraper, ScraperUtil

def normalize_keywords(keyword: str) -> str:
    keyword = keyword.replace('\n', '')
    keyword = keyword.replace(' ', '-')
    return keyword.lower()

if __name__ == '__main__':
        
        # Initialize ScraperUtil
        util = ScraperUtil()

        # Read data from each keywords file in keywords directory
        keywords = util.read_files(directory='keywords', file_type='.md')
        print(f"Keywords to Scrape: {len(keywords)}\n")

        # Ensure the output directory exists
        output_dir = "volume/item_data"
        os.makedirs(output_dir, exist_ok=True)

        # Set keyset config file path
        keysetConfigPath = "config/account-credentials.json"

        # Call the data scraper and run as a generator
        datascraper = Scraper(environment='SANDBOX', keyset='DataScraper', keysetConfigPath=keysetConfigPath)
        
        # Iterate through keywords
        for i, keyword in enumerate(keywords):
            # Normalize keywords
            keyword = normalize_keywords(keyword) 
            print(f"Scraping items related to '{keyword}'... {len(keywords)-i} keywords left.")
            
            # Use search_and_scrape() as a generator, aka itereator, that scrapes up to 200 items per key-word.
            for data_dump in datascraper.search_and_scrape(keyword, limit='200'): 
                with open(f"{output_dir}/data_{keyword}.json", 'a') as outfile:
                    json.dump(data_dump, outfile)
                    outfile.write("\n")

