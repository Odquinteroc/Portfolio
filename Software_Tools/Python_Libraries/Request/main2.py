import requests
import pprint

printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args ={'Name':'Oscar', 'Curse':'Python'}
    response = requests.get(url, params = args)

    if response.status_code == 200: # the status of the server will be store in the argument status_code

        content = response.text #response.content returns the raw binary content of the response. It returns the response content as bytes object and response.text returns the content of the response, decoded using the detected encoding or a specified encoding if provided. It returns the response content as a string object.
        
        print(content)
        