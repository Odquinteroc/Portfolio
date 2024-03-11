import requests
import pprint
import json

printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    url = 'https://httpbin.org/post' #https://httpbin.org/get?Name=Oscar&Curse=Python this is how we query through the get request
    payload ={'Name':'Oscar', 'Curse':'Python'}
    headers = {'Content-Type':'application/json', 'access_token':'1234'}
    response = requests.post(url, data=json.dumps(payload), headers= headers) #json =payload
    # there are two arguments where we can send data, Json and Data, if we used Json it itself will serialize the data and if we used Data we need to serialize the data

    print(response.url)

    if response.status_code == 200: # the status of the server will be store in the argument status_code

        headers_response = response.headers
        server = headers_response['server']
        print(server)
        