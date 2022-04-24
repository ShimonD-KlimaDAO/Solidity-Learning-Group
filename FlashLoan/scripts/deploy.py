from brownie import MyV2FlashLoan, accounts

def main():

    account = accounts.load('deployment_private')

    aave_addressprovider='0xd05e3E715d945B59290df0ae8eF85c1BdB684744'

    MyV2FlashLoan.deploy(aave_addressprovider, {'from': account, 'priority_fee': "80 gwei"}, publish_source = True)