import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


def check_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("\n🔍 Scanning:", url)
    print("-" * 70)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as error:
        print("❌ Unable to open website")
        print("Error:", error)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    checked = set()

    working = 0
    broken = 0
    skipped = 0

    print(f"🔗 Links found: {len(links)}\n")

    for tag in links:

        link = tag.get("href").strip()

        if not link:
            continue

        # Ignore local page references
        if link.startswith("#"):
            skipped += 1
            continue

        # Ignore special links
        if link.startswith(("mailto:", "tel:", "javascript:")):
            skipped += 1
            continue

        full_url = urljoin(url, link)

        if full_url in checked:
            continue

        checked.add(full_url)

        try:

            start = time.time()

            result = requests.head(
                full_url,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )

            # Some websites don't support HEAD requests
            if result.status_code >= 400:
                result = requests.get(
                    full_url,
                    headers=headers,
                    timeout=10,
                    allow_redirects=True,
                    stream=True
                )

            elapsed = time.time() - start

            status = result.status_code

            if status < 400:

                working += 1

                print(
                    f"✅ {status} | "
                    f"{elapsed:.2f}s | "
                    f"{full_url}"
                )

            else:

                broken += 1

                print(
                    f"❌ {status} | "
                    f"{elapsed:.2f}s | "
                    f"{full_url}"
                )

        except requests.RequestException:

            broken += 1

            print(
                f"❌ ERROR | "
                f"{full_url}"
            )

    print("\n" + "=" * 70)
    print("📊 LINK CHECK SUMMARY")
    print("=" * 70)

    print(f"Total links checked : {working + broken}")
    print(f"Working links       : {working}")
    print(f"Broken links        : {broken}")
    print(f"Skipped links       : {skipped}")

    if broken == 0:
        print("\n🎉 No broken links found!")

    else:
        print(f"\n⚠️ {broken} broken link(s) detected.")


if __name__ == "__main__":

    website = input(
        "Enter website URL: "
    ).strip()

    if not website.startswith(("http://", "https://")):
        website = "https://" + website

    check_links(website)
