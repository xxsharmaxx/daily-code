from collections import Counter
import re

def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        lines = text.splitlines()
        words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

        word_count = Counter(words)

        print("\n" + "=" * 40)
        print("       FILE STATISTICS ANALYZER")
        print("=" * 40)

        print(f"File: {filename}")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {len(text)}")
        print(f"Unique Words: {len(word_count)}")

        print("\nTop 10 Most Common Words:")
        print("-" * 40)

        for word, count in word_count.most_common(10):
            print(f"{word:<20} {count}")

        print("=" * 40)

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

    except Exception as error:
        print(f"Error: {error}")


filename = input("Enter text file name: ")
analyze_file(filename)
