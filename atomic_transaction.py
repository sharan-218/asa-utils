from algosdk import mnemonic, account
from algosdk.transaction import PaymentTxn,assign_group_id, wait_for_confirmation
from algosdk.v2client import algod


ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"

ALGOD_TOKEN = ""
client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)
mnemonic1 = input("Enter the mnemonic 1: ")
mnemonic2 = input("Enter the mnemonic 2: ")

sk1 = mnemonic.to_private_key(mnemonic1)
sk2 = mnemonic.to_private_key(mnemonic2)

pk1 = account.address_from_private_key(sk1)
pk2 = account.address_from_private_key(sk2)
print(f"Address 1: {pk1}")
print(f"Address 2: {pk2}")

params = client.suggested_params()

amt1 = float(input("Amount 1: "))
amt2 = float(input("Amount 2: "))

txn1 = PaymentTxn(pk1,params,pk2,int(amt1 * 1e6))
txn2 = PaymentTxn(pk2,params,pk1,int(amt2 * 1e6))
group = assign_group_id([txn1, txn2])
signed_txn1 = txn1.sign(sk1)
signed_txn2 = txn2.sign(sk2)

txn_id = client.send_transactions([signed_txn1, signed_txn2])
print(f"🪪 Atomic transaction ID: {txn_id}")
confirmed_txn = wait_for_confirmation(client, txn_id)
print(f"✅ Atomic transaction confirmed in round {confirmed_txn['confirmed-round']}")