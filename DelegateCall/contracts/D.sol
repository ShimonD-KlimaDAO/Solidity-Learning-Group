// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract D {
    // appending another variable!
    uint public num;
    address public sender;
    uint public value;
    uint public double_value;

    function setVars(uint _num) public payable {
        num = _num*2;
        sender = msg.sender;
        value = msg.value;
        double_value = value*2;
    }
}