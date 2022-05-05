from brownie import A, B, accounts

def main():

    account = accounts[0]

    # Deploy B first, then A
    b = B.deploy({"from":account})
    a = A.deploy({"from":account})

    # call A with B address and set num
    a.setVars(b, 10, {"from":account, "value": '1 ether'})

    print(a.num())
    print(b.num())