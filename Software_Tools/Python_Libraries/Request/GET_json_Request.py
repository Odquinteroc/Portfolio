import requests
import pprint
import json

printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    url = 'https://httpbin.org/get' #https://httpbin.org/get?Name=Oscar&Curse=Python this is how we query through the get request
    args ={'Name':'Oscar', 'Curse':'Python'}
    response = requests.get(url, params = args)
    print(response.url)

    if response.status_code == 200: # the status of the server will be store in the argument status_code

        # response_json = response.json() # dictionary
        # origins = response_json['origin']

        response_json =json.loads(response.text)
        origins = response_json['origin']
        
        print(origins)
        