import requests

def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{url} is UP ✅")
        else:
            print(f"{url} returned status code {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"{url} is DOWN ❌")


