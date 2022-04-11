from brownie import NBO, NBOFaucet, accounts

def main():

    account = accounts.load('deployment_private')

    # Deploy NBO and NBO faucet
    nbo = NBO.deploy('10000000 ether', {'from': account, 'priority_fee': "10 gwei"}, publish_source = True) # 10MM NBOs minted
    faucet = NBOFaucet.deploy(nbo, 18, {"from":account, 'priority_fee': "10 gwei"}, publish_source = True)

    # Transfer all NBO tokens to the faucet
    nbo.transfer(faucet, '10000000 ether', {'from': account})

