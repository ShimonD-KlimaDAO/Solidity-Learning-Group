from brownie import SimpleStorage, accounts

def main():

    account = accounts.load('SLG_deploy')

    SimpleStorage.deploy({'from': account})