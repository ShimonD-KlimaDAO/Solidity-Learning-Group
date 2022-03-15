// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract EtherStore {

    mapping(address => uint) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {

        uint bal = balances[msg.sender];

        require(bal > 0, "Not enough ether");

        (bool sent, ) = msg.sender.call{value: bal}("");
        require(sent, "Failed to send Ether");

        balances[msg.sender] = 0;
        
    }

    // Helper function to check the balance of this contract
    function getBalance() external view returns (uint) {
        return address(this).balance;
    }
}