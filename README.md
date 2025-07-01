🔍 What It Does
This tool automates SSL monitoring for Nepali government domains (.gov.np):

- Reads a list of base websites from a Google Sheet
- Sends HTTP GET requests to those sites
- Extracts all anchor (<a>) tags from each page
- Filters and collects only links ending with .gov.np
- Checks SSL certificate status for those filtered domains
- Updates the Google Sheet with detailed SSL data (one row per domain)
- Sends email alerts if a certificate expires within 7 days
- Runs automatically every Monday at 08:00 AM


## ⚙️ Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/govnp-ssl-monitor.git
cd govnp-ssl-monitor
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set up Google API credentials**
- Create a service account and download the creds.json file from Google Cloud Console
- Share your target Google Sheet with the service account email
- Place the creds.json file in the project directory and update the path in config.py

4. **Configure email settings**
- Use an App Password if you're using Gmail
- Set your email credentials in config.py
