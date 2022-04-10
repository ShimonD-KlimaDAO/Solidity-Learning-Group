// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NBO is ERC20 {
    // initial supply in wei
    constructor(uint256 initialSupply) ERC20("Nature Based Offset", "NBO") {
        _mint(msg.sender, initialSupply);
    }
}
