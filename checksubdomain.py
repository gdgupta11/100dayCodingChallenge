# Script to check subdomain of the websites using Certificate transperancy logs
# 100daysCodingChallenge

import requests
import sys

args_length = len(sys.argv) - 1
if args_length < 1:
    print("Enter the domain name for search")
    sys.exit(1)

def get_subdomains(url):
    """
        Takes a URL and get lists of subdomains using certificate transperancy logs from crt.sh website. 

         Response schema from website:
            {
            "issuer_ca_id": int,
            "issuer_name": string,
            "name_value": string, # this is the domain/subdomain Name
            "id": long int,
            "entry_timestamp": timestamp,
            "not_before": timestamp,
            "not_after": timestamp"
            }

         parameters:
            url: string

         return:
            all_subdomains: list
    """
    response = requests.get(url, verify=False)
    all_subdomains = []
    if response.status_code == 200:
        data = response.json()
        for d in data:
            site = d['name_value'].split("\n")[0]
            if site not in all_subdomains:
                all_subdomains.append(site)

    return all_subdomains


def main():
    url = "https://crt.sh/?q={}&output=json"
    website = str(sys.argv[1])
    url = url.format(website)

    subdomains = get_subdomains(url)
    for sub in subdomains:
        print(sub)


if __name__ == "__main__":
    main()
