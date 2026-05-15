import random
import time

love_quotes = [
    "Love is composed of a single soul inhabiting two bodies.",
    "Every love story is beautiful.",
    "Together is a wonderful place to be.",
    "You are my favorite notification.",
    "Love grows when shared."
]

personality_types = [
    "Romantic",
    "Funny",
    "Intelligent",
    "Mysterious",
    "Adventurous",
    "Creative"
]

events = [
    "went on a candlelight dinner ❤️",
    "watched a movie together 🎬",
    "traveled to Paris ✈️",
    "had a cute argument 😅",
    "played games all night 🎮",
    "shared ice cream 🍦",
    "went on a beach walk 🌊"
]


def loading():
    print("\nAnalyzing hearts", end="")

    for _ in range(5):
        time.sleep(0.5)
        print(".", end="")

    print("\n")


def heart_animation():
    hearts = [
        "  ❤️     ❤️  ",
        " ❤️❤️   ❤️❤️ ",
        "❤️❤️❤️ ❤️❤️❤️",
        " ❤️❤️❤️❤️❤️ ",
        "  ❤️❤️❤️❤️  ",
        "    ❤️❤️    ",
        "      ❤️     "
    ]

    for line in hearts:
        print(line)
        time.sleep(0.2)


def compatibility_score(name1, name2):

    base = random.randint(40, 100)

    common_letters = len(set(name1.lower()) & set(name2.lower()))

    score = min(100, base + common_letters)

    return score


def relationship_level(score):

    if score >= 90:
        return "Soulmates 💍"

    elif score >= 75:
        return "Perfect Match ❤️"

    elif score >= 60:
        return "Cute Couple 😊"

    elif score >= 45:
        return "Complicated 😅"

    else:
        return "Better as Friends 🤝"


def main():

    print("======================================")
    print("      AI LOVE COMPATIBILITY TEST")
    print("======================================")

    name1 = input("\nEnter First Name: ")
    name2 = input("Enter Second Name: ")

    loading()

    heart_animation()

    type1 = random.choice(personality_types)
    type2 = random.choice(personality_types)

    score = compatibility_score(name1, name2)

    level = relationship_level(score)

    quote = random.choice(love_quotes)

    event = random.choice(events)

    print("\n========== LOVE REPORT ==========\n")

    print(f"{name1}'s Personality : {type1}")
    print(f"{name2}'s Personality : {type2}")

    print(f"\nCompatibility Score: {score}%")

    print(f"Relationship Status: {level}")

    print(f"\nFuture Prediction:")
    print(f"{name1} and {name2} {event}")

    print(f"\nLove Quote:")
    print(f"\"{quote}\"")

    print("\n===================================")

    if score >= 80:
        print("Destiny says you belong together ❤️")

    elif score >= 60:
        print("There is strong potential between you ✨")

    else:
        print("A friendship may bloom into something special 🌸")


if __name__ == "__main__":
    main()
