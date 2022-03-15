from brownie import SimpleStorage, accounts

def test_deploy():

    #Arrange
    account = accounts[0]

    #Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    #Assert
    assert starting_value == expected

def test_updating_storage():

    #Arrange
    account = accounts[0]
    transaction_from = {"from": account}

    #Act
    simple_storage = SimpleStorage.deploy(transaction_from)
    simple_storage.store(15)
    updated_value = simple_storage.retrieve()
    expected = 15

    #Assert
    assert updated_value == expected

def test_add_person():

    #Arrange
    account = accounts[0]
    transaction_from = {"from": account}

    #Act
    simple_storage = SimpleStorage.deploy(transaction_from)
    simple_storage.addPerson("Shimon", 2)
    my_favorite_number = simple_storage.nameToFavoriteNumber("Shimon")
    expected = 2

    assert my_favorite_number == expected