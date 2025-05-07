from algosdk.v2client import algod
from algosdk import mnemonic,account,transaction
def get_algod_client(network="testnet"):
    algod_address = {
        "testnet": "https://testnet-api.algonode.cloud",
        "mainnet": "https://mainnet-api.algonode.cloud",
    }.get(network)
    if not algod_address:
        raise ValueError(f"Unsupported network: {network}. Use 'testnet' or 'mainnet'.")
        exit(1)
    algod_token = ""
    return algod.AlgodClient(algod_token, algod_address)

def send_transaction(receiver: str, amount:float, network: str="testnet",creator_mnemonic: str=None):
    try:
        algod_client = get_algod_client(network)
        sender_privatekey = mnemonic.to_private_key(creator_mnemonic)
        sender_address = account.address_from_private_key(sender_privatekey)
        print(f"📤 Sender Address: {sender_address}")
        params = algod_client.suggested_params()

        unsigned_txn = transaction.PaymentTxn(
            sender=sender_address,
            receiver=receiver,
            amt=amount,
            sp=params,
            note="Transaction using asa-util".encode(),
        )
        signed_txn = unsigned_txn.sign(sender_privatekey)
        txid = algod_client.send_transaction(signed_txn)
        print(f"Transcation sent with txID: {txid}")
        transaction.wait_for_confirmation(algod_client, txid)
        print(f"Transaction confirmed with txID: {txid}")
        return txid
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None
if __name__ == "__main__":
    creator_mnemonic = input("Enter the mnemonic of the sender account: ")
    receiver = input("Enter the receiver address: ")
    amount = float(input("Enter the amount to send (in ALGO): "))
    network = input("Enter the network (testnet/mainnet): ").strip().lower()
    send_transaction(receiver, amount, network, creator_mnemonic)


