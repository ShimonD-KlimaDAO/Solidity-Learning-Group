from brownie import BCT, OneUpCuban, accounts

def test_cuban_getchange():

    #Arrange
    deployer = accounts[0]
    winner = accounts[1]
    amount = 200000000000000000000   # 200 tokens, 18 decimal precision

    #Act
    bct = BCT.deploy(amount, {"from":deployer})
    cuban = OneUpCuban.deploy(bct, {"from":deployer})

    bct.transfer(winner, (amount*0.5), {"from":deployer}) # 100 tokens each

    bct.approve(cuban, '100 ether' , {"from":deployer}) # approve from deployer 
    cuban.deposit('100 ether' , {"from":deployer})

    bct.approve(cuban, '100 ether' , {"from":winner}) # approve from winner 
    cuban.deposit('5 ether' , {"from":winner}) #expecting to get 4 BCT in change from the contract

    winner_cuban = cuban.winners(0)
    winner_balance = bct.balanceOf(winner)
    deployer_balance = bct.balanceOf(deployer)
    cuban_balance = cuban.getBCTBalance()

    #Assert
    assert winner_cuban == winner
    assert winner_balance == '99 ether'
    assert deployer_balance == '101 ether'
    assert cuban_balance == 0


