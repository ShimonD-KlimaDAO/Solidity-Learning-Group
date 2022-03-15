from brownie import KlimaDoge, accounts

def test_deploy():

    #Arrange
    account_me = accounts[0]
    amount = 100000000000000000000  # 100 tokens, 18 decimal precision

    #Act
    erc20 = KlimaDoge.deploy(amount, {"from":account_me})
    starting_balance = erc20.balanceOf(account_me)
    expected = amount

    #Assert
    assert starting_balance == expected

def test_transfer():

    #Arrange
    account_me = accounts[0]
    account_not_me = accounts[1]
    amount = 100000000000000000000   # 100 tokens, 18 decimal precision - decimals() is called in constructor

    #Act
    erc20 = KlimaDoge.deploy(amount, {"from":account_me})
    erc20.transfer(account_not_me, (amount*0.25))
    my_balance = erc20.balanceOf(account_me)
    expected = int((amount*0.75))

    #Assert
    assert my_balance == expected