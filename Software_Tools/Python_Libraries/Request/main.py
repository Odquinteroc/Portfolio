import requests

if __name__ == '__main__':
    url = 'https://www.google.ca/'
    response = requests.get(url)

    if response.status_code == 200: # the status of the server will be store in the argument status_code

        content = response.content #response.content returns the raw binary content of the response. It returns the response content as bytes object and response.text returns the content of the response, decoded using the detected encoding or a specified encoding if provided. It returns the response content as a string object.
        with open('google.html', 'wb') as file:
            file.write(content)
        
    