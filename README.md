# eCom Item Data Scraper

## Overview
This project is a data scraper for eBay, designed to collect item data for model training purposes. It uses eBay's Sandbox environment APIs to gather diverse e-commerce item data.

## Key Features
- Utilizes eBay's Browse API for efficient data collection
- Implements Selenium for extracting item descriptions
- Supports both sandbox and production environments
- Provides flexible keyword-based searching

## Installation

### Prerequisites
- Python 3.x
- Docker (optional)

### Install Dependencies
Using conda:
```bash
conda create --file requirements.txt --name scraper
conda activate scraper
```

Using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Running with Docker
```bash
docker volume create scraper_data
docker build -t scraper:v1 .
docker run -it -v scraper_data:/app/volume scraper:v1
```

### Running Locally
1. Obtain a sandbox keyset via [eBay's developer program](https://developer.ebay.com/develop/get-started). And place credientails into the `config` directory. (Details and example in `config`).
2. Clone this repository, and open a script in this directory.
3. Use the following imports to get started:
   ```python
   import json
   from datacraper import Scraper, ScraperUtil
   ```
4. Create a text file in the `keywords` directory with your desired search keywords. The `ScraperUtil` class will handle reading in keyword data.
5. Use the list of keywords generated from `ScraperUtil` with `Scraper.search_and_scrape()` to start scraping item data.  

Refer to `tests/sandbox_test.py` for examples on using the `Scraper` and `ScraperUtil` classes.

## Data Collection

The scraper searches for up to 200 results for each keyword. For tips on generating effective keyword lists, see the [Data](#data) section below.

**Note**: The `search_and_scrape()` method yields a generator where each iteration provides a single search result with complete item data.

## Data

Sample outputs can be found in the `tests/outputs` directory. These were generated using eBay API search calls with a limit of 200 items per keyword.

### Generating Keywords
To create diverse keyword lists, you can use AI tools like ChatGPT. Here's an example prompt:

```
Give me a common and diverse set of items typically found on eBay, such as:
Watch
Technology
Cars
Games
Shoes
Clothes

Extend this list with items necessary for a diverse model training dataset. Format your response as newline-separated item keywords.
```

## Why eBay?

eBay was chosen for this project due to several advantages:
1. Open API Sandbox Support
2. Extensive Developer Support
3. Vast and High-Quality Data
4. RESTful APIs (offering scalability, atomicity, flexibility, and performance)

## Development Notes

### Sandbox Mode
This project uses eBay's Sandbox environment, which provides a rich simulated eBay website for testing and development.

### eBay Developer Program
To access eBay's Sandbox APIs, sign up for the [eBay Developer Program](https://developer.ebay.com/develop/get-started) (it's free and verification usually takes about a day).

### API Selection
This project uses the Browse API from eBay's Buy APIs, specifically the `search` call, which provides comprehensive item data.

### Description Parsing
Due to limitations in the API's item description data, Selenium is used to scrape the full item description from the listing URL.

## Future Work
- Implement tracking for item listing duration (time until sold).
- Optimize for production API usage, including caching and retry mechanisms. Though, production API usage will certainly be denied by eBay given the scope of this project.
- Improve performance through threading or multiprocessing techniques.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments
- [eBay Developer Program](https://developer.ebay.com/develop/get-started)

## License
Distributed under the Apache-2.0 License. See LICENSE.txt for more information.
