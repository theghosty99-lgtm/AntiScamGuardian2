import aiohttp
import os
import uuid

TEMP_FOLDER = "assets/temp"

os.makedirs(TEMP_FOLDER, exist_ok=True)


async def download_image(url: str):
    """
    Download image from Discord attachment URL.
    Returns local file path or None.
    """

    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(TEMP_FOLDER, filename)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:

                if resp.status != 200:
                    return None

                with open(filepath, "wb") as f:
                    f.write(await resp.read())

        return filepath

    except Exception as e:
        print(f"[IMAGE DOWNLOAD ERROR] {e}")
        return None


def cleanup_file(filepath: str):
    """
    Delete temporary image file.
    """

    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        print(f"[FILE DELETE ERROR] {e}")