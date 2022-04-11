from brownie import NBO, NBOFaucet, accounts, chain

def test_faucet():

    #Arrange
    owner = accounts[0]
    dev1_WL = accounts[1]
    dev2_WL = accounts[2]
    dev3_NoWL = accounts[3]
    amount = '100 ether'   # 100 tokens, 18 decimal precision

    #Act and assert
    nbo = NBO.deploy(amount, {"from":owner})
    faucet = NBOFaucet.deploy(nbo, 18, {"from":owner})

    # Send all tokens to faucet contract.
    nbo.transfer(faucet, '100 ether', {"from":owner})
    assert nbo.balanceOf(owner) == 0 and nbo.balanceOf(faucet) == '100 ether'
    
    # WL boolean
    assert faucet.whiteListEnabled() == False
    faucet.setWhiteListEnabled(True, {"from":owner})
    assert faucet.whiteListEnabled() == True

    # add dev1 and dev2 to WL and try using the faucet for all 3.
    faucet.addUserWL(dev1_WL, {"from":owner})
    faucet.addUserWL(dev2_WL, {"from":owner})

    faucet.send({"from":dev1_WL})
    faucet.send({"from":dev2_WL})
    #faucet.send({"from":dev2_WL})   --> uncommenting this correctly reverts with "FaucetError: Try again later"

    chain.sleep(301) # fast forward 5 minutes 
    faucet.send({"from":dev2_WL})

    chain.sleep(301) # fast forward 5 minutes 

    assert nbo.balanceOf(dev1_WL) == '1 ether' and nbo.balanceOf(dev2_WL) == '2 ether' and nbo.balanceOf(dev3_NoWL) == 0

    #faucet.send({"from":dev3_NoWL})   --> this reverts as expected when uncommented

    # remove dev2 from WL and try using faucet with dev2 - should revert.
    faucet.removeUserWL(dev2_WL, {"from":owner})
    #faucet.send({"from":dev2_WL})   --> this reverts as expected when uncommented

    # disable WL and attempt using faucet again for dev2_WL and for dev3_NoWL
    faucet.setWhiteListEnabled(False, {"from":owner})
    faucet.send({"from":dev2_WL})
    faucet.send({"from":dev3_NoWL})

    assert nbo.balanceOf(dev1_WL) == '1 ether' and nbo.balanceOf(dev2_WL) == '3 ether' and nbo.balanceOf(dev3_NoWL) == '1 ether'
