import re
import sys

def extract_urls(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    urls = re.findall(r'(?:https?://)?(?:[-\w.]|(?:%[\da-fA-F]{2}))+', contents)
    subdomains = set()
    for url in urls:
        subdomain = re.search(r'(?:https?://)?([^/]+)', url)
        if subdomain:
            subdomains.add(subdomain.group(1))
    
    return urls, subdomains

file_path = sys.argv[1]
urls, subdomains = extract_urls(file_path)
print("URLs: " + ' '.join(urls))
print("Subdomains: " + ' '.join(subdomains))
