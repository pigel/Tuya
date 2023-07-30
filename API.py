from tuyapy import TuyaApi
from config import USERNAME, PASSWORD, COUNTRY_CODE # login data from Smart Life

api = TuyaApi()
api.init(USERNAME, PASSWORD, COUNTRY_CODE)

discover = api.discover_devices()
print(discover)
