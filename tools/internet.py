from typing import Optional
import requests


def get_json_from_url(url: str) -> Optional[dict]:
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return None
