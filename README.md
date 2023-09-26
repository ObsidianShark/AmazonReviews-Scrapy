# Amazon Reviews Scraper



## Description

This spider will crawl amazon.com and gather review data from all products in a query list to a SQL database.

## Requirements

Python 3.10+\
Docker


## Installation

To clone the repository, type the code below in a shell :

```bash
  git clone https://github.com/ObsidianShark/AmazonReviews-Scrapy.git  
```

To install dependencies, run the command bellow :

```bash
  pip install -r requirements.txt  
```

To properly use the scrapy-splash dependency, splash docker is necessary so make sure to check all the settings configuration at: https://github.com/scrapy-plugins/scrapy-splash



## Usage

1 - Start your splash docker with the command bellow:

```bash
  docker run -p 8050:8050 scrapinghub/splash
```

2 - Add all desired queries to 'queries' and the start of the spider.

3 - To crawl over all products, run the command bellow:

```bash
  scrapy crawl amazon_review
```




