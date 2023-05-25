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
    def send_post(self,url):
        payload = {
            "title":"foo",
            "body":"Hi",
            "userId":1
        }
        response = requests.post(url=url, data=payload)
        if response.status_code == 200:
            print("POST Request is Successfully")
        else:
            print("POST Request is Failed")

        print(response.text)


print("Testing 1 - Send Http GET request")
url = "https://jsonplaceholder.typicode.com/posts"
api_call = RestApiClass(url=url)
result = api_call.send_get(url=url)


print("Testing 2 - Send Http POST request")
url = "https://jsonplaceholder.typicode.com/posts"
api_call = RestApiClass(url=url)
result2 = api_call.send_post(url=url)

if result and result2:
    print(result)
    print(result2)

