from algosdk.v2client import algod 
from algosdk import mnemonic,account
from algosdk import transaction

ALGOD_ADDR = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""
try:
    creator_mnemonic = input("🔐 Please enter your Algorand account mnemonic (25 words): ")
    creator_privatekey = mnemonic.to_private_key(creator_mnemonic)
    creator_address = account.address_from_private_key(creator_privatekey)
    algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDR)
except Exception as e:
    print(f"Error creating Algod client: {e}")
    exit(1)

def create_asa(algo_client, creator_privatekey, creator_address,unit_name,asset_name,total=100000,url=None,note=None) -> None:
    params = algo_client.suggested_params()
    txn = transaction.AssetConfigTxn(
    sender=creator_address,
        sp=params,
        total=total,
        default_frozen=False,
        unit_name=unit_name,
        asset_name=asset_name,
        manager=creator_address,
        reserve=creator_address,
        freeze=creator_address,
        clawback=creator_address,
        url=url,
        note=note,
    )
    stxn = txn.sign(creator_privatekey)
    txid = algo_client.send_transaction(stxn)
    print(f"Transaction ID: {txid}")
    transaction.wait_for_confirmation(algo_client, txid)
    asset_id = algo_client.pending_transaction_info(txid)["asset-index"]
    print(f"Asset ID: {asset_id}")
    print("😃 ASA created successfully!")
# create_asa(
#     algo_client=algod_client,
#     creator_privatekey=creator_privatekey,
#     creator_address=creator_address,
#     unit_name="TEST",
#     asset_name="Test Asset",
#     total=1000000,
#     url="",
#     note="This is a test ASA".encode("utf-8"),
# )
unit_name = input("Enter the unit name of the ASA: ")
asset_name = input("Enter the asset name of the ASA: ")
total = int(input("Enter the total supply of the ASA: "))
url = input("Enter the URL of the ASA: ")
note = input("Enter a note for the ASA: ").encode("utf-8")
try:
    create_asa(
    algo_client=algod_client,
    creator_privatekey=creator_privatekey,
    creator_address=creator_address,
    unit_name=unit_name,
    asset_name=asset_name,
    total=total,
    url=url,
    note=note,
    )
except Exception as e:
    print(f"😞 Error creating ASA: {e}")
finally:
    exit(0)