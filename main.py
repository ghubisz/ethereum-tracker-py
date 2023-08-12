from requests import get
from matplotlib import pyplot as plt

API_KEY = "PXP99MX7J2WFNXWWUGSKADRVTIHAQ1F1I9"
BASE_URL = "https://api.etherscan.io/api"
address = "0x73bceb1cd57c711feac4224d062b0f6ff338501e"
ETHER_VALUE = 10 ** 18

def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url

def get_account_balance(address):

    get_balance_url = make_api_url("account", "balance", address, tag="latest", x="2")
    response = get(get_balance_url)
    data = response.json()

    value = (int(data["result"]) / ETHER_VALUE)
    return value

def get_transactions(address):
    get_transactions_url = make_api_url("account", "txlist", address, startblock =0, endblock=99999999, page=1, offset = 10000, sort="asc")
    response = get(get_transactions_url)
    data = response.json()["result"]
    
    for tx in data:
        to = tx["to"]
        from_addr = tx["from"]
        value = tx["value"]
        gas = tx["gasUsed"]
        time = tx["timeStamp"]
        print("------------------")
        print("To:", to)
        print("From:", from_addr)
        print("Value:", value)
        print("Gas Used:", gas)
        print("Time:", time)

get_transactions(address)
