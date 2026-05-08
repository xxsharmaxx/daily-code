import requests
import time

websites = [
    "https://google.com",
    "https://github.com",
    "https://openai.com",
    "https://thiswebsitedoesnotexist123.com"
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"✅ {url} is UP")
        else:
            print(f"⚠️ {url} returned status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"❌ {url} is DOWN")


print("🌐 Website Monitoring Tool\n")

for site in websites:
    check_website(site)
    time.sleep(1)
