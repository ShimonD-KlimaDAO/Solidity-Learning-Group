from brownie import BCT, OneUpCuban, accounts

def test_cuban_multiple_winners():
##just started
    #Arrange
    deployer = accounts[0]
    winner_1 = accounts[1]
    winner_2 = accounts[2]
    winner_3 = accounts[3]
    amount = 500000000000000000000   # 500 tokens, 18 decimal precision

    #Act

    #deploy
    bct = BCT.deploy(amount, {"from":deployer})
    cuban = OneUpCuban.deploy(bct, {"from":deployer})

    #transfer
    bct.transfer(winner_1, '100 ether', {"from":deployer}) # 100 tokens each
    bct.transfer(winner_2, '100 ether', {"from":deployer}) # 100 tokens each
    bct.transfer(winner_3, '100 ether', {"from":deployer}) # 100 tokens each

    bct.approve(cuban, '100 ether' , {"from":deployer}) 
    cuban.deposit('100 ether' , {"from":deployer})

    bct.approve(cuban, '100 ether' , {"from":winner_1}) # approve from winner 
    cuban.deposit('100 ether' , {"from":winner_1}) # expecting to get 99 BCT in change from the contract
    # can assert that winner(0) is winner_1 and they have 99 BCT
    assert cuban.winners(0) == winner_1
    assert bct.balanceOf(winner_1) == '99 ether'


    bct.approve(cuban, '100 ether' , {"from":winner_1}) # approve from winner 
    cuban.deposit('99 ether' , {"from":winner_1}) # no change - balance is now 99 in the contract
    # can assert that winner_1 is out of BCT now
    assert cuban.getBCTBalance() == '99 ether'
    assert bct.balanceOf(winner_1) == 0

    #send all bct from winner 2 and winner 3
    bct.approve(cuban, '100 ether' , {"from":winner_2}) 
    cuban.deposit('2 ether' , {"from":winner_2})
    bct.approve(cuban, '100 ether' , {"from":winner_2}) 
    cuban.deposit('98 ether' , {"from":winner_2}) #winner 2 is declared and contract has 98 BCT, winner2 has none

    #winner 2 is declared and contract has 98 BCT, winner 2 has none
    assert bct.balanceOf(winner_2) == 0
    assert cuban.winners(1) == winner_2
    assert cuban.winners(0) == winner_1
    #two different ways of checking BCT balance for cuban contract
    assert cuban.getBCTBalance() == '98 ether'
    assert bct.balanceOf(cuban) == '98 ether'

    bct.approve(cuban, '100 ether' , {"from":winner_3}) 
    cuban.deposit('3 ether' , {"from":winner_3}) #winner 3 declared, contract has 0, and winner3 has 97
    assert cuban.winners(2) == winner_3
    assert cuban.getBCTBalance() == 0
    assert bct.balanceOf(cuban) == 0
    assert bct.balanceOf(winner_3) == '97 ether'