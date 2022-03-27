// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract Foo {
    event Log(string message);

    function log() public {
        emit Log("Foo was called");
    }
}

contract TopLevel {
    Foo foo;

    constructor(address _foo) {
        foo = Foo(_foo);
    }

    function callFoo() public {
        foo.log();
    }
}
