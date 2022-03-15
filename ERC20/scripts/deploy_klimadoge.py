from brownie import accounts, KlimaDoge


def main():

    account_me = accounts[0]
    account_not_me = accounts[4]


    amount = 100000000000000000000  # 100 tokens, 18 decimal precision
    erc20 = KlimaDoge.deploy(amount, {"from": account_me})

    my_tx = erc20.transfer(account_not_me, (amount*0.25))

    print(my_tx.info())
