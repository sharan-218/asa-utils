from algosdk import mnemonic,account 
import json
import os 
private_key, address = account.generate_account()
mnemonic_phrase = mnemonic.from_private_key(private_key)
wallet_details = {
    "address": address,
    "mnemonic": mnemonic_phrase,
    "private_key": private_key
}
filename = f"wallet_{address[:6]}.json"
os.makedirs("accounts", exist_ok=True)
try:
    with open(f"accounts/{filename}","w") as f:
        json.dump(wallet_details, f, indent=4)
except Exception as e:
    print(f"Error writing to file: {e}")

print("Wallet created successfully!✅")
print("Mnemonic:📜", mnemonic_phrase)
print("Private Key:🗝️", private_key)
print("Filename: ", filename)
print("Address:🔑", address)
print("Wallet details saved in accounts folder.")
print("Dont share your mnemonic/private key with anyone!🚫")