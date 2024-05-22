import requests

while True:
    c = input("구문입력: ").replace(" ", "_").replace("\"", "\'")
    response = requests.post('http://localhost:8888', json={'command': c, 'target': 'py'})
    print(response.text)