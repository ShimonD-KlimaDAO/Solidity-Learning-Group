from brownie import TopLevel, Foo, Malicious, accounts


def main():
    
    account = accounts[0]
    mal = Malicious.deploy({"from": account})
    foo = Foo.deploy({"from": account})
    top_level_good = TopLevel.deploy(foo, {"from": account})
    top_level_bad = TopLevel.deploy(mal, {"from": account})
    tx_good = top_level_good.callFoo()
    tx_bad = top_level_bad.callFoo()

    print(tx_good.info())
    print(tx_bad.info())
