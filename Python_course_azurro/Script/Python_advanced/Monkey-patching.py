import requests 
def get(url: str): 
    return '<TEST RESPONSE>'
requests.get = get 

# to download the original data , we have to use the previous line commented so that
data = requests.get('https://www.apple.com')

print(data)