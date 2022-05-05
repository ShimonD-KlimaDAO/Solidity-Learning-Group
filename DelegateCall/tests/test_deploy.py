from brownie import A, B, accounts

def test_deploy():

    account = accounts[0]

    # Deploy B first, then A
    b = B.deploy({"from":account})
    a = A.deploy({"from":account})