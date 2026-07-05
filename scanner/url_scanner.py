import re
from urllib.parse import urlparse

from scanner.keyword_detector import Detection

URL_REGEX = re.compile(r"https?://[^\s]+")

SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "cutt.ly",
    "rb.gy",
    "t.ly",
    "is.gd",
    "goo.gl"
}


def scan(text: str):

    detections = []

    if not text:
        return detections

    urls = URL_REGEX.findall(text)

    for url in urls:

        score = 10

        domain = urlparse(url).netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        if domain in SHORTENERS:
            score += 20

        detections.append(
            Detection(
                detector="URL",
                value=url,
                score=score
            )
        )

    return detections