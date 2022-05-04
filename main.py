import os
import argparse

import requests

from typing import Optional, Final
from urllib.parse import urlparse
from dotenv import load_dotenv


RESOURCE_URL: Final = "https://api-ssl.bitly.com/v4/bitlinks"


def shorten_link(headers: dict, resource_url: str, 
    input_url: str) -> str:
    payload = {"long_url": input_url}
    response = requests.post(
        resource_url, headers=headers,     
        json=payload
    )
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(headers: dict, link: str,
    bitly_params: Optional[dict]) -> str:
    response = requests.get(
        link, headers=headers,
        params=bitly_params
    )
    response.raise_for_status()
    return response.json()["total_clicks"]


def cleanup_link(link: str) -> str:
    clean_link = urlparse(link).hostname + urlparse(link).path
    return clean_link


def is_bitlink(headers: dict, url: str) -> bool:
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser(
            description="The programm make short link by Bitly API service"
            )
    parser.add_argument("link", help="link to convert")
    args = parser.parse_args()
    load_dotenv()
    bitly_headers = {"Authorization": f"Bearer {os.getenv('BITLY_TOKEN')}"}
    clean_link = cleanup_link(args.link)
    if is_bitlink(headers=bitly_headers, url=f"{RESOURCE_URL}/{clean_link}"):
        clicks_count = count_clicks(
            headers=bitly_headers, 
            link=f"{RESOURCE_URL}/{clean_link}/clicks/summary",
            bitly_params={"units": -1}
        ) 
        print(f"Clicks: {clicks_count}")
    else:    
        link_shorten = shorten_link(
            headers=bitly_headers, 
            resource_url=RESOURCE_URL,
            input_url=args.link
        )
        print(f"Bitlink is: {link_shorten}")


if __name__ == "__main__":
    try:  
        main()
    except TypeError:
        print("Enter correct url!")
    except KeyboardInterrupt:
        print("Programm close!")
    except requests.HTTPError:
        print("HTTP Client Error!")
