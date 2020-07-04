'''author:vishwanath hiremath
date:03/02/2020
summary:gets the data from the webpage of dr.ait results'''

from bs4 import BeautifulSoup
import requests
import pandas as pn

value = {'get_ry': '<enter the date as displayed in result page>', 'get_usn': '<usn>'}

response = requests.post(url='http://results.drait.in/ug_result_info_see.php', data=value)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.table
rows = table.find_all("tr")
field = []

for row in rows:
    if row.find('th'):
        heading = row.find_all('th')
    field.append([each.get_text() for each in row.find_all('td')])
col = [each.get_text() for each in heading]

# to remove empty fields in the table
for each in field:
    if each == []:
        field.remove(each)

# Data analysis using pandas starts here
df = pn.DataFrame(columns=col, data=field)
df.columns = df.columns.str.replace(' ', '')
df.columns = [x.upper() for x in df.columns]
df.rename(columns={'ATT-L': 'ATT-1'}, inplace=True)

# prints the result in data frame format
print(df)

# to get the grades in list to calculate sgpa
# this is continued part....
grade = df['SEEGRADE']
credit = df['CREDITS(R)']
