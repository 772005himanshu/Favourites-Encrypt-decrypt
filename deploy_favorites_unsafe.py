from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os



load_dotenv()
RPC_URL = os.getenv("RPC_URL")
# MY_ADDRESS = os.getenv("MY_ADDRESS")
# MY_PRIVATE_KEY = os.getenv("MY_PRIVATE_KEY")


def main():
    print("Let's read in Vyper code and deploy it!")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    with open("favorites.vy","r") as favorites_file:
        favorites_code = favorites_file.read()
        compliation_details = compile_code(favorites_code,output_formats = ["abi","bytecode"])
        # print(compliation_details)
        
    print("Getting environment variables...")
    my_address = os.getenv("MY_ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")
    
    favorites_contract = w3.eth.contract(abi=compliation_details["abi"],bytecode=compliation_details["bytecode"])
    # print(favorites_contract)
    
    
    print("Building the transaction..")
    
    nonce = w3.eth.get_transaction_count(my_address)
    transaction = favorites_contract.constructor().build_transaction({
        "nonce": nonce,
        "from": my_address,
        "gasPrice": w3.eth.gas_price,
        
    })
    # transaction["nonce"] = nonce
    # print(transaction)
    signed_transaction = w3.eth.account.sign_transaction(transaction,private_key=private_key)
    print(signed_transaction)
    print(signed_transaction)
    
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"My TX hash is {tx_hash}")
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! contract deployed to {tx_receipt.contractAddress}")
    
    
    #  This manually creating the tx
    # transaction = {
    #     # from
    #     # to
    #     # 
    # }
    
if __name__ == "__main__":
    main()
