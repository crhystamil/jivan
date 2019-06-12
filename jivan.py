#!/usr/bin/env python3
from urllib3.util import parse_url
import argparse
import requests

def start():
    parser = argparse.ArgumentParser(description='jivan is a toll for fuzzing of urls')
    parser.add_argument("-u","--url", help="URL tarjet",required=True)
    parser.add_argument("-v","--verify", type=bool, help="verify URL's",required=False)
    parser.add_argument("-m","--method", help="type method for verify (GET,POST)",required=False)
    parser.add_argument("-w", "--word", help="word to change", required=True)
    args = parser.parse_args()
    if args.url is not None:
        analyze_url(args.url, args.word, args.verify, args.method)
    else:
        print('\033[93m[!] Invalid source.\n\n \033[0m')
        sys.exit(1)

def analyze_url(url, word, verify, method):
    url_site = parse_url(url)
    domain = url_site.host
    path = url_site.path
    scheme = url_site.scheme
    word = word
    list_urls = generate_url(domain, path, word, scheme)
    print("-------------------------- urls --------------------------------------")
    for a in list_urls:
        print(a)
#    print(verify)
    if verify == True:
        verify_urls(list_urls, method)

def generate_url(domain, path, word, scheme):
    paths = path.split('/')
    paths = [i for i in paths if i]
    new_paths = []
    for i, c in enumerate(paths[0:-1]):
        y = c + word
        z = paths[i]
        paths[i] = y
        new_paths.append(scheme+"://"+domain+"/"+"/".join(paths))
        paths[i] = z

    return new_paths
def verify_urls(list_urls, method):
    print("-------------------------- verify url's --------------------------------")
    if method == "GET":
        for u in list_urls:
            r = requests.get(u)
            print(u + " ---> " + str(r.status_code))
    elif method == "POST":
        for u in list_urls:
            r = requests.post(u)
            print(u + " ---> " + str(r.status_code))

def main():
    banner = """
       __.__                      
      |__|__|__  _______    ____  
      |  |  \  \/ /\__  \  /    \ 
      |  |  |\   /  / __ \|   |  \\
  /\__|  |__| \_/  (____  /___|  /
  \______|              \/     \/ 
    """
    print(banner)
    start()

if __name__ == "__main__":
    main()
