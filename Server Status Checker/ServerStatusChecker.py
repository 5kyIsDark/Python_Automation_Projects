import requests


file_path = input("Please Enter The Path To The .txt File Containing URLs: ").strip()


with open(file_path, "r") as file:
    sites = [line.strip() for line in file]


for site in sites:
    try:
        response = requests.get(site, timeout=5)
        if response.status_code == 200:
            print(f"✅ {site} is Online")
        else:
            print(f"⚠️ {site} returned status code: {response.status_code}")
    except requests.RequestException:
        print(f"❌ {site} is Offline or Unreachable")

tag = bytes.fromhex('536b7949734461726b').decode()
