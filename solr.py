import urllib3
import json

http = urllib3.PoolManager()

# Upload du lieu
url = 'http://localhost:8983/solr/my_test/update?commit=true'
myheaders = {'Content-Type': 'application/json'}

f = open('fb_comments_data.json')
my_data = json.load(f)
# print(my_data[1])

data = json.dumps(my_data).encode('utf-8')
# print(data)

response = http.request(
    'POST', url, body=data, headers=myheaders)
# response = http.request(
#    'POST', url, body='fb_comments_data.json', headers=myheaders)


# truy van
"""
connection = urlopen('http://localhost:8983/solr/my_test/select?q=Image:*%20OR%20UserName:*Ng*&wt=python')
response = eval(connection.read())

connection = urlopen('http://localhost:8983/solr/my_test/select?q=Image:*%20OR%20UserName:*Ng*&wt=json')
"""
query = input("Enter your query: ")
url = 'http://localhost:8983/solr/my_test/select?q=' + query + '&wt=json'
response = http.request('GET', url)
#print("1", dir(response))
print("2", response.status)

data = json.loads(response.data)
#print("3", data)

# Print the name of each document.
print(data['response']['numFound'])
for document in data['response']['docs']:
    print("  DATA =", document)

"""
res = browser.find_element(By.XPATH, xpathRES).text
            snum = re.search(r'\d*[.][\d]+|\d+', res).group()
            resNum = ""
            if "." in snum:
                resNum = float(snum)
            else:
                resNum = int(snum)
            sk = res.split(snum)[1]
            if sk[0]=="k" or sk[0]=="K":
                resNum *= 1000
            elif sk[0]=="M":
                resNum *= 1000000
            
            resInt = int(resNum)
"""