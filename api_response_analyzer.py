import requests
import json
import time


def analyze_json(data, level=0):
    indent = "  " * level

    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent}├── {key}: {type(value).__name__}")

            if isinstance(value, (dict, list)):
                analyze_json(value, level + 1)

    elif isinstance(data, list):
        print(f"{indent}└── Array items: {len(data)}")


def analyze_api(url):

    print("\n" + "=" * 65)
    print("              API RESPONSE ANALYZER")
    print("=" * 65)

    headers = {
        "User-Agent": "API-Response-Analyzer/1.0"
    }

    try:

        start = time.perf_counter()

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        elapsed = time.perf_counter() - start

    except requests.RequestException as error:

        print("\n❌ Request failed")
        print("Error:", error)
        return

    print("\n📡 REQUEST INFORMATION")
    print("-" * 65)

    print("URL          :", url)
    print("Status Code  :", response.status_code)
    print("Status       :", response.reason)
    print(f"Response Time: {elapsed:.3f} seconds")
    print(
        "Response Size:",
        f"{len(response.content) / 1024:.2f} KB"
    )
    print(
        "Content Type :",
        response.headers.get(
            "Content-Type",
            "Unknown"
        )
    )

    print("\n📊 RESPONSE HEADERS")
    print("-" * 65)

    for key, value in response.headers.items():
        print(f"{key}: {value}")

    content_type = response.headers.get(
        "Content-Type",
        ""
    ).lower()

    if "application/json" in content_type:

        try:

            data = response.json()

            print("\n🧩 JSON STRUCTURE")
            print("-" * 65)

            analyze_json(data)

            print("\n📄 JSON RESPONSE")
            print("-" * 65)

            print(
                json.dumps(
                    data,
                    indent=4
                )[:3000]
            )

        except ValueError:

            print(
                "\n⚠️ Content type says JSON, "
                "but response could not be parsed."
            )

    else:

        print("\n📄 RESPONSE PREVIEW")
        print("-" * 65)

        print(response.text[:1000])

    print("\n🏥 API HEALTH")
    print("-" * 65)

    if 200 <= response.status_code < 300:

        if elapsed < 1:
            print("🟢 Status : Healthy")
            print("🟢 Speed  : Excellent")

        elif elapsed < 3:
            print("🟢 Status : Healthy")
            print("🟡 Speed  : Acceptable")

        else:
            print("🟢 Status : Healthy")
            print("🔴 Speed  : Slow")

    elif 400 <= response.status_code < 500:

        print("🟡 Status : Client-side issue")

    elif 500 <= response.status_code < 600:

        print("🔴 Status : Server-side issue")

    else:

        print("⚪ Status : Unknown")

    print("\n" + "=" * 65)


def main():

    print("Python API Response Analyzer")

    url = input(
        "\nEnter API URL: "
    ).strip()

    if not url.startswith(("http://", "https://")):
        print("❌ Please enter a valid HTTP/HTTPS URL.")
        return

    analyze_api(url)


if __name__ == "__main__":
    main()
