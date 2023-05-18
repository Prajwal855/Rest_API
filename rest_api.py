import requests


class RestApiClass:

    def __init__(self, url):
        self.url = url
        pass

    def send_get(self, url):
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Error:' + response.status_code)

    #
    def upload_to_server(self):
        url = "https://jsonplaceholder.typicode.com/posts"


print("Testing 1 - Send Http GET request")
url = "https://jsonplaceholder.typicode.com/posts"
api_call = RestApiClass(url=url)
result = api_call.send_get(url=url)

if result:
    print(result)

    # print("Testing 2 - Send Http POST request")
    # upload_to_server()
