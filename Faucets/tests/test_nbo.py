from brownie import NBO, accounts

def test_deploy_NBO():

    #Arrange
    account_me = accounts[0]
    amount = '100 ether'  # 100 tokens, 18 decimal precision

    #Act
    nbo = NBO.deploy(amount, {"from":account_me})
    starting_balance = nbo.balanceOf(account_me)
    expected = amount

    #Assert
    assert starting_balance == expected

def test_transfer_NBO():

    #Arrange
    account_me = accounts[0]
    account_not_me = accounts[1]
    amount = '100 ether'   # 100 tokens, 18 decimal precision

    #Act
    nbo = NBO.deploy(amount, {"from":account_me})
    nbo.transfer(account_not_me, '25 ether')
    my_balance = nbo.balanceOf(account_me)
    expected = '75 ether'

    #Assert
    assert my_balance == expected