import re
import requests

url_ier = 'https://example.com'
response_iea = requests.get(url)
emails_ID = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)

print(emails_ID)
