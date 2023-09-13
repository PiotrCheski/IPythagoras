import sys
import os
import re
import requests
import config

API_KEY = config.API_KEY
scanned_IPs = set()

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

def process_file(file_path):
    ip_addresses = extract_ip_addresses(file_path)
    if not ip_addresses:
        print(f"No IP addresses were found in {file_path}.")

    for ip in ip_addresses:
        if ip not in scanned_IPs:
            scanned_IPs.add(ip)
            info_about_ip = get_info_about_ip(ip)
            if info_about_ip:
                print(f"IP: {ip}")
                print(f"Country: {info_about_ip['country_name']}")
                print(f"ISP: {info_about_ip['isp']}")
                print(f"Organization: {info_about_ip['organization']}")
                print(f"Country TLD: {info_about_ip['country_tld']}")
                print("-" * 30)
        else:
            print(f"The IP {ip} has been previously scanned.")

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path_or_directory>")
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            process_file(path)
        elif os.path.isdir(path):
            process_directory(path)
        else:
            print(f"Invalid path: {path}")
