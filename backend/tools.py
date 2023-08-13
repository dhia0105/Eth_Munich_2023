from web3 import Web3
from consts import contract_bytecode, contract_abi

royalty_fee=10
mumbai_chain_id = 80001
private_key="25dc082617530a4e6f92567295c7499b05611c6f097670ea7114a7da7fd4fd6b"
# i should not share this but i do nothave time for hiiding it please d ont profit from it. it has only development purposes
public_key="0x29FdAf9cE3672ECABD3fd65E3c4A5778fE6Ab442"
event_owner_example = "0xA046E4E8731C0a47eB9491798dc54e787197006D"
participant_example = "0xF73be91C9caC17dbb6Cc43653D0d70a6Bcc54455"
push_notification_contract = "0xb3971BCef2D791bc4027BbfedFb47319A4AAaaAa"
molecule_logic_contract = "0xE88C3d74Bba6Ac3ff78D3E426278475490D24B01"
molecule_contract_controller = "0xFA8e2c0485934b11A781B586252075b96e2f40A1"
ticket_contract="0x2B7be7ebF9Cf5c7fE1d0F7309F50A9101C226be3"
#maps between the address of smart contract of the event nft and the event name 
event_contract_map = {"eth_munich":ticket_contract}
def deploy_contract(name, symbol, event_owner):
    w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
    
    transaction = {
    'from': public_key,
    'gasPrice': w3.eth.gas_price,
    'gas': 10000000,
    'chainId': mumbai_chain_id,
    'nonce': w3.eth.get_transaction_count(public_key)
    }
    #signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    contract_transaction = contract.constructor(name, symbol, royalty_fee, event_owner).build_transaction(transaction)
    signed_transaction = w3.eth.account.sign_transaction(contract_transaction, private_key)
    tx_hash=w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    event_contract_map[name]=tx_receipt.contractAddress
    return tx_receipt.contractAddress

#address = deploy_contract("eth_mun", "emu", "0xA046E4E8731C0a47eB9491798dc54e787197006D")
#print(address)

def mint(event_name, token_id, event_owner, token_uri):
    w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
    contract_address = event_contract_map[event_name]
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    transaction = {
    'from': public_key,
    'gasPrice': w3.eth.gas_price,
    'gas': 200000,
    'chainId': mumbai_chain_id,
    'nonce': w3.eth.get_transaction_count(public_key)
    }
    minting_transaction = contract.functions.mintNft(token_uri, event_owner, token_id).build_transaction(transaction)
    signed_transaction = w3.eth.account.sign_transaction(minting_transaction, private_key)
    tx_hash=w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt
    
def add_to_registered(event_name, wallet_address, email_address):
    w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
    contract_address = event_contract_map[event_name]
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    transaction = {
    'from': public_key,
    'gasPrice': w3.eth.gas_price,
    'gas': 200000,
    'chainId': mumbai_chain_id,
    'nonce': w3.eth.get_transaction_count(public_key)
    }
    minting_transaction = contract.functions.addToRegisteredlist(wallet_address,[1]).build_transaction(transaction)
    signed_transaction = w3.eth.account.sign_transaction(minting_transaction, private_key)
    tx_hash=w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def check_registred(event_name, wallet_address, email_address):
    w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
    contract_address = event_contract_map[event_name]
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    registered_status = contract.functions.getRegistered(wallet_address).call()
    return {"registered?":registered_status}


#testing purposes
poor_address = "0xF73be91C9caC17dbb6Cc43653D0d70a6Bcc54455"
rich_address = "0x29FdAf9cE3672ECABD3fd65E3c4A5778fE6Ab442"
#receip = add_to_registred("s", rich_address, "h")
#print(receip)
print("rich : ", check_registred("eth_munich", rich_address, "a"))
print("poor : ", check_registred("eth_munich", poor_address, "b"))
#the rich is always registered
#What if its a new equal tax regulation event