import requests
import pprint
import json

printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    url = 'https://httpbin.org/put' 
    payload ={'Name':'Oscar', 'Curse':'Python'}
    headers = {'Content-Type':'application/json', 'access_token':'1234'}
    response = requests.put(url, data=json.dumps(payload), headers= headers) 

    print(response.url)

    if response.status_code == 200: # the status of the server will be store in the argument status_code

        headers_response = response.headers
        server = headers_response['server']
        print(server)
        