import requests
import logging

def check_ssl(host):
    url = f"https://ssl-checker.io/api/v1/check/{host}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        logging.warning(f"Error checking SSL for {host}: {e}")
        return None
