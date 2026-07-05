from pyzbar.pyzbar import decode
from PIL import Image


def scan_qr(image_path: str):
    """
    Scan an image for QR codes.

    Returns:
        list[str] - Decoded QR code contents.
    """

    try:
        image = Image.open(image_path)
        codes = decode(image)

        results = []

        for code in codes:
            try:
                data = code.data.decode("utf-8")
            except UnicodeDecodeError:
                data = code.data.decode("latin-1", errors="ignore")

            results.append(data)

        return results

    except Exception as e:
        print(f"[QR ERROR] {e}")
        return []