from brownie import BCT, OneUpCuban, accounts

def test_deploy_cuban():

    #Arrange
    deployer = accounts[0]
    amount = 100000000000000000000   # 100 tokens, 18 decimal precision

    #Act
    bct = BCT.deploy(amount, {"from":deployer})
    cuban = OneUpCuban.deploy(bct, {"from":deployer})

    my_balance = bct.balanceOf(deployer)

    cuban.updateBCTBalance()
    cuban_balance = cuban.getBCTBalance()

    #Assert
    assert my_balance == amount and cuban_balance == 0

