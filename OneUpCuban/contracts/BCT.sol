// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BCT is ERC20 {
    // initial supply in wei
    constructor(uint256 initialSupply) ERC20("BaseCarbonTonne", "BCT") {
        _mint(msg.sender, initialSupply);
    }
}
