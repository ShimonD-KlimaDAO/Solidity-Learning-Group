from brownie import NBO, NBOFaucet, accounts

def test_transfer_NBO():

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
    # remove dev2 from WL and try using faucet with dev2 - should revert.
    # change whiteListEnabled param to false again, then try with dev2 and should succeed.
