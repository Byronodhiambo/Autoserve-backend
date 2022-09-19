from ast import Try
import os
import json 
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def main():
    GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
    }

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    SAVE_FOLDER = 'C:\Test\FusionERP8\FR6Share\Photo'

    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)

    file = open('Product.txt', "r")
    lines = file.readlines()
    
    for line in lines:
        searchurl = GOOGLE_IMAGE + 'q=' + line
        response = requests.get(searchurl, headers=usr_agent)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.findAll('img', {'class': 'yWs4tf'}, limit=2)
        # print(f'found {len(images)} images')
        # print('Start downloading...')
        line = line.strip()
        for i , image in enumerate(images):
            try:
                link = image['src']
                imagename = SAVE_FOLDER + '/' + line + str(i) + '.jpg'                   
                response = session.get(link)            
                with open(imagename, 'wb') as file:
                    file.write(response.content)
                    # print('Writing: ', imagename)
            except:
                print(f'error writing {imagename}')
                # with open("failed.txt", "a") as f:
                    # f.write(line + '\n')            
                    # f.close()

main()