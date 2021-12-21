import requests

url='https://cio.go.jp/sites/default/files/uploads/documents/digital/vaccinecert_list.csv'
filename='./vaccinecert_list.csv'

urlData = requests.get(url).content

with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
    f.write(urlData)