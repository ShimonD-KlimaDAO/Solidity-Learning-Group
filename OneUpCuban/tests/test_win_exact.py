from brownie import BCT, OneUpCuban, accounts

def test_winner_cuban_exact():

    #Arrange
    deployer = accounts[0]
    not_winner = accounts[1]
    winner = accounts[2]
    amount = 200000000000000000000   # 200 tokens, 18 decimal precision

    #Act
    bct = BCT.deploy(amount, {"from":deployer})
    cuban = OneUpCuban.deploy(bct, {"from":deployer})

    bct.transfer(not_winner, '100 ether', {"from":deployer}) # 100 tokens each
    bct.transfer(winner, '5 ether', {"from":deployer}) # 100 tokens each

    bct.approve(cuban, '100 ether' , {"from":not_winner}) # approve from deployer 
    cuban.deposit(100000000000000000000 , {"from":not_winner})

    bct.approve(cuban, '100 ether' , {"from":winner}) # approve from winner 
    cuban.deposit('1 ether' , {"from":winner})

    winner_cuban = cuban.winners(0)
    winner_balance = bct.balanceOf(winner)
    deployer_balance = bct.balanceOf(deployer)
    cuban_balance = cuban.getBCTBalance()

    #Assert
    assert winner_cuban == winner
    assert winner_balance == '4 ether'
    assert deployer_balance == '196 ether'
    assert cuban_balance == 0
