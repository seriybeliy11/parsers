import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

url = ''
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

text = soup.get_text()
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
keywords = [token for token in tokens if token not in stop_words]

print(keywords)
