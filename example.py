from hbr_client import ApiClient, UserClient
from time import sleep
import pprint



'''
client = ApiClient(token="token")

for i in range(10):
    r = client.save({'x':i})
    print(r.status_code)
    print(r.text)
    sleep(1)
'''

client = UserClient('email', 'pass')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(client.get_data())
