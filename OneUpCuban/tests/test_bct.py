from brownie import BCT, accounts

def test_deploy_BCT():

    #Arrange
    account_me = accounts[0]
    amount = 100000000000000000000  # 100 tokens, 18 decimal precision

    #Act
    bct = BCT.deploy(amount, {"from":account_me})
    starting_balance = bct.balanceOf(account_me)
    expected = amount

    #Assert
    assert starting_balance == expected

def test_transfer_BCT():

    #Arrange
    account_me = accounts[0]
    account_not_me = accounts[1]
    amount = 100000000000000000000   # 100 tokens, 18 decimal precision

    #Act
    bct = BCT.deploy(amount, {"from":account_me})
    bct.transfer(account_not_me, (amount*0.25))
    my_balance = bct.balanceOf(account_me)
    expected = int((amount*0.75))

    #Assert
    assert my_balance == expected