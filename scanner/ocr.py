import easyocr

# Initialize the OCR reader once when the bot starts
reader = easyocr.Reader(
    ["en"],
    gpu=False
)


def read_text(image_path: str):
    """
    Read all text from an image.
    Returns a single lowercase string.
    """

    try:
        result = reader.readtext(image_path)

        text = []

        for item in result:
            # item format:
            # (bbox, detected_text, confidence)
            text.append(item[1])

        return " ".join(text).lower()

    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return ""