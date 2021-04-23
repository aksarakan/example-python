import requests
import os

# file path
file = ''

# generate token in web profile
token = ''

# document type 'ktp', 'npwp', 'sim-2019'
type = 'ktp'

url = 'https://api.aksarakan.com/document'


if not file:
    raise Exception('file not set')

if not token:
    raise Exception('token not set')


headers = {
    'Authentication': "bearer " + token,
}

files = {
    'file': (os.path.basename(file), open(file, 'rb'))
}

response = requests.request('PUT', url + '/' + type, files=files, headers=headers)

print(response.content)