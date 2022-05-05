// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract B {
    // NOTE: storage layout must be the same as contract A
    uint public num;
    address public sender;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num*2;
        sender = msg.sender;
        value = msg.value;
    }
}