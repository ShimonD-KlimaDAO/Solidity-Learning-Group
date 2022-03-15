from brownie import SimpleStorage, accounts, config

def deploy_simple_storage():

    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(9, {"from": account})
    transaction.wait(1)
    stored_value = simple_storage.retrieve()
    print(stored_value)

def main():
    
    deploy_simple_storage()
