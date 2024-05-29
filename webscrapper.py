import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sandbox.oxylabs.io/products')
results = []
other_results = []

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.find_all(attrs={'class': 'product-card'}):
    name = a.find('h4')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs={'class': 'product-card'}):
    name2 = b.find(attrs={'class': 'price-wrapper'})
    if name2 not in other_results:
        other_results.append(name2.text)

df = pd.DataFrame({'Names': results, 'Prices': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')