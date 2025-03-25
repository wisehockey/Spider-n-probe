# Spider n Probe

This project consists of two Python scripts:
1. **Spider.py**: Crawls a given URL, searching for links containing a specific keyword.
2. **Probe.py**: Verifies the validity of URLs by checking their HTTP status.

## How to Use

### Spider.py
- Input a URL to scrape and a keyword to search for.
- The script will crawl the website and print URLs that contain the keyword.

### Probe.py
- Input a list of URLs (one per line).
- The script will check which URLs are valid (status code 200) and save them to a file.

## Requirements
- `requests`
- `beautifulsoup4`

## Install dependencies via pip:
- pip install requests beautifulsoup4
