from brownie import A, B, accounts

def test_setVars():

    ### Arrange ###

    account = accounts[0]

    ### Act ###

    # Deploy B first, then A
    b = B.deploy({"from":account})
    a = A.deploy({"from":account})

    # call A with B address and set num
    a.setVars(b, 10, {"from":account, "value": '1 ether'})

    ### Assert ###
    assert a.num() == 20 and b.num() == 0 and a.sender() == account and b.sender() == "0x0000000000000000000000000000000000000000"