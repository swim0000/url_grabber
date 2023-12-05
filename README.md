# Scrapy Web Scraping Project

This project utilizes Scrapy, a web scraping framework for Python, to extract and save URLs from a website.

## Overview

The spider in this project starts from a specified URL, extracts all URLs on the page, and recursively follows each link to collect additional URLs. The full URLs are then saved to a CSV file for further analysis or processing.

## Getting Started

### Prerequisites

Make sure you have Python and Scrapy installed. You can install Scrapy using the following command:

```bash
pip install scrapy

git clone https://github.com/swim0000/url_grabber.git
cd your_project

scrapy crawl url_spider
