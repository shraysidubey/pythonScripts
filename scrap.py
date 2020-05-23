import requests
from bs4 import BeautifulSoup

def parseRow(row):
    LL = []
    tds = row.find_all("td")
    for el in tds:
        LL.append(el.text.replace('\n', ''))
    return LL


url = 'https://www.codechef.com/contests'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'html.parser')


tables = soup.find_all("table", attrs={"class": "dataTable"})
L = []
for table_data in tables:
    rows = table_data.find_all("tr")
    for row in rows:
        LL = parseRow(row)
        if len(LL) != 0:
            L.append(LL)
print(L)

File_object = open("Beauty.txt","w")
File_object.write(str(L))
File_object.close()

