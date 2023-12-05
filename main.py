import blockcypher

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ADDRESS = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'

def get_balance(address):
    blockcypher.api_key = API_KEY
    wallet_info = blockcypher.get_address_details(address)
    return wallet_info['final_balance'] / 10**8

def get_details(address):
    blockcypher.api_key = API_KEY
    wallet_info = blockcypher.get_address_details(address)
    transactions = wallet_info.get('txrefs', [])
    
    details_list = []
    for tx in transactions:
        hash_id = tx['tx_hash']
        amount = tx['value'] / 10**8
        
        details_list.append({
            'Hash ID': hash_id,
            'Amount': amount
        })
    
    return details_list

if __name__ == "__main__":
    balance = get_balance(ADDRESS)
    print(f"Balance of {ADDRESS}: {balance} BTC")

    with open('details.txt', 'w') as f:
        details = get_details(ADDRESS)
        for tx_details in details:
            f.write(f"Hash ID: {tx_details['Hash ID']}\n")
            f.write(f"Amount: {tx_details['Amount']} BTC\n\n")

    print("Done.")
