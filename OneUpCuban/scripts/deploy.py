from brownie import OneUpCuban, accounts

def main():

    account = accounts.load('deployment_private')

    OneUpCuban.deploy({'from': account, 'priority_fee': "50 gwei"}, publish_source = True)