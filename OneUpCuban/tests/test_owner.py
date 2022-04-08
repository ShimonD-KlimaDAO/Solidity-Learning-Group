from brownie import BCT, OneUpCuban, accounts

def test_owner():

    #Arrange
    deployer = accounts[0] # also owner
    bob = accounts[1]
    amount = 100000000000000000000   # 100 tokens, 18 decimal precision

    newTargetAmount =  61000000000000000000 ; # 61 BCT
    newMinDeposit =    2000000000000000000; # 2 BCT

    #Act & Assert

    # original min deposit
    bct = BCT.deploy(amount, {"from":deployer})
    cuban = OneUpCuban.deploy(bct, {"from":deployer})

    assert cuban.minDeposit() == 1000000000000000000
    assert cuban.targetAmount() == 101000000000000000000

    # update min deposit

    # NOTE: calling something like cuban.changeMinDeposit(newMinDeposit, {"from":bob}) should (And does) revert since bob is not the owner
    cuban.changeMinDeposit(newMinDeposit, {"from":deployer})
    cuban.changeTargetAmount(newTargetAmount, {"from":deployer})

    assert cuban.minDeposit() == newMinDeposit
    assert cuban.targetAmount() == newTargetAmount

    # owner offsets balance
    bct.approve(cuban, '100 ether' , {"from":deployer}) # approve from deployer 
    cuban.deposit(30000000000000000000 , {"from":deployer})

    assert cuban.getBCTBalance() == '30 ether'

    cuban.offsetBalanceOwner({"from":deployer})
    assert cuban.getBCTBalance() == '0 ether'


