// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract Malicious {
    event Log(string message);

    //fallback () external {
    //    emit Log("Malicious fallback was called");
    //}

    // Actually we can execute the same exploit even if this function does
    // not exist by using the fallback
    function logs() public {
        // 
        emit Log("Malicious was called");
    }
}