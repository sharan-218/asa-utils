from algosdk.v2client import algod
from algosdk.encoding import is_valid_address
from algosdk.util import microalgos_to_algos

def get_balance(address,network) -> float:
    if not is_valid_address(address):
        print("Oops! Invalid Algorand address 😬")
        exit(1)
    if network == "testnet":
        ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
    elif network == "mainnet":
        ALGOD_ADDRESS = "https://mainnet-api.algonode.cloud"
    else:
        print("Invalid network. Please enter 'mainnet' or 'testnet'❗")
        exit(1)
    algod_token =""
    client = algod.AlgodClient(algod_token,ALGOD_ADDRESS)
    try:
        account_info = client.account_info(address)
        balance = account_info.get("amount") 
        balance = microalgos_to_algos(balance)
        # print(f"Network: {network}")
        # print(f"Address: {address}")
        # print(f"Asset information: {asset_info['assets']}")
        # asset_info = client.account_info(address)
        return balance
    except Exception as e:
        print(f"Error fetching account info: {e}")
        return None
address = input("Enter the Algorand address: ")
network = input("Enter the network (mainnet/testnet): ").strip().lower()
balance = get_balance(address,network)
if balance is not None:
    print(f"💰 Balance is {balance:.5f} ALGO")