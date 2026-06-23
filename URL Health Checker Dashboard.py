import requests
import time

websites = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com"
]

print("=== WEBSITE HEALTH CHECKER ===\n")

for site in websites:
    try:
        start = time.time()
        response = requests.get(site, timeout=5)
        end = time.time()

        print(f"URL: {site}")
        print(f"Status: {response.status_code}")
        print(f"Response Time: {round(end-start,2)} sec")
        print("-" * 40)

    except Exception:
        print(f"{site} is DOWN")
