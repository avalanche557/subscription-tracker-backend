import re


KNOWN_SUBSCRIPTIONS = [
    "Netflix",
    "Spotify",
    "Amazon Prime",
    "YouTube",
    "ChatGPT",
    "Apple",
    "Google One",
    "Swiggy One",
    "Zomato Gold",
]


def extract_amount(message):

    patterns = [
        r'₹\s?(\d+)',
        r'Rs\.?\s?(\d+)',
        r'INR\s?(\d+)',
    ]

    for pattern in patterns:

        match = re.search(pattern, message)

        if match:
            return float(match.group(1))

    return None


def detect_merchant(message):

    for merchant in KNOWN_SUBSCRIPTIONS:

        if merchant.lower() in message.lower():
            return merchant

    return None


def is_subscription_message(message):

    keywords = [
        "subscription",
        "renewed",
        "autopay",
        "membership",
        "monthly plan",
        "yearly plan",
    ]

    for keyword in keywords:

        if keyword.lower() in message.lower():
            return True

    return False