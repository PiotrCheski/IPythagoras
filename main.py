import sys
import re
import requests
import json
API_KEY = ""

def extract_ip_addresses(file_path):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    with open(file_path, "r") as file:
        content = file.read()
        ip_addresses = re.findall(ip_pattern, content)
    
    return ip_addresses

def get_info_about_ip(ip):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data for IP {ip}: {response.text}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
    else:
        file_path = sys.argv[1]
        ip_addresses = extract_ip_addresses(file_path)

        for ip in ip_addresses:
            info_about_ip = get_info_about_ip(ip)
            if info_about_ip:
                print(f"IP: {ip}")
                print(f"Country: {info_about_ip['country_name']}")
                print(f"ISP: {info_about_ip['isp']}")
                print(f"Organization: {info_about_ip['organization']}")
                print(f"Country TLD: {info_about_ip['country_tld']}")
                print("-"*30)
