from bs4 import BeautifulSoup
import requests
import csv
import lxml.html as lh

page = requests.get('https://www.nationsonline.org/oneworld/countries_of_the_world.htm')

doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
[len(T) for T in tr_elements[:12]]

tr_elements = doc.xpath('//tr')
csv_file = open('scrape_countries.csv','w')

csv_writer = csv.writer(csv_file)

col=[]
i=0
for t in tr_elements:
    i+=1
    name=t.text_content()
    #print(i,name)
    
    col.append((name,[]))

for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    i=0
    for t in T.iterchildren():
        data=t.text_content() 
        try:
        	csv_writer.writerow([data])
        except:
        	pass
csv_file.close()
