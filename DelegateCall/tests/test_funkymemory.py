from brownie import A, C, accounts

def test_funkymemory():

    ### Arrange ###

    account = accounts[0]

    ### Act ###

    # Deploy C first, then A
    c = C.deploy({"from":account})
    a = A.deploy({"from":account})

    # call A with C address and set num
    a.setVars(c, 10, {"from":account, "value": '1 ether'})

    ### Assert ###
    # This returns gibberish due to the memory location incompatibility/mixup
    assert a.num() == 20

