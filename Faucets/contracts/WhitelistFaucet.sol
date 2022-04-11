// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/access/Ownable.sol";

contract WhitelistFaucet is Ownable{

    // White-listed addresses
    mapping(address => bool) whitelistedAddresses;

    // Whitelist enabled
    bool public whiteListEnabled;

    modifier isWhitelisted(address _address) {
        require(whitelistedAddresses[_address] == true || whiteListEnabled == false, "Whitelist: You need to be whitelisted");
        _;
    }

    function addUserWL(address _addressToWhitelist) public onlyOwner {
        whitelistedAddresses[_addressToWhitelist] = true;
    }

    function setWhiteListEnabled(bool _newSetting) public onlyOwner {
        whiteListEnabled = _newSetting;
    }

    function removeUserWL(address _addressToRemove) public onlyOwner {
        require(whitelistedAddresses[_addressToRemove], "Address already not whitelisted");
        whitelistedAddresses[_addressToRemove] = false;
    }

    function verifyUserWL(address _whitelistedAddress) public view returns(bool) {
        return whitelistedAddresses[_whitelistedAddress];
    }

}