import advertools as adv
import pandas as pd
import re

crawl = adv.crawl(
    'https://djangoproject.com', 
    output_file='result.jl', 
    follow_links=False , 
    # allowed_domains=['www.djangoproject.com'],
    custom_settings= {
        'LOG_FILE' : 'django.log',
        # 'ROBOTSTXT_OBEY': False
    })

df        = pd.read_json('result.jl', lines=True)
csv       = df.to_csv ('result.csv', index=None)

# regex = '20\d\d-\d\d-\d\d \d\d:\d\d:\d\d.*?Forbidden by robots\.txt: <GET (.*?).'
# blocked_urls = []
# with open('django.log') as file:
#     for line in file:
#         url = re.findall(regex, line)
#         if url:
#             blocked_urls.append(url[0])

# print(f'Number of blocked URLs : {len(blocked_urls):,} \n\nSample:')
# blocked_urls[:10]

# django_sitemap = adv.sitemap_to_df('https://www.bbc.com/robots.txt')
# django_sitemap.to_csv ('sitemap.csv', index=None)
# please add if some sitemap url in sitemap index points to 404 skip it and continue with the rest  

