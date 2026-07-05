from dataclasses import dataclass

@dataclass
class Detection:
    detector: str
    value: str
    score: int


KEYWORDS = {
    # Discord
    "free nitro": 20,
    "discord gift": 20,
    "gift inventory": 20,

    # Crypto
    "wallet": 15,
    "crypto": 15,
    "airdrop": 20,
    "seed phrase": 40,

    # Fake giveaway
    "claim now": 25,
    "limited time": 15,
    "verify account": 25,

    # Fake payment
    "withdraw successful": 30,
    "payment received": 20,

    # Common scam wording
    "click here": 10,
    "claim reward": 20,
    "free skin": 20,
}


def scan(text: str):

    detections = []

    if not text:
        return detections

    lower = text.lower()

    for keyword, score in KEYWORDS.items():

        if keyword in lower:
            detections.append(
                Detection(
                    detector="Keyword",
                    value=keyword,
                    score=score
                )
            )

    return detections