from brownie import A, D, accounts

def test_appendmemory():

    ### Arrange ###

    account = accounts[0]

    ### Act ###

    # Deploy D first, then A
    d = D.deploy({"from":account})
    a = A.deploy({"from":account})

    # call A with C address and set num
    a.setVars(d, 10, {"from":account, "value": '1 ether'})

    ### Assert ###
    # This doesn't return gibberish since we just appended a new state variable.
    assert a.num() == 20 and a.value() == '1 ether'

