from scanner.manager import scan_message

...

async def scan_message(self, message):

    result = await scan_message(message)

    if result["score"] == 0:
        return

    print("=" * 60)
    print("SCAM DETECTED")
    print("User :", message.author)
    print("Score:", result["score"])

    for detection in result["detections"]:
        print(
            f"{detection.detector} | "
            f"{detection.value} | "
            f"{detection.score}"
        )

    print("=" * 60)