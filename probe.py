import sys
import requests

def urls(out_file):
    url2 = sys.stdin.read().splitlines()

    res_urls = []
    bad_urls = []

    for url in url2:
        try:
            response = requests.head(url)
            
            if response.status_code == 200:
                res_urls.append(url)
        
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
            continue

        except requests.exceptions.ConnectionError:
            bad_urls.append(url)

    with open(out_file, 'w') as f:
         f.write('\n'.join(res_urls))

    print(f"Saved URLS {out_file}")
     

out_file = 'filtered_urls.txt'
urls(out_file)