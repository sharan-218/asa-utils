from algosdk.v2client import algod
from algosdk.encoding import is_valid_address

address = input("Enter the Algorand address: ")
if not is_valid_address(address):
    print("😬 Invalid Algorand address.")
    exit(1)
network = input("Enter the network (mainnet/testnet): ").strip().lower()
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
    balance = account_info.get("amount") / 1e6
    print(f"Network: {network}")
    print(f"Address: {address}")
    print(f"💰 Balance is {balance:.5f} ALGO")
except Exception as e:
    print(f"Error fetching account info: {e}")
