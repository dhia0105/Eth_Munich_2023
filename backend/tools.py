from web3 import Web3
from consts import contract_bytecode, contract_abi

royalty_fee=10
mumbai_chain_id = 80001

def deploy_contract(name, symbol, event_owner):
    
    w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
    # i should not share this but i do nothave time for hiiding it please d ont profit from it. it has only development purposes
    public_key="0x29FdAf9cE3672ECABD3fd65E3c4A5778fE6Ab442"
    private_key="25dc082617530a4e6f92567295c7499b05611c6f097670ea7114a7da7fd4fd6b"
    transaction = {
    'from': public_key,
    'gasPrice': w3.eth.gas_price,
    'gas': 10000000,
    'chainId': mumbai_chain_id,
    'nonce': w3.eth.get_transaction_count(public_key)
    }
    #signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    ExampleContract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    contract_transaction = ExampleContract.constructor(name, symbol, royalty_fee, event_owner).build_transaction(transaction)
    signed_transaction = w3.eth.account.sign_transaction(contract_transaction, private_key)
    tx_hash=w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt.contractAddress

address = deploy_contract("eth_mun", "emu", "0xA046E4E8731C0a47eB9491798dc54e787197006D")
print(address)