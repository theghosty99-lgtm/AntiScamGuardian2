from scanner.keyword_detector import scan as keyword_scan
from scanner.url_scanner import scan as url_scan


async def scan_message(message):

    detections = []

    detections.extend(keyword_scan(message.content))
    detections.extend(url_scan(message.content))

    score = sum(d.score for d in detections)

    return {
        "score": score,
        "detections": detections
    }