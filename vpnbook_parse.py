import urllib.request
from bs4 import BeautifulSoup


request = urllib.request.Request('http://www.vpnbook.com/freevpn')
with urllib.request.urlopen(request) as resp:
    page = resp.read()
html_page = page.decode()
soup = BeautifulSoup(html_page, 'html.parser')
result = soup.find('ul', class_='disc').find_all('li')
username = result[-2].find('strong').string
password = result[-1].find('strong').string

print('Username: ', username)
print('Password: ', password)

