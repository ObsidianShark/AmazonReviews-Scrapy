# Amazon Reviews Scraper



## Description

This spider will crawl amazon.com and gather review data from all products in a query list.

## Requirements

Python 3.10+


## Installation

To clone the repository, type the code below in a shell :

```bash
  git clone https://github.com/ObsidianShark/AmazonReviews-Scrapy.git
  cd amazon
```

To install dependencies, run the command bellow :

```bash
  pip install -r requirements.txt
```



## Usage

1 - Add all desired queries to 'queries' and the start of the spider.

2 - To crawl over all products, run the command bellow:

```bash
  scrapy crawl amazon_review -o reviews.json
```




