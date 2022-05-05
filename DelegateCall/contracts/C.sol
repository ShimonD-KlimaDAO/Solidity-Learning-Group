// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract C {
    // switched order of sender and num
    address public sender;
    uint public num;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num*2;
        sender = msg.sender;
        value = msg.value;
    }
}