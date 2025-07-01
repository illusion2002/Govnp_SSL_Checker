import logging
from utils.link_extractor import get_links_from_url
from utils.ssl_checker import check_ssl
from utils.email_alert import send_email_alert
from utils.sheet_handler import get_sheet, chunked

def update_ssl_info():
    logging.info("Starting SSL check...")
    sheet = get_sheet()

    raw_urls = [u.strip() for u in sheet.col_values(1) if u.strip()]

    gov_np_domains = set()
    for base_url in raw_urls:
        if not base_url.startswith("http"):
            base_url = "https://" + base_url
        links = get_links_from_url(base_url)
        gov_np_domains.update(links)

    seen = set()
    for batch in chunked(list(gov_np_domains), 50):
        for host in batch:
            if host in seen:
                continue
            seen.add(host)

            ssl_data = check_ssl(host)
            if not ssl_data or not ssl_data.get("result"):
                continue

            result = ssl_data["result"]
            days_left = result.get("days_left", 0)

            row_data = [
                host,
                ssl_data.get("status", ""),
                ssl_data.get("response_time_sec", ""),
                result.get("resolved_ip", ""),
                result.get("issued_to", ""),
                result.get("issued_o", ""),
                result.get("issuer_c", ""),
                result.get("issuer_o", ""),
                result.get("issuer_cn", ""),
                result.get("cert_sn", ""),
                result.get("cert_sha1", ""),
                result.get("cert_alg", ""),
                result.get("cert_ver", ""),
                result.get("cert_sans", ""),
                result.get("cert_exp", ""),
                result.get("cert_valid", ""),
                result.get("valid_from", ""),
                result.get("valid_till", ""),
                result.get("validity_days", ""),
                result.get("days_left", ""),
                result.get("valid_days_to_expire", ""),
                result.get("hsts_header_enabled", "")
            ]

            try:
                cell = sheet.find(host)
                sheet.delete_row(cell.row)
            except:
                pass

            sheet.append_row(row_data)

            if days_left <= 7:
                send_email_alert(host, days_left)

    logging.info("SSL check completed.")
